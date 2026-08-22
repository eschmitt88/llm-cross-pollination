---
kind: experiment
slug: "h2-integration-bakeoff"
date: "2026-08-22"
status: done
hypothesis: "With identical seeds and problems, abstract-then-reinstantiate (and its isolated-brief variant) yields deeper transfer than naive injection or persona prompting, without losing usefulness."
result: "H2 and H6 supported: abstract-reinstantiate-brief mean transfer depth 3.29 (88% ≥ mechanism) vs naive 2.12 (41%); paired sign test 13 wins/1 loss, p=0.002; brief > plain abstract-reinstantiate 7/1 (p=0.07); persona ≈ naive. Usefulness flat (~2.2/4) across all strategies and baselines. Judge marks 94% of proposals as reachable by the home field: deep transfer mostly *rediscovers* known home-field methods via a foreign path. 4/72 seeded generations refused by the API bio-safety classifier (HIV, pesticide seeds)."
related_concepts: ["abstract-then-reinstantiate", "seed-brief-isolation", "transfer-depth-ladder", "novelty-usefulness-tradeoff"]
related_literature: ["literature/papers/jiang2024autotriz.md", "literature/papers/gentner1983structuremapping.md", "literature/papers/ding2023fluid.md", "literature/papers/yasunaga2023large.md", "literature/papers/zhang2025noveltybench.md"]
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

84 generations (Sonnet 5), 84 judgments (Opus 5), 0 parse errors, 4
generations refused by the API safety classifier (`[bio]`: the HIV/AIDS
seed for clay-vessel-bending, the pesticide-toxicity seed for
submerged-ring-stability) and recorded as refusals. Seeds per problem in
`results/seeds.json`; every proposal + prompt in `results/gen/`.

| strategy | n | transfer depth (0–4) | ≥ 3 (mechanism) | usefulness (0–4) | ≥ 3 | home-field-default |
|---|---|---|---|---|---|---|
| none (baseline) | 6 | 0 by construction | — | 2.17 | 0.17 | 1.00 |
| unconventional (baseline) | 6 | 0 by construction | — | 2.50 | 0.50 | 1.00 |
| naive | 17 | 2.12 | 0.41 | 2.24 | 0.24 | 0.94 |
| persona | 17 | 2.29 | 0.41 | 2.24 | 0.24 | 0.94 |
| abstract-reinstantiate | 17 | 2.94 | 0.76 | 2.18 | 0.18 | 0.94 |
| **abstract-reinstantiate-brief** | 17 | **3.29** | **0.88** | 2.29 | 0.29 | 0.94 |

(`metrics.json`.) Paired on the same (problem, seed), exact sign tests:

| comparison | n | wins / losses | p |
|---|---|---|---|
| brief vs naive | 16 | 13 / 1 | 0.002 |
| abstract-reinstantiate vs naive | 17 | 11 / 1 | 0.006 |
| brief vs abstract-reinstantiate | 16 | 7 / 1 | 0.070 |
| brief vs persona | 17 | 13 / 0 | <0.001 |
| persona vs naive | 16 | 5 / 4 | 1.0 |
| usefulness, brief vs naive | 16 | 3 / 2 | 1.0 |

Depth distribution: naive puts 5/17 at vocabulary-or-nothing; brief puts
15/17 at mechanism-or-method, 7 of them at method (runnable maths).
Usefulness rises weakly with depth (2.0 at depth ≤2 → 2.58 at depth 4,
seeded only). Per problem (brief / atr / naive / persona mean depth):
cnn-overfit 3.7/4.0/3.0/3.0 · game-outcome-drift 4.0/3.0/2.7/3.0 ·
submerged-ring 3.5/2.3/1.3/1.5 · rl-sample-efficiency 3.3/3.0/2.0/2.0 ·
ecg-artifact 3.0/3.0/2.0/2.3 · clay-vessel-bending 2.3/2.0/1.5/1.7.

## Interpretation

- **H2 supported.** The abstract → retrieve → map → re-instantiate
  template is what makes a random seed transfer: same seeds, same
  problems, 13/1 over naive injection. Persona prompting — the popular
  "you are an X expert" move — does nothing beyond naive (5/4). This
  matches the structure-mapping account ([[gentner1983structuremapping]]):
  transfer needs forced relational alignment, not a different speaker.
