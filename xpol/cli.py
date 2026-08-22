"""CLI: `xpol sample`, `xpol prompt`, `xpol stats`."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .frame import Frame, LEVELS
from .sampler import Sampler, seeds_to_dicts

PROMPTS = Path(__file__).resolve().parent.parent / "prompts"


def _band(s: str | None):
    if not s:
        return None
    lo, hi = (float(x) for x in s.split(","))
    return (lo, hi)


def render(template: str, problem: str, seed, brief: str | None = None) -> str:
    t = (PROMPTS / f"{template}.md").read_text()
    return t.format(problem=problem.strip(), seed_name=seed.name, seed_path=seed.path,
                    seed_description=seed.description, seed_keywords=", ".join(seed.keywords),
                    brief=brief or "")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="xpol")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sample", help="draw k random foreign seeds")
    s.add_argument("-k", type=int, default=5)
    s.add_argument("--level", choices=LEVELS, default="topic")
    s.add_argument("--seed", type=int, default=None, help="RNG seed (default: OS entropy)")
    s.add_argument("--stratify", default="domain", help="domain | field | none")
    s.add_argument("--problem", default=None, help="problem text (or @file) to measure distance from")
    s.add_argument("--band", default=None, help="distance percentile band lo,hi e.g. 0.4,0.8")
    s.add_argument("--keep-home", action="store_true", help="do not exclude the problem's home field")
    s.add_argument("--exclude", nargs="*", default=None, help="field names to exclude")
    s.add_argument("--json", action="store_true")

    p = sub.add_parser("prompt", help="render an integration prompt for a sampled seed")
    p.add_argument("--problem", required=True, help="problem text or @file")
    p.add_argument("--template", default="abstract-reinstantiate")
    p.add_argument("-k", type=int, default=1)
    p.add_argument("--level", choices=LEVELS, default="topic")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--band", default="0.5,0.9")
    p.add_argument("--stratify", default="domain")

    sub.add_parser("stats", help="frame statistics")

    a = ap.parse_args(argv)
    if a.cmd == "stats":
        print(json.dumps(Frame().stats(), indent=2)); return

    problem = a.problem
    if problem and problem.startswith("@"):
        problem = Path(problem[1:]).read_text()
    sampler = Sampler()
    band = _band(getattr(a, "band", None)) if problem else None
    seeds, rec = sampler.sample(k=a.k, level=a.level, seed=a.seed, stratify=a.stratify,
                                problem=problem, band=band,
                                exclude_home=not getattr(a, "keep_home", False),
                                exclude_fields=getattr(a, "exclude", None))
    if a.cmd == "sample":
        if a.json:
            print(json.dumps({"record": rec, "seeds": seeds_to_dicts(seeds)}, indent=2)); return
        print(f"# rng seed {rec['seed']}  level={rec['level']}  population={rec['population']}"
              f"  eligible={rec.get('eligible')}  stratify={rec['stratify']}"
              + (f"  home={rec['home']['field']} / {rec['home']['subfield']}" if 'home' in rec else ""))
        for i, sd in enumerate(seeds, 1):
            d = f"  [d={sd.distance:.3f} p{int(sd.distance_pct*100):02d}]" if sd.distance is not None else ""
            print(f"{i:2d}. {sd.name}{d}\n    {sd.path}")
        return
    for sd in seeds:
        print(render(a.template, problem, sd))
        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()
