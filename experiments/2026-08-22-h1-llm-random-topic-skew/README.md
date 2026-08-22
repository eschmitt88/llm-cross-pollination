---
kind: experiment
slug: "h1-llm-random-topic-skew"
date: "2026-08-22"
status: done
hypothesis: "Asking an LLM to name a random research topic yields a heavily skewed distribution (few favourite fields, entropy far below the sampler's), so external randomness is necessary."
result: "Confirmed, strongly: model-chosen random topics are heavily skewed (Sonnet 5: 71% duplicates, one answer 33× in 100 calls, 8/26 fields; Haiku: 79% duplicates on broad prompts). The best prompt phrasing still reached only 17/26 fields and 0.7% Health Sciences. xpol sampler: 25–26/26 fields, zero duplicates."
related_concepts: ["external-randomness", "sampling-frame", "homogenization"]
related_literature: ["literature/papers/zhao2026large.md", "literature/papers/coronadoblazquez2025deterministic.md", "literature/papers/zhang2025verbalized.md"]
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

All 450 `claude -p` calls succeeded (`results/summary.json:*.failed_calls = 0`).
Answers were mapped to the nearest OpenAlex topic by embedding, then
aggregated by field (26) and domain (4). Reference = 1000 `xpol` draws.

| condition | n | field entropy (bits, max 4.70) | fields seen | top-5 field mass | duplicate answers | most common answer |
|---|---|---|---|---|---|---|
| haiku, "specific subfield, uniformly at random" | 150 | 3.59 | 17/26 | 0.61 | 11% | dendrochronology ×5, topological data analysis ×5 |
| sonnet, same prompt | 100 | 1.83 | 8/26 | 0.96 | 71% | "ethnomusicology of Andean panpipe traditions" ×33 |
| haiku, "random scientific discipline" | 100 | 2.26 | 10/26 | 0.92 | 79% | mycology ×41, seismology ×14 |
| haiku, "field far from ML to borrow from" | 100 | 2.14 | 10/26 | 0.91 | 79% | forestry ×32, ecology ×28 |
| **xpol, stratified by domain** | 1000 | 3.89 | 25/26 | 0.61 | 0% | — |
| **xpol, uniform over topics** | 1000 | 3.96 | 26/26 | 0.57 | 0% | — |

(`metrics.json`; full distributions and top answers in `results/summary.json`.)

Domain balance: the best model condition (haiku specific) was 60% Physical
Sciences, 29% Life, 11% Social, **0.7% Health Sciences**; Sonnet was 82%
Social Sciences. The stratified sampler is 25/25/25/25 by construction.

## Interpretation

- H1 confirmed, and more strongly than expected. The failure is not mild
  skew but *mode collapse*: Sonnet 5 produced essentially one answer
  (ethnomusicology variants = 57/100) despite being told to pick uniformly
  across all of scholarship. This matches the mechanism described in
  [[coronadoblazquez2025deterministic]] — the model narrates a script about
  "a random-sounding topic" rather than sampling — and the GoF failure
  rates in [[zhao2026large]].
- Prompt phrasing matters a lot (haiku: 11% vs 79% duplicates), but even
  the best phrasing leaves a third of fields unseen and health sciences
  absent. Phrasing is a mitigation, not a fix.
- The "foreign field for my ML problem" prompt — which is exactly what a
  user would type — is the worst case: 60% of answers were forestry or
  ecology. A user asking the model to pick the foreign seed gets the same
  two seeds every time. This is the concrete justification for
  [[external-randomness]] and for the sampler being a separate tool.
- Caveat: the nearest-topic mapping of free-text answers is approximate
  (e.g. "ethnomusicology" → some Arts and Humanities topic); it does not
  affect the duplicate-rate or top-answer findings, which are computed on
  raw strings.
- The sampler's field entropy is 3.9 rather than the 4.7 maximum because
  fields hold unequal numbers of topics (Medicine has the most). Whether
  to stratify by field rather than domain is a design choice, not a bug.

## Diagnostics

- intended_effect_confirmed: yes — sonnet duplicate rate 0.71 and top-5 field mass 0.96 vs sampler 0.00 / 0.61 (`metrics.json:sonnet_specific.duplicate_rate`, `metrics.json:xpol_sampler_stratified.top5_field_mass`)
- leakage_check: n/a — no held-out split; no tuning on these results
- overfitting_signal: n/a
- delta_from_prior: n/a — first experiment
- unexpected_findings: the more capable model (Sonnet 5) collapsed *harder* than Haiku (71% vs 11% duplicates on the same prompt) — capability does not buy randomness; and the realistic user prompt ("a field far from ML") is the worst-behaved (`results/summary.json:haiku_foreign_for_ml.top_answers`)
- next_candidates:
  - Test Verbalized Sampling (ask for 10 weighted candidates per call) as the best achievable in-model baseline, to quantify how far prompting alone can get ([[zhang2025verbalized]]).
  - Repeat with Opus 5 and with temperature variation once `claude -p` exposes it, to check whether collapse is model-family-wide.

## Follow-up

- ...
