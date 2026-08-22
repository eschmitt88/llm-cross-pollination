---
kind: paper
title: "Probing the \"Creativity\" of Large Language Models: Can Models Produce Divergent Semantic Association?"
authors: ["Honghua Chen", "Nai Ding"]
institutions: ["Zhejiang University"]
year: 2023
venue: "Findings of EMNLP 2023"
peer_reviewed: true
url: "https://arxiv.org/abs/2310.11158"
code_url: null
citations: null
source: "raw/papers/chen2023probing.pdf"
added: "2026-08-22"
relevance: 2
credibility: 4
status: read
related_experiments: []
related_concepts: ["external-randomness"]
tags: ["dat", "metric", "decoding-strategy", "temperature"]
---

# Probing the "Creativity" of LLMs

## TL;DR

Applies [[olson2021naming]]'s DAT to LLMs. With greedy decoding GPT-4
outscores 96% of humans and GPT-3.5-turbo beats the human average.
Stochastic sampling and temperature scaling raise DAT scores for every
model *except* GPT-4, at the cost of stability.

## Claims

- Greedy search: GPT-4 > 96th human percentile; GPT-3.5-turbo > human mean.
- Stochastic sampling / temperature scaling improve DAT scores for most
  models but introduce a creativity-vs-stability trade-off.
- GPT-4 is the exception — sampling does not help it, suggesting its greedy
  output is already near its divergent-association ceiling.
- Interpretation offered: advanced LLMs possess divergent semantic
  association, a process underlying creativity.

## Methods

- DAT administered to a panel of LLMs across decoding strategies (greedy,
  stochastic sampling, varied temperature); scores computed with the
  standard GloVe pipeline and compared against Olson et al.'s human
  distribution.

## Results

- The decoding-strategy finding is the useful part: **temperature buys
  measured diversity but costs stability**, and the trade-off curve differs
  per model.

## Critique / open questions

- Scoring an LLM on a human psychometric instrument invites a validity
  objection the paper does not resolve: DAT was validated as a *predictor of
  human creativity*, and a high score from a system that has memorized the
  semantic-distance structure of the embedding space does not carry the same
  construct meaning. "GPT-4 beats 96% of humans" is a statement about the
  metric, not clearly about creativity.
- Contamination is plausible and untested: DAT and its example words are
  public and on OSF. [[patel2026similarly]] later reports heavy cross-model
  repetition on DAT ("ocean" recurring), which is consistent with a
  saturated/contaminated task.
- Single-task, list-of-words scope; no bearing on solution quality.

## Trust signals

- **Credibility:** 4 — peer-reviewed (Findings of EMNLP 2023), a
  well-established group at Zhejiang University, straightforward and
  correctly-executed application of a published instrument. Docked one for
  no released code and for not engaging the construct-validity objection.

## Follow-up

- **Relevance: 2** — mostly context rather than a load-bearing input. Its
  one directly usable result is the decoding-strategy sweep: it supplies
  prior evidence for how temperature trades diversity against stability,
  which is relevant to specifying the **"just raise temperature" baseline
  arm** in H5. It also quietly reinforces [[external-randomness]] — model
  diversity here is bought with a sampling knob that degrades stability,
  whereas an external seed source costs nothing in stability.
