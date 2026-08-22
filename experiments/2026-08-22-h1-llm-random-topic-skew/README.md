---
kind: experiment
slug: "h1-llm-random-topic-skew"
date: "2026-08-22"
status: running
hypothesis: "Asking an LLM to name a random research topic yields a heavily skewed distribution (few favourite fields, entropy far below the sampler's), so external randomness is necessary."
result: ""
related_concepts: ["external-randomness", "sampling-frame", "homogenization"]
related_literature: []
tags: ["h1", "sampler", "randomness"]
---

# h1-llm-random-topic-skew

## Hypothesis

If we ask the model (via `claude -p`, independent calls, no shared context)
to "name a random research topic", the answers will concentrate on a small
set of fields. Measured against the OpenAlex frame (4 domains / 26 fields /
4516 topics): field-level entropy well below that of `xpol`'s stratified
sampler; top-5 fields carrying most of the mass; many exact-duplicate
answers. If instead the model is near-uniform, the whole "external
randomness" premise (H1) is wrong and the sampler is unnecessary.

## Setup

- Config: `config.yaml` — conditions × N, model pins, prompts.
- Code: `run.py` (collects answers in parallel via `claude -p --model …`),
  `analyze.py` (maps answers to nearest OpenAlex topic by embedding, then
  computes field/domain distributions, entropy, top-k mass, duplicate rate;
  same metrics for N draws from the `xpol` sampler as the reference).
- Data: `results/answers_<condition>.jsonl`, `results/summary.json`.

## Result

(fill after run)

## Interpretation

(fill after run)

## Diagnostics

- intended_effect_confirmed: n/a
- leakage_check: n/a — no held-out split in this experiment
- overfitting_signal: n/a
- delta_from_prior: n/a — first experiment
- unexpected_findings: n/a
- next_candidates:
  - n/a
  - n/a

## Follow-up

- ...
