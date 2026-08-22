import json, statistics as st
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = [json.loads(l) for l in open(HERE / "results" / "judgments.jsonl")]
rows = [r for r in rows if "transfer_depth" in r]
by = defaultdict(list)
for r in rows:
    by[r["strategy"]].append(r)
metrics = {}
for s, rs in sorted(by.items()):
    td = [r["transfer_depth"] for r in rs]; us = [r["usefulness"] for r in rs]
    metrics[s] = {"n": len(rs), "transfer_depth_mean": round(st.mean(td), 2),
                  "transfer_depth_ge3": round(sum(t >= 3 for t in td) / len(td), 2),
                  "usefulness_mean": round(st.mean(us), 2),
                  "usefulness_ge3": round(sum(u >= 3 for u in us) / len(us), 2),
                  "home_field_default_rate": round(sum(bool(r.get("home_field_default")) for r in rs) / len(rs), 2),
                  "depth3plus_and_useful3plus": round(sum(t >= 3 and u >= 3 for t, u in zip(td, us)) / len(rs), 2)}
# per-problem depth for the two ATR variants
per = defaultdict(lambda: defaultdict(list))
for r in rows:
    per[r["pid"]][r["strategy"]].append(r["transfer_depth"])
metrics["_per_problem_depth"] = {p: {s: round(st.mean(v), 1) for s, v in d.items()} for p, d in per.items()}
(HERE / "metrics.json").write_text(json.dumps(metrics, indent=2))
print(f"{'strategy':32s} n  depth  ≥3   useful ≥3   home-default  both≥3")
for s, m in metrics.items():
    if s.startswith("_"): continue
    print(f"{s:32s} {m['n']:2d}  {m['transfer_depth_mean']:.2f}  {m['transfer_depth_ge3']:.2f}  {m['usefulness_mean']:.2f}  {m['usefulness_ge3']:.2f}   {m['home_field_default_rate']:.2f}       {m['depth3plus_and_useful3plus']:.2f}")
