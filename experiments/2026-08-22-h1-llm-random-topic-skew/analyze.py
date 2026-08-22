"""Map free-text answers to the OpenAlex frame and compare distributions."""
import json, math, sys, yaml
from collections import Counter
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from xpol import Frame, Sampler
from xpol.embed import embed, topic_embeddings

HERE = Path(__file__).resolve().parent
cfg = yaml.safe_load((HERE / "config.yaml").read_text())
frame = Frame(); emb = topic_embeddings(frame)
FIELDS = sorted({t.field for t in frame.topics}); DOMAINS = sorted({t.domain for t in frame.topics})


def entropy(counter, support):
    n = sum(counter.values())
    return -sum((c / n) * math.log2(c / n) for c in counter.values() if c)


def describe(fields, domains, topics, answers=None):
    cf, cd, ct = Counter(fields), Counter(domains), Counter(topics)
    n = len(fields)
    d = {
        "n": n,
        "field_entropy_bits": round(entropy(cf, FIELDS), 3),
        "field_entropy_max_bits": round(math.log2(len(FIELDS)), 3),
        "fields_seen": len(cf), "fields_total": len(FIELDS),
        "top5_field_mass": round(sum(c for _, c in cf.most_common(5)) / n, 3),
        "top_fields": cf.most_common(8),
        "domain_dist": {k: round(v / n, 3) for k, v in cd.most_common()},
        "topic_entropy_bits": round(entropy(ct, None), 3),
        "unique_topics": len(ct), "top_topics": ct.most_common(8),
    }
    if answers is not None:
        ca = Counter(a.lower().strip(" .") for a in answers)
        d["unique_answers"] = len(ca); d["duplicate_rate"] = round(1 - len(ca) / n, 3)
        d["top_answers"] = ca.most_common(10)
    return d


summary = {}
for cond in cfg["conditions"]:
    p = HERE / "results" / f"answers_{cond['name']}.jsonl"
    if not p.exists():
        continue
    rows = [json.loads(l) for l in open(p)]
    answers = [r["answer"].splitlines()[0] for r in rows if r["ok"] and r["answer"]]
    v = embed(answers)
    nearest = (v @ emb.T).argmax(1)
    tops = [frame.topics[i] for i in nearest]
    summary[cond["name"]] = describe([t.field for t in tops], [t.domain for t in tops],
                                     [t.name for t in tops], answers)
    summary[cond["name"]]["failed_calls"] = sum(1 for r in rows if not r["ok"])

# reference: the sampler
s = Sampler(frame)
seeds, _ = s.sample(k=cfg["reference"]["sampler_n"], level="topic", seed=cfg["seed"], stratify="domain")
summary["xpol_sampler_stratified"] = describe([x.path.split(" > ")[1] for x in seeds],
                                              [x.path.split(" > ")[0] for x in seeds], [x.name for x in seeds])
seeds, _ = s.sample(k=cfg["reference"]["sampler_n"], level="topic", seed=cfg["seed"], stratify="none")
summary["xpol_sampler_uniform"] = describe([x.path.split(" > ")[1] for x in seeds],
                                           [x.path.split(" > ")[0] for x in seeds], [x.name for x in seeds])

(HERE / "results" / "summary.json").write_text(json.dumps(summary, indent=2))
metrics = {k: {m: v[m] for m in ("n", "field_entropy_bits", "fields_seen", "top5_field_mass", "topic_entropy_bits", "unique_topics")}
           for k, v in summary.items()}
for k, v in summary.items():
    if "duplicate_rate" in v:
        metrics[k]["duplicate_rate"] = v["duplicate_rate"]
(HERE / "metrics.json").write_text(json.dumps(metrics, indent=2))
for k, v in summary.items():
    print(f"{k:28s} n={v['n']:4d} H_field={v['field_entropy_bits']:.2f}/{v['field_entropy_max_bits']} fields={v['fields_seen']}/{v['fields_total']} top5={v['top5_field_mass']:.2f} uniq_topics={v['unique_topics']}"
          + (f" dup={v['duplicate_rate']:.2f}" if 'duplicate_rate' in v else ""))
    print("   top fields:", v["top_fields"][:5])
