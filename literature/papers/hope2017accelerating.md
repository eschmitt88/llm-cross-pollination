---
kind: paper
title: "Accelerating Innovation Through Analogy Mining"
authors: ["Tom Hope", "Joel Chan", "Aniket Kittur", "Dafna Shahaf"]
institutions: ["The Hebrew University of Jerusalem", "Carnegie Mellon University"]
year: 2017
venue: "KDD 2017"
peer_reviewed: true
url: "https://arxiv.org/abs/1706.05585"
code_url: null
citations: null
source: "raw/papers/hope2017accelerating.pdf"
added: "2026-08-22"
relevance: 3
credibility: 4
status: read
related_experiments: []
related_concepts: ["analogical-distance", "sampling-frame"]
tags: ["q1-choosing", "analogical-distance", "purpose-mechanism", "pre-llm"]
---

# Accelerating Innovation Through Analogy Mining

## TL;DR

Pre-LLM (2017) but foundational: decomposes product descriptions into
**purpose** ("what it does") and **mechanism** ("how it does it") vector
representations, learned via crowdsourced annotation + a recurrent neural
net, then defines a "far analogy" as *high purpose similarity, low
mechanism similarity* — i.e. same problem, different solution approach.
In a controlled ideation experiment, inspirations retrieved this way
produced good ideas at roughly **1.5–2.7x the rate** of TF-IDF or random
baselines. This paper is the clearest formal operationalization of "near
vs far analogy" the project will find, and directly anchors
[[analogical-distance]].

## Claims

- Human analogical retrieval is biased toward "near" (surface-similar,
  within-domain) matches and struggles to retrieve "far" (structurally
  similar, cross-domain) ones, even though far analogies are more
  strategically valuable — a well-known cognitive-science finding (Gick &
  Holyoak-style) that the paper operationalizes computationally.
- A **weak structural representation** (purpose + mechanism, not full
  predicate-calculus schemas) is learnable at scale and is expressive
  enough to support useful analogical retrieval — a deliberate
  expressivity/tractability tradeoff.
- Distance is a controllable, two-dimensional retrieval query, not a
  single scalar: same-purpose+different-mechanism ("far" analogy, good
  for re-solving) vs. same-mechanism+different-purpose ("re-purposing").

## Methods

- Corpus: ~8,000 Quirky.com crowdsourced product descriptions.
- Crowdsourcing: AMT workers search for analogous products and label
  purpose/mechanism attributes; a model is trained (RNN-based) on these
  behavioral traces to produce purpose and mechanism embeddings for any
  new product description.
- Formal query definitions (directly reusable as pseudocode for a
  distance-banded sampler):
  - *Same purpose, different mechanism* ("far" analogy): minimize
    purpose-distance subject to mechanism-distance ≥ threshold.
  - *Same mechanism, different purpose* ("re-purposing"): minimize
    mechanism-distance subject to purpose-distance ≥ threshold.
- Ideation experiment: 38 AMT workers redesign a product (a phone
  charger case) under 3 within-subjects conditions — ANALOGY (their
  near-purpose/far-mechanism retrieval, 12 inspirations), BASELINE:
  SURFACE (TF-IDF top-12, simulating a keyword search engine), BASELINE:
  RANDOM (12 random products). Two-phase task: 1 minute unassisted
  ideation, then 6 minutes with 12 inspirations shown.
- "Good idea" judged by 5 graduate raters against three explicit criteria
  (directly reusable as a rubric component): (1) uses a *different*
  mechanism/technology than the original (novelty), (2) achieves the
  *same purpose* as the original (quality/relevance), (3) implementable
  with existing technology, does not defy physics (feasibility).

## Results

- k=2 rater threshold: analogy condition 46% good ideas vs. random 37%
  vs. TF-IDF 30% (χ² p ≤ .01).
- k=3 (majority vote, stricter): analogy 38% vs. random 22% vs. TF-IDF
  21% (p < .01) — the advantage *grows* under the stricter threshold.
- Mixed-effects logistic regression confirms significance controlling for
  participant and seed-product random effects (p < .01 for both
  comparisons, both k).
- Precision/recall of the purpose+mechanism retrieval model itself beats
  TF-IDF/LSA/LDA/GloVe baselines on a held-out analogy-labeling task.

## Critique / open questions

Pre-LLM: a *retrieval* system over a fixed real-world corpus (Quirky
products), not prompt engineering — the transfer mechanism (retrieve a
real analogous product) differs structurally from this project's approach
(sample a foreign field, prompt an LLM); the concept transfers, the
method does not. Confidence intervals on the ideation results are wide
(n=38). No exploration of a "too far" regime — their far-analogy
definition is a single threshold, not a distance band — so it doesn't
directly test H3, though it supplies the vocabulary to build one.

## Trust signals

- **Credibility:** 4 — CMU + Hebrew University, peer-reviewed at KDD
  2017, rigorous crowdsourced experiment with mixed-effects stats; no
  code/data release found; methodology (RNN + crowdsourced labels) is
  now dated relative to LLM-era approaches.

## Follow-up

- **Relevance: 3** — Formalizes the near/far, purpose/mechanism
  vocabulary [[analogical-distance]] needs; its rater rubric (different
  mechanism + same purpose + feasible) is a good scaffold for scoring
  rung 3–4 of the [[transfer-depth-ladder]]. The right citation for
  "near-analogy bias is a known, measured human phenomenon," predating
  the LLM literature.