- **H6 directionally supported.** Writing the seed brief in a problem-blind
  call adds ~0.35 depth (7/1, p=0.07 at n=16). Mechanism: the joint-context
  model retrieves the parts of X that already resemble the problem; the
  blind brief brings X's own structure.
- **Usefulness is not hurt by seeding, and not helped.** All arms sit at
  2.2–2.3/4; the no-seed "be unconventional" baseline reaches 2.5. Deep
  transfer is not the same as a better idea.
- **The dominant outcome is rediscovery.** The judge flags 94% of
  proposals — including depth-4 ones — as reachable by the home field,
  with reasons like "retraces an import ML made years ago" (CVaR →
  DRO/tilted ERM), "already exists as example-tied dropout". Read the
  justifications in `results/judgments.jsonl`: the transfers are real, the
  destinations are usually known. Only 4/72 outputs were judged both
  genuinely foreign and useful. Random seeding at k=3 therefore mostly
  yields *a foreign derivation of a known method* — valuable when the
  practitioner did not know it, and a fresh framing otherwise, but rarely
  a method the field lacks.
- **Problem type matters more than strategy.** Modelling problems
  (cnn-overfit, game-outcome-drift) reach depth 3.7–4.0; the
  hard-constraint physical design problem (clay-vessel-bending, fixed
  shape and material) tops out at 2.3 with every strategy — the judge
  repeatedly notes the proposal collapses to "graded infill + internal
  stiffener wearing ecological labels".
- **Judge caveat.** One judge model, no human calibration yet. Its
  justifications are specific and internally consistent, and its harshness
  on `home_field_default` is if anything conservative — but the usefulness
  scale is the one to distrust until a human rates a subset.
- **Refusals are a real cost of random seeding.** 5.6% of seeded
  generations hit the API bio-safety classifier because the *seed*
  (HIV/AIDS, pesticide toxicity) is medical/toxicological. The sampler
  should resample on refusal rather than the user losing a slot.

## Diagnostics

- intended_effect_confirmed: yes — brief vs naive paired 13/1, p=0.002 (`metrics.json:abstract-reinstantiate-brief.transfer_depth_mean` 3.29 vs `naive` 2.12)
- leakage_check: `grep heldout run.py` → 0 hits; only `data/problems/dev.yaml` read — no leakage
- overfitting_signal: n/a — no training; judge prompt was not tuned on these results
- delta_from_prior: vs h1-llm-random-topic-skew — different question (sampler necessity vs integration), no shared metric; H1 `experiments/2026-08-22-h1-llm-random-topic-skew/metrics.json:sonnet_specific.duplicate_rate` = 0.71, here `metrics.json:abstract-reinstantiate-brief.transfer_depth_mean` = 3.29
- unexpected_findings: (1) 94% home-field-default even at depth 4 — transfer ≠ novelty, the common outcome is rediscovery (`results/judgments.jsonl`); (2) persona prompting is worthless for transfer (5/4 vs naive); (3) 4 API safety refusals caused by medical/toxicology seeds (`results/run.log`)
- next_candidates:
  - H5 tournament: k=8 seeds per problem with the brief template, judge selects the best — test whether the 6% "foreign and useful" rate scales with k (`results/judgments.jsonl` home_field_default=false cases).
  - Human calibration: the user rates 20 proposals on usefulness and home-field-default blind to the judge; compute agreement before trusting the usefulness column.
  - H3 distance sweep with the brief template only — bands 0.1–0.3, 0.3–0.6, 0.6–0.9, 0.9–1.0 — to see whether nearer seeds trade depth for foreignness.

## Follow-up

- Proposals worth a human read: `results/gen/cnn-overfit__abstract-reinstantiate__0.json` (plant stress → feedback-controlled regularisation, judged foreign+useful), `game-outcome-drift__abstract-reinstantiate-brief__0.json` (allelochemical decay kinetics → patch-effect half-lives), `submerged-ring-stability__abstract-reinstantiate-brief__0.json` (risk-based tax audit selection → sensor/actuator budget allocation).
