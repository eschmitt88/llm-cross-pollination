---
kind: concept
name: "external randomness"
status: seedling
added: "2026-08-22"
sources: []
related_concepts: ["foreign-seed", "sampling-frame", "homogenization"]
related_experiments: []
tags: ["q1-choosing", "h1"]
---

# External randomness

## Definition

The foreign topic is drawn by an RNG outside the model — OS entropy or a
seeded PRNG with the seed logged — never by asking the model to choose.

## Why it matters here

A language model asked to "name a random scientific field" samples from its
own skewed prior, not from a uniform distribution: the same few fields
recur, and the skew is exactly the [[homogenization]] the project exists to
defeat. Hypothesis H1 measures this directly (entropy of model picks vs.
uniform over a [[sampling-frame]]). Until H1 is run this is an assumption,
but a cheap one to test, so it is the first experiment.

Reproducibility follows for free: the seed in `config.yaml` reproduces the
seed list.

## Connections

- Stratified draws (one per top-level domain) keep a batch of k seeds
  spread — plain uniform sampling over a leaf-heavy frame would over-draw
  the big fields.
- Distance-banded sampling ([[analogical-distance]]) is still external
  randomness: the band restricts the population, the RNG picks within it.
