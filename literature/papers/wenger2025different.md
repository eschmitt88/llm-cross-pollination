---
kind: paper
title: "We're Different, We're the Same: Creative Homogeneity Across LLMs"
authors: ["Emily Wenger", "Yoed Kenett"]
institutions: ["Duke University", "Technion — Israel Institute of Technology"]
year: 2025
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2501.19361"
code_url: null
citations: null
source: "raw/papers/wenger2025different.pdf"
added: "2026-08-22"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["homogenization", "sampling-frame"]
tags: ["homogenization", "cross-model", "dat", "creativity-tests"]
---

# We're Different, We're the Same

## TL;DR

Prior homogenization studies each used a *single* LLM, leaving open the
obvious escape hatch: maybe the narrowing is one vendor's quirk, and a
population of writers each using a different model would recover diversity.
This paper closes that hatch. Across a broad set of LLMs on standardized
creativity tests, LLM responses are far more similar to *other LLMs'*
responses than human responses are to each other. Homogenization is a
property of the model class, not of any one model.

## Claims

- Population-level diversity of LLM responses is significantly lower than
  human population diversity, and the gap survives controls for response
  structure and other confounds.
- Cross-model homogeneity is substantial: different LLM families converge
  on similar creative content, not merely similar formatting.
- Prompting the model for higher creativity via the system prompt yields
  only a slight increase in creativity and does not close the homogeneity
  gap.
- Speculative mechanism offered: representational/feature-space alignment
  across LLMs (a convergent-representations story) would predict exactly
  this shared, limited output range.

## Methods

- Standardized psychometric creativity instruments (DAT-family and related
  divergent-thinking tests — see [[olson2021naming]]) administered to both
  humans and a broad LLM panel.
- Population-level comparison: semantic similarity computed *among* the set
  of human responses and *among* the set of LLM responses, rather than
  scoring individual responses for quality. The unit of analysis is the
  spread of the response distribution.

## Results

- Headline for us: switching models is not a mitigation. Any intervention
  that relies on model diversity to supply idea diversity is building on
  sand.

## Critique / open questions

- Preprint; no peer-review signal found and no released code, so held at
  credibility 4 despite a well-posed design.
- Standardized creativity tests (name unrelated words, alternate uses) are
  short-form and far from STEM problem-solving. The homogeneity measured is
  over word/idea lists, not over solution strategies.
- The feature-space-alignment mechanism is postulated, not tested here.

## Trust signals

- **Credibility:** 4 — credible authorship (Wenger at Duke; Kenett is an
  established creativity/semantic-networks researcher at Technion), a
  genuine human baseline rather than a model-only comparison, and a
  question that is sharply posed and directly answered. Docked one point
  for preprint status and no released artifacts.

## Follow-up

- **Relevance: 4** — load-bearing for the project's framing in a specific
  way: it rules out "just use a different model" as the competing
  explanation and therefore as the competing intervention. That makes an
  *external*, model-independent seed source ([[external-randomness]],
  [[sampling-frame]]) more clearly necessary rather than merely convenient.
  Pairs with [[patel2026similarly]] (same senior author) which adds the
  time dimension to the same claim.
