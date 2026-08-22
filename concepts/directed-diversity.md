---
kind: concept
name: "directed diversity"
status: seedling
added: "2026-08-22"
sources: ["cox2021directed"]
related_concepts: ["sampling-frame", "external-randomness", "analogical-distance"]
related_experiments: []
tags: ["q1-choosing", "method"]
---

# Directed diversity

## Definition

Selecting a maximally-spread subset of k points from a large embedded
population by greedy farthest-point selection over a minimum spanning tree
of the embedding space — a scalable substitute for the NP-hard "pick k
maximally diverse points" problem. From Cox et al. 2021 (CHI), where it
selects diverse crowd-ideation prompts from embedded text phrases.

## Why it matters here

It's a different objective from what this project's sampler needs — Cox et
al. want the *most* spread-out set available; the [[sampling-frame]]
sampler wants a set drawn *randomly within a target distance band*
([[analogical-distance]]), which is deliberately not maximal spread. But
the algorithm is directly adaptable (constrain the MST-based selection to
candidates within the band, then pick among survivors with external
randomness — [[external-randomness]] — rather than greedily), and the
paper's diversity-metric catalog (mean/min pairwise distance,
distance-from-centroid, entropy of spread, Chamfer distance between sets)
is a ready-made vocabulary for this project's own evaluation metrics
(pairwise embedding distance among outputs, per `docs/research-plan.md`).

## Connections

- Feeds the [[sampling-frame]] sampler's selection step once a candidate
  population and distance band are fixed.
- Distinct from [[verbalized-sampling]]: directed diversity operates on an
  *external* embedded population (the frame), verbalized sampling operates
  *inside* the model's own output distribution. They solve diversity at
  different points in the pipeline — one for choosing the seed, one
  (potentially) for the integrator eliciting multiple candidate mappings.
