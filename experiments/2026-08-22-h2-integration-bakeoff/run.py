"""H2/H6 bake-off: sample seeds → render → generate (Sonnet) → judge (Opus)."""
import json, subprocess, sys, yaml, hashlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Run every `claude -p` from a directory outside any research project: the
# SessionEnd hook otherwise commits+pushes a journal line per call, and the
# project CLAUDE.md would leak into the sub-call context.
NEUTRAL = Path.home() / "projects" / ".claude-p-cwd"
NEUTRAL.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from xpol import Sampler
from xpol.cli import render, PROMPTS

cfg = yaml.safe_load((HERE / "config.yaml").read_text())
problems = yaml.safe_load((ROOT / cfg["problems"]).read_text())
GEN = HERE / "results" / "gen"; GEN.mkdir(parents=True, exist_ok=True)
JUD = HERE / "results" / "judgments.jsonl"


class Refused(Exception):
    """API-side safety refusal — terminal for this job, never retried."""


def call(model, prompt, retries=2):
    import time
    for attempt in range(retries + 1):
        r = subprocess.run(["claude", "-p", "--model", model, prompt], capture_output=True, text=True, timeout=600, cwd=NEUTRAL)
        if r.returncode == 0:
            return r.stdout.strip()
        msg = (r.stdout + r.stderr)[:300]
        if "can't help with this" in msg or "usage policy" in msg.lower():
            raise Refused(msg)
        if attempt < retries:
            time.sleep(20 * (attempt + 1))
    raise RuntimeError(f"{model} failed: {msg}")


def stable_seed(pid):
    return cfg["seed"] + int(hashlib.sha1(pid.encode()).hexdigest()[:6], 16)


# 1. seeds per problem (deterministic, logged)
sampler = Sampler()
seed_table = {}
for p in problems:
    seeds, rec = sampler.sample(k=cfg["seeds_per_problem"], level=cfg["level"], seed=stable_seed(p["id"]),
                                problem=p["text"], band=tuple(cfg["band"]), stratify="domain")
    seed_table[p["id"]] = {"record": rec, "seeds": [s.__dict__ for s in seeds], "_objs": seeds}
(HERE / "results" / "seeds.json").write_text(json.dumps(
    {k: {"record": v["record"], "seeds": v["seeds"]} for k, v in seed_table.items()}, indent=2, default=str))

# 2. jobs
jobs = []
for p in problems:
    for b, tmpl in cfg["baselines"].items():
        jobs.append({"pid": p["id"], "strategy": b, "si": 0, "seed": None,
                     "prompt": tmpl.format(problem=p["text"].strip())})
    for si, sd in enumerate(seed_table[p["id"]]["_objs"]):
        for strat in cfg["strategies"]:
            jobs.append({"pid": p["id"], "strategy": strat, "si": si, "seed": sd, "prompt": None})


def generate(job):
    key = f"{job['pid']}__{job['strategy']}__{job['si']}"
    out = GEN / f"{key}.json"
    if out.exists():
        return key
    p = next(x for x in problems if x["id"] == job["pid"])
    brief = None
    if job["strategy"] == "abstract-reinstantiate-brief":
        bpath = GEN / f"brief__{job['pid']}__{job['si']}.txt"
        if not bpath.exists():
            try:
                bpath.write_text(call(cfg["generator"], render("brief", "", job["seed"])))
            except Refused as e:
                out.write_text(json.dumps({"pid": job["pid"], "strategy": job["strategy"], "si": job["si"],
                                           "seed": job["seed"].__dict__, "prompt": None, "proposal": None,
                                           "refused": "brief: " + str(e)[:300]}, indent=1, default=str))
                print(f"  REFUSED brief {key}", flush=True); return key
        brief = bpath.read_text()
    prompt = job["prompt"] or render(job["strategy"], p["text"], job["seed"], brief=brief)
    rec = {"pid": job["pid"], "strategy": job["strategy"], "si": job["si"],
           "seed": None if job["seed"] is None else job["seed"].__dict__, "prompt": prompt}
    try:
        rec["proposal"] = call(cfg["generator"], prompt)
    except Refused as e:
        rec["proposal"] = None; rec["refused"] = str(e)[:300]
        print(f"  REFUSED {key}: {str(e)[:80]}", flush=True)
    except Exception as e:
        print(f"  ERROR {key}: {e}", flush=True)
        return None
    out.write_text(json.dumps(rec, indent=1, default=str))
    return key


def judge(key):
    done = {json.loads(l)["key"] for l in open(JUD)} if JUD.exists() else set()
    if key in done:
        return
    g = json.loads((GEN / f"{key}.json").read_text())
    if not g.get("proposal"):
        with open(JUD, "a") as f:
            f.write(json.dumps({"key": key, "pid": g["pid"], "strategy": g["strategy"], "si": g["si"],
                                "refused": True}) + "\n")
        return
    p = next(x for x in problems if x["id"] == g["pid"])
    seed_name = g["seed"]["name"] if g["seed"] else "(no seed — baseline; score transfer_depth 0)"
    seed_path = g["seed"]["path"] if g["seed"] else "n/a"
    jp = (PROMPTS / "judge.md").read_text().format(problem=p["text"].strip(), seed_name=seed_name,
                                                   seed_path=seed_path, proposal=g["proposal"])
    try:
        raw = call(cfg["judge"], jp)
    except Exception as e:
        print(f"  JUDGE ERROR {key}: {str(e)[:80]}", flush=True); return
    txt = raw[raw.find("{"): raw.rfind("}") + 1]
    try:
        j = json.loads(txt)
    except Exception:
        j = {"parse_error": raw[:300]}
    with open(JUD, "a") as f:
        f.write(json.dumps({"key": key, "pid": g["pid"], "strategy": g["strategy"], "si": g["si"], **j}) + "\n")


print(f"{len(jobs)} generations", flush=True)
with ThreadPoolExecutor(cfg["parallel"]) as ex:
    keys = []
    for i, k in enumerate(ex.map(generate, jobs)):
        if k: keys.append(k)
        if (i + 1) % 10 == 0:
            print(f"  gen {i+1}/{len(jobs)}", flush=True)
print("judging", flush=True)
with ThreadPoolExecutor(cfg["parallel"]) as ex:
    for i, _ in enumerate(ex.map(judge, keys)):
        if (i + 1) % 10 == 0:
            print(f"  judge {i+1}/{len(keys)}", flush=True)
print("done", flush=True)
