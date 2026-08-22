"""Collect independent 'name a random topic' answers via `claude -p`."""
import json, subprocess, sys, yaml
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
cfg = yaml.safe_load((HERE / "config.yaml").read_text())


def ask(model, prompt):
    r = subprocess.run(["claude", "-p", "--model", model, prompt],
                       capture_output=True, text=True, timeout=120)
    return {"ok": r.returncode == 0, "answer": r.stdout.strip(), "err": r.stderr.strip()[:200]}


for cond in cfg["conditions"]:
    out = HERE / "results" / f"answers_{cond['name']}.jsonl"
    done = sum(1 for _ in open(out)) if out.exists() else 0
    todo = cond["n"] - done
    if todo <= 0:
        print(cond["name"], "already complete"); continue
    print(f"{cond['name']}: {todo} calls to {cond['model']}", flush=True)
    with ThreadPoolExecutor(cfg["parallel"]) as ex, open(out, "a") as f:
        for i, res in enumerate(ex.map(lambda _: ask(cond["model"], cond["prompt"]), range(todo))):
            f.write(json.dumps(res) + "\n"); f.flush()
            if (i + 1) % 25 == 0:
                print(f"  {i+1}/{todo}", flush=True)
print("done")
