---
kind: moc
name: "choosing the seed"
status: active
added: "2026-08-22"
concepts:
  - "[[concepts/foreign-seed]]"
  - "[[concepts/sampling-frame]]"
  - "[[concepts/external-randomness]]"
  - "[[concepts/analogical-distance]]"
  - "[[concepts/directed-diversity]]"
  - "[[concepts/verbalized-sampling]]"
sources:
  - "[[literature/papers/zhao2026large]]"
  - "[[literature/papers/coronadoblazquez2025deterministic]]"
  - "[[literature/papers/zhang2025verbalized]]"
  - "[[literature/papers/uzzi2013atypical]]"
  - "[[literature/papers/fu2013meaning]]"
  - "[[literature/papers/cox2021directed]]"
tags: ["moc", "q1-choosing"]
---

# Choosing the seed

**Q1.** "Pick a random foreign topic" is meaningless until you fix a
population to draw from, a way to make the draw actually random, and how
far the draw is allowed to land. Get any of the three wrong and the seed
either isn't foreign or isn't random — it's the model narrating its own
favourite fields. This MoC organizes the six concepts that define and
defend that pipeline, problem down to operational sampler.

## Problem: the model can't be trusted to choose

- [[concepts/external-randomness]] — the load-bearing claim: an LLM asked to
  name something "at random" samples its own skewed prior, so the RNG has
  to live outside the model. No longer a hypothesis here — see below.
- [[concepts/verbalized-sampling]] — the nearest rebuttal: verbalizing a
  weighted *distribution* over candidates recovers much suppressed
  diversity without external RNG. Closes the gap, doesn't prove it reaches
  a uniform target — kept as an open ablation, not a replacement.

## Theory: what "far" means and why mixed beats pure

- [[concepts/analogical-distance]] — the non-monotone shape design-by-
  analogy literature reports: near sources add nothing, very far sources
  give metaphor without mechanism, a middle band is most productive
  ([[literature/papers/fu2013meaning]], abstract-only, flagged for re-fetch
  before H3). [[literature/papers/uzzi2013atypical]] corroborates the same
  "mixture beats purity" shape at a different unit of analysis (17.9M
  papers: hit papers pair a conventional citation core with an atypical
  fringe) — independent evidence for the curve H3 tests.
- [[concepts/foreign-seed]] packages three independently-varied attributes
  — source population, granularity (field/subfield/method, H4), distance
  (H3) — which is why choosing and integrating are separate project halves.

## Operational design: frame, sample, spread

- [[concepts/sampling-frame]] — the explicit finite population a seed is
  drawn from ("random" is undefined without one). Candidates compared on
  coverage/granularity/embeddability: OpenAlex topics (chosen — 4-level
  hierarchy, ~4.5k leaves, embeddable), Wikipedia category graph,
  MSC2020/ACM CCS/arXiv categories, CPC patent classes (TRIZ lineage),
  curated mechanism lists (best for H4, hand-built).
- [[concepts/directed-diversity]] — Cox et al.'s MST-based greedy
  farthest-point selection for a maximally-spread k-subset; a different
  objective from the sampler (random draw within a distance band, not
  maximal spread) but its selection mechanics and diversity-metric
  vocabulary (mean/min pairwise distance, centroid distance, entropy,
  Chamfer distance) are reused for this project's evaluation metrics.

## Evaluation

H1's diagnostic — is the draw distribution close to uniform over the
frame? — is the entry point. H3's diagnostic — does transfer depth vs.
distance follow the predicted non-monotone curve? — is downstream and
still open, scored against [[concepts/transfer-depth-ladder]].

## What's established: H1, closed

`experiments/2026-08-22-h1-llm-random-topic-skew/` (done, confirmed
strongly). 450 independent `claude -p` calls asking a model for a random
research topic, vs. 1000 `xpol` draws. Sonnet 5 mode-collapsed: **one
answer ("ethnomusicology of Andean panpipe traditions") 33/100 calls**,
71% duplicate rate, 8/26 fields, top-5 fields = 96% of mass. Haiku: 79%
duplicates on the realistic "foreign field for my ML problem" prompt, 60%
landing on forestry/ecology. The `xpol` sampler (`xpol/frame.py` +
`sampler.py` + `embed.py`, stratified-by-domain draw) hit 25–26/26 fields,
zero duplicates. The more capable model collapsed *harder*, matching
[[literature/papers/coronadoblazquez2025deterministic]] (model narrates a
cultural script about randomness rather than sampling one) and the
goodness-of-fit failure rates in [[literature/papers/zhao2026large]].
**External randomness is not optional; the sampler is the answer.**

## What's still open

- **H3 — distance sweep.** Not run. Bin `xpol` draws by distance from a
  fixed problem set, score transfer depth vs. distance against
  [[concepts/analogical-distance]]'s predicted curve.
- **H4 — granularity.** Field vs. subfield vs. named-method seeds; not
  started.
- **H5 — tournament.** k seeds → k proposals → judge merge/select;
  [[concepts/verbalized-sampling]] is a candidate proposal-step format
  (not the seed-draw step).
- **Verbalized-sampling ablation**: does "k diverse fields with
  probabilities" get closer to uniform over the frame than single-shot
  asking? Bounds how much of H1's skew is prompt-format artifact — not run.
- `fu2013meaning` re-fetch with institutional access — abstract-only,
  needed before H3's power analysis is credible.
