---
kind: experiment
slug: "h2-integration-bakeoff"
date: "2026-08-22"
status: running
hypothesis: "With identical seeds and problems, abstract-then-reinstantiate (and its isolated-brief variant) yields deeper transfer than naive injection or persona prompting, without losing usefulness."
result: ""
related_concepts: ["abstract-then-reinstantiate", "seed-brief-isolation", "transfer-depth-ladder", "novelty-usefulness-tradeoff"]
related_literature: []
tags: ["h2", "h6", "integration", "bakeoff"]
---

# h2-integration-bakeoff

## Hypothesis

H2: integration strategy dominates. On the dev problem set with the *same*
three foreign seeds per problem (drawn by `xpol`, distance band 0.5–0.9,
home field excluded), the `abstract-reinstantiate` template scores higher on
the transfer-depth ladder (0–4) than `naive` and `persona`, and at least as
high on usefulness. H6: the `abstract-reinstantiate-brief` variant (seed
brief written in a problem-blind call, then injected) scores higher still on
depth. Two no-seed baselines (`none`, `unconventional`) anchor usefulness
and the judge's `home_field_default` flag.

## Setup

- Config: `config.yaml` — 6 dev problems × 3 seeds × 4 seeded strategies +
  2 baselines per problem. Generator Sonnet 5; judge Opus 5 (different model
  from the generator to dampen self-preference).
- Code: `run.py` (sample seeds, render prompts from `prompts/`, generate,
  judge), `analyze.py` (aggregate → `metrics.json`).
- Data: `data/problems/dev.yaml` only. `heldout.yaml` is not read.
- Outputs: `results/gen/*.json` (prompt, proposal), `results/judgments.jsonl`.

## Result

(fill after run)

## Interpretation

(fill after run)

## Diagnostics

- intended_effect_confirmed: n/a
- leakage_check: heldout.yaml never opened by run.py (grep) — n/a until run
- overfitting_signal: n/a
- delta_from_prior: n/a
- unexpected_findings: n/a
- next_candidates:
  - n/a
  - n/a

## Follow-up

- ...
