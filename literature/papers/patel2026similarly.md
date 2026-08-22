---
kind: paper
title: "Are LLMs becoming similarly creative? Evidence from three years of models"
authors: ["Nirav Patel", "Josiah Crossman", "Eva Aggarwal", "Emily Wenger"]
institutions: ["Duke University"]
year: 2026
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2608.19437"
code_url: null
citations: null
source: "raw/papers/patel2026similarly.pdf"
added: "2026-08-22"
relevance: 2
credibility: 3
status: read
related_experiments: []
related_concepts: ["homogenization"]
tags: ["homogenization", "longitudinal", "dat", "aut"]
---

# Are LLMs becoming similarly creative?

## TL;DR

The longitudinal companion to [[wenger2025different]]: every prior
homogenization result is a snapshot, so this paper asks whether the
snapshots are trending. Across three years of model releases evaluated on
the Alternate Uses Task and a corpus of real open-ended user queries
(Infinity-Chat), cross-provider output distances *decline* significantly
over time. Models are converging, not diversifying.

## Claims

- Statistically significant decrease in LLM output diversity across the
  observation period, on both the psychometric task (AUT) and the
  real-world open-ended prompt set.
- The decline is *cross-provider* — distances between different vendors'
  outputs shrink, so this is industry-level convergence rather than one
  lab's models drifting.
- Notable intra-model repetition: on DAT, a small set of words (e.g.
  "ocean") recurs heavily across model responses.
- Framing claim: if the trend persists, LLM-driven homogenization
  progressively erodes human agency in co-creative work.

## Methods

- Select models spanning ~3 years of releases; elicit responses to AUT and
  to Infinity-Chat100 (a curated set of real open-ended user queries);
  compute sentence-embedding similarity; regress diversity on release date.

## Results

- Direction and significance are reported; the paper is explicit that this
  is a *preliminary* analysis (12 pages, 4 figures).

## Critique / open questions

- Self-described preliminary; small figure count, no released code found,
  not peer reviewed. The confound is serious and only partly addressed:
  newer models differ from older ones in many ways besides recency
  (post-training recipe, safety tuning, distillation from shared
  teachers), so "time" is a proxy for a bundle of causes.
- Model selection over a 3-year window is itself a researcher degree of
  freedom that can move the slope.
- Embedding-similarity-of-short-responses is a coarse instrument; see
  [[saakyan2026death]] for why surface-level novelty metrics mislead.

## Trust signals

- **Credibility:** 3 — plausible design and a useful question, from the
  same group as [[wenger2025different]], but preliminary by the authors'
  own description, unreviewed, no artifacts, and vulnerable to the
  recency-confound above. Treat the *direction* as suggestive and the
  magnitude as unestablished.

## Follow-up

- **Relevance: 2** — motivational framing only ("is the problem getting
  worse"), not load-bearing for any hypothesis. Cite it in the project's
  introduction if at all, with the preliminary caveat attached; do not
  build a design decision on it. The one methodologically useful nugget is
  the Infinity-Chat100 prompt set as a source of *real* open-ended queries,
  which could seed the dev problem set.
