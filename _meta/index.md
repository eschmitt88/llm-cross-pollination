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
- `docs/decisions/0002-default-integration-strategy.md` — brief template, k=5, no persona.
- `docs/method.md` — the method v0.1 (evidence-tagged); `skill/cross-pollinate/` — install-ready skill.

## Maps of Content

- `mocs/choosing-the-seed.md` — Q1: frame, external RNG, distance, directed diversity (H1 closed)
- `mocs/integrating-the-seed.md` — Q2: structure mapping → abstract-reinstantiate / isolated brief → transfer-depth ladder (H2 running)


## Active experiments

- ~~H1~~ done: `experiments/2026-08-22-h1-llm-random-topic-skew/` — model-chosen "random topics" collapse (Sonnet 71% duplicates); sampler is necessary
- ~~H2/H6~~ done: `experiments/2026-08-22-h2-integration-bakeoff/` — abstract-reinstantiate-brief 3.29 depth vs naive 2.12 (13/1, p=0.002); persona ≈ naive; 94% rediscovery

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
