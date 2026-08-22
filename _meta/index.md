---
name: index
description: Entry-point index for this project's knowledge graph.
---

# Index

Orientation for the project knowledge graph. Updated by `/wrap`, `/ingest`,
and `/new-experiment`.

## Plan

- `docs/research-plan.md` — problem, hypotheses H1–H6, design space, phases.
- `docs/decisions/0001-scope-and-framing.md` — scope ADR.

## Maps of Content

(promote a cluster of ≥5 related concepts into `mocs/<theme>.md`)

Two clusters are already forming and will be MoC candidates once the
concepts have sources: **choosing the seed** (foreign-seed, sampling-frame,
external-randomness, analogical-distance) and **integrating the seed**
(structure-mapping, abstract-then-reinstantiate, seed-brief-isolation,
transfer-depth-ladder).

## Active experiments

- ~~H1~~ done: `experiments/2026-08-22-h1-llm-random-topic-skew/` — model-chosen "random topics" collapse (Sonnet 71% duplicates); sampler is necessary
- `experiments/2026-08-22-h2-integration-bakeoff/` — H2/H6: naive vs persona vs abstract-reinstantiate (±isolated brief) on the dev set

## Candidate reading (uncurated)

- `raw/_candidates/2026-08-22-llm-homogenization-and-diversity-metrics.md`
- `raw/_candidates/2026-08-22-cross-domain-prompting-techniques.md`
- `raw/_candidates/2026-08-22-random-topic-sampling-and-analogical-distance.md`

## Open questions

- Uniform vs. distance-banded sampling — is "random" the goal or "usably
  surprising"? (H3)
- Field-level vs. method-level seeds. (H4)
- Does the LLM judge inherit the homogenization bias it grades? Calibrate on
  human ratings before trusting any bake-off result.
- Which sampling frame: OpenAlex topics is the leading candidate (hierarchy +
  descriptions); CPC patent classes are the interesting outlier (solutions,
  not fields).
