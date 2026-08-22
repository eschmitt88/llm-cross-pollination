---
kind: concept
name: "transfer depth ladder"
status: seedling
added: "2026-08-22"
sources: []
related_concepts: ["structure-mapping", "novelty-usefulness-tradeoff", "foreign-seed"]
related_experiments: []
tags: ["evaluation", "q2-integrating"]
---

# Transfer depth ladder

## Definition

An ordinal rubric for what actually crossed from seed to problem:

0. **none** — seed ignored or mentioned and dropped
1. **vocabulary** — the output is the home-field answer wearing the seed's words
2. **metaphor** — a loose "it's like X" framing that suggests no concrete step
3. **mechanism** — a specific causal mechanism from the seed is mapped to a specific element of the problem, with the correspondence stated
4. **method** — a procedure (ideally with its math / algorithm) transferred and adapted so it could be run

## Why it matters here

Diversity metrics reward *different*; this rubric rewards *transferred*.
Levels 3–4 are the project's target. It is the primary outcome measure in
the integration bake-off (H2), the granularity test (H4), the isolation test
(H6), and the distance sweep (H3). Scored by an LLM judge with this rubric
and calibrated on a human-rated subset.

## Connections

- Derived from [[structure-mapping]]: the rungs are increasing amounts of
  relational structure surviving the mapping.
- Paired with usefulness in [[novelty-usefulness-tradeoff]] — a level-4
  method that is wrong for the problem is still not useful.
