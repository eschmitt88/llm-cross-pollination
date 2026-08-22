---
kind: paper
title: "Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas"
authors: ["Xiang Hu", "Hongyu Fu", "Jinge Wang", "Yifeng Wang", "Zhikun Li", "Renjun Xu", "Yu Lu", "Yaochu Jin", "Lili Pan", "Zhenzhong Lan"]
institutions: ["Westlake University", "Zhejiang University", "University of Electronic Science and Technology of China", "China Life R&D Center", "Carnegie Mellon University", "Southeast University", "University of Oxford"]
year: 2024
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2410.14255"
code_url: null
citations: null
source: "raw/papers/hu2024nova.pdf"
added: "2026-08-22"
relevance: 3
credibility: 3
status: read
related_experiments: []
related_concepts: ["foreign-seed", "novelty-usefulness-tradeoff"]
tags: ["retrieval-planning", "diversity", "h2", "h5"]
---

# Nova

## TL;DR

Attacks the same problem as [[wang2024scimon]] — LLMs produce "simplistic
and repetitive suggestions" because they cannot acquire external knowledge
well — with an *iterative planning* layer that deliberately plans which
external knowledge to retrieve next, progressively broadening and deepening
the evidence base before generating. Reports **3.4x more unique novel
ideas** than without the framework, and at least **2.5x more top-rated
ideas** than the prior state of the art across 170 seed papers under a
Swiss-tournament evaluation.

## Claims

- Purposeful, planned, iterative retrieval beats single-shot or unplanned
  retrieval for idea novelty and diversity.
- 3.4x increase in the number of unique novel ideas produced, versus the
  ablation without the framework.
- ≥2.5x more top-rated ideas than the current state of the art, evaluated
  over 170 seed papers via a Swiss Tournament ranking.
- Validated by both automated and human assessment.

## Methods

- Iterative plan-then-retrieve loop over external knowledge, feeding
  progressive idea enrichment; Swiss-tournament pairwise ranking for
  evaluation over a 170-paper seed set.

## Results

- The multiplicative numbers (3.4x, 2.5x) are the headline and are the
  strongest quantitative case in the corpus that *deliberate, structured*
  knowledge injection beats default prompting on diversity.

## Critique / open questions

- **Treat the multipliers with caution.** "3.4x more unique novel ideas" is
  a count of items passing a novelty filter, not an effect size on a
  calibrated scale; such ratios are highly sensitive to the filter's
  threshold and to how "unique" is operationalized, neither of which is
  pinned down in the abstract. The comparison is also partly against the
  authors' own ablation.
- Preprint; no peer-review signal and no released code found, so the
  numbers are unreplicated. This is the main reason for credibility 3.
- Like SciMON, retrieval is aimed at *relevant* knowledge, so it broadens
  within a neighbourhood rather than jumping domains. It is a
  diversity-within-field method, not a cross-pollination method.
- Swiss-tournament evaluation is a reasonable ranking device but the judge
  and its self-preference behaviour are not scrutinised.

## Trust signals

- **Credibility:** 3 — plausible method with both automated and human
  evaluation and a sensible tournament design, but unreviewed, no artifacts,
  and headline numbers expressed as ratios whose denominators depend on
  unstated thresholds. Directionally useful; do not quote the multipliers as
  established.

## Follow-up

- **Relevance: 3** — supporting evidence rather than a foundation. Its real
  use is as prior art for **H5** (multiple seeds plus selection beats a
  single seed): Nova's planned-iterative-retrieval is a close cousin of the
  tournament arm, and its Swiss-tournament protocol is a reusable evaluation
  mechanic for ranking H5 candidates at reasonable cost. Cite alongside
  [[wang2024scimon]] as "structured injection > default prompting," with the
  preprint caveat attached.
