---
kind: paper
title: "Directed Diversity: Leveraging Language Embedding Distances for Collective Creativity in Crowd Ideation"
authors: ["Samuel Rhys Cox", "Yunlong Wang", "Ashraf Abdul", "Christian von der Weth", "Brian Y. Lim"]
institutions: ["National University of Singapore"]
year: 2021
venue: "CHI 2021"
peer_reviewed: true
url: "https://arxiv.org/abs/2101.06030"
code_url: null
citations: null
source: "raw/papers/cox2021directed.pdf"
added: "2026-08-22"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["sampling-frame"]
tags: ["diversity-metrics", "prompt-selection", "embeddings"]
---

# Directed Diversity

## TL;DR

A system (Directed Diversity) that automatically selects maximally-diverse
prompts for crowd ideation by embedding candidate phrases (Universal
Sentence Encoder) and greedily picking points that are farthest apart in
embedding space, using a minimum-spanning-tree-based algorithm to make the
NP-hard "pick n maximally diverse points" problem tractable at scale. Ships
alongside a "Diversity Prompting Evaluation Framework" that consolidates
diversity metrics from several fields into a common toolkit.

## Claims

- Diverse, farthest-point prompt selection measurably increases collective
  creativity across four user studies vs. random or non-diverse prompt
  selection, evaluated along the full ideation chain (prompt selection →
  prompt creativity → ideation diversity).
- Random prompt selection is a weaker baseline than directed (farthest-
  point) selection on originality-related metrics, but not distinguishable
  on self-assessed quality — diversity and perceived quality are separable
  axes, consistent with this project's own novelty/usefulness split.

## Methods

- Universal Sentence Encoder embeddings of phrases extracted from a target-
  domain text corpus; pairwise angular distance as the base metric.
- A catalog of diversity metrics at two levels: **distance between two
  points** (pairwise distance, angular distance) and **diversity of a set**
  (mean/min pairwise distance, distance-from-centroid, entropy of spread,
  Chamfer distance between sets) — Table 2/3 in the paper is effectively a
  menu of diversity metrics with formulas.
- Scalable greedy selection: build a minimum spanning tree over the
  candidate embedding, use the dendrogram to select a diverse subset of
  size n without exhaustive search.

## Results

- The MST-based greedy diverse-selection algorithm is a directly reusable
  method: it's exactly "pick k maximally-spread points from a large
  embedded population," which is the [[sampling-frame]] sampler's
  distance-banded / stratified selection problem, minus the "external
  randomness" requirement (this system is deliberately maximizing spread,
  not sampling from a band — the project would need to adapt the objective
  from "farthest" to "within a target distance band, but randomly within
  it").
- Their diversity-metric catalog (mean pairwise distance, distance-from-
  centroid, entropy, Chamfer distance) is a ready-made checklist for this
  project's own evaluation metrics (`docs/research-plan.md`'s "Diversity:
  pairwise embedding distance among outputs across seeds").

## Critique / open questions

- Domain is crowd ideation prompts for motivational messaging, not STEM
  problem-solving or cross-domain technical transfer — the diversity
  *metrics* transfer cleanly, the *application* does not.
- Maximizing diversity is not the same objective as this project's H3
  (a useful mid-distance band, not the farthest points available) — worth
  remembering when adapting the selection algorithm.

## Trust signals

- **Credibility:** 4 — peer-reviewed at CHI 2021 (top-tier HCI venue),
  reputable institution (NUS), extensive empirical validation (simulation +
  4 user studies), no released code found at time of ingest.

## Follow-up

- **Relevance: 4** — doesn't seed a new hypothesis, but supplies two things
  the project can import directly: a scalable diverse-selection algorithm
  for the [[sampling-frame]] sampler, and a consolidated diversity-metric
  vocabulary for the evaluation harness. See also the new
  [[directed-diversity]] concept seeded from this paper.
