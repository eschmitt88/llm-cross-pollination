---
kind: concept
name: "sampling frame"
status: seedling
added: "2026-08-22"
sources: []
related_concepts: ["foreign-seed", "external-randomness", "analogical-distance"]
related_experiments: []
tags: ["q1-choosing"]
---

# Sampling frame

## Definition

The explicit, finite population from which a [[foreign-seed]] is drawn. "Pick
a random topic" is undefined until the frame is named; the frame fixes both
what *can* be chosen and what "uniform" means.

## Why it matters here

Candidate frames differ on coverage, granularity, and whether a distance
metric is cheap to compute:

| frame | granularity | notes |
|-------|-------------|-------|
| OpenAlex topics | domain → field → subfield → topic (~4.5 k leaves) | has descriptions → embeddable; hop distance free |
| Wikipedia vital articles / category graph | any | huge, uneven, includes non-STEM |
| MSC2020, ACM CCS, arXiv categories | field/subfield | STEM-only, tidy, shallow |
| CPC patent classes | solution-level | the TRIZ lineage — patents are *solutions* |
| curated mechanism lists (named effects, reactions, algorithms) | method | best for H4, but hand-built and therefore biased |

A frame is also what makes H1 measurable: the model's "random" picks can be
compared against uniform over the frame.

## Connections

- Stratify by the frame's top level so a batch of seeds is spread across
  domains — [[external-randomness]].
- The frame entries must be embeddable for distance-banded sampling —
  [[analogical-distance]].
