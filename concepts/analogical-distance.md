---
kind: concept
name: "analogical distance"
status: seedling
added: "2026-08-22"
sources: []
related_concepts: ["foreign-seed", "sampling-frame", "structure-mapping", "transfer-depth-ladder"]
related_experiments: []
tags: ["q1-choosing", "h3"]
---

# Analogical distance

## Definition

How far the seed's domain is from the problem's domain. Operationalised two
ways here: cosine distance between embeddings of the problem statement and
the frame entry, and hop distance in the frame's taxonomy.

## Why it matters here

The design-by-analogy literature (Fu, Chan, Cagan et al. on "near" vs "far";
Chan & Schunn) reports a non-monotone effect: near sources add little, very
far sources produce metaphor without mechanism, and a middle band is most
productive. Hypothesis H3 tests whether that holds for LLM-assisted STEM
work. If it does, the sampler should draw from a **distance band** rather
than uniformly — "random" becomes "random within the useful band".

## Connections

- Relational vs. surface similarity ([[structure-mapping]]) is the deeper
  notion; embedding distance is a cheap proxy that mostly tracks surface
  similarity. A seed can be far in embedding space and structurally near —
  which is exactly the kind we want. Worth a second metric eventually.
- Output of the sweep is plotted as [[transfer-depth-ladder]] score vs.
  distance.
