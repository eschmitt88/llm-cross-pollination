---
kind: concept
name: "external randomness"
status: growing
added: "2026-08-22"
sources: ["zhao2026large", "coronadoblazquez2025deterministic", "zhang2025verbalized", "chen2023probing", "priem2022openalex", "malthouse2021influence"]
related_concepts: ["foreign-seed", "sampling-frame", "homogenization", "verbalized-sampling"]
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

Two independent papers now give H1 hard numbers before we've even run it.
Zhao, Du & Wang audit 11 frontier LLMs against 15 target distributions and
find a 7% median goodness-of-fit pass rate for batch "random" generation,
collapsing to 0/11 models passing *any* distribution under independent
(stateless) calls — and the same failure propagates into categorical
tasks: GPT-4o asked to place a correct MCQ answer uniformly across
A/B/C/D instead produces 12.6% / 46.8% / 35.1% / 5.5% (χ²=444.5,
p<.001). Coronado-Blázquez replicates the qualitative picture on simple
numeric ranges (uniformity rejected at p as low as 2.19e-15) and adds a
mechanism: DeepSeek-R1's exposed chain-of-thought shows the model
retrieving *cultural scripts about how humans randomize* (digits of π,
current date/time, "gut instinct") rather than sampling — i.e. "pick a
random field" will likely retrieve stereotyped answers for the same
reason, not just produce numerically skewed ones. Both papers make the
MCQ/categorical result the closest available proxy for what H1 will find.

## Connections

- Stratified draws (one per top-level domain) keep a batch of k seeds
  spread — plain uniform sampling over a leaf-heavy frame would over-draw
  the big fields.
- Distance-banded sampling ([[analogical-distance]]) is still external
  randomness: the band restricts the population, the RNG picks within it.
- [[verbalized-sampling]] is the nearest thing to a counter-argument: a
  training-free prompting trick recovers much of a model's suppressed
  output diversity *without* external RNG. It increases spread relative to
  direct prompting, which is a different claim from "matches a target
  distribution" — worth an explicit ablation before assuming external
  randomness is strictly necessary rather than just the safest default.
