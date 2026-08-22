---
kind: paper
title: "Naming unrelated words predicts creativity"
authors: ["Jay A. Olson", "Johnny Nahas", "Denis Chmoulevitch", "Simon J. Cropper", "Margaret E. Webb"]
institutions: ["McGill University", "University of Melbourne"]
year: 2021
venue: "PNAS 118(25), e2022340118"
peer_reviewed: true
url: "https://doi.org/10.1073/pnas.2022340118"
code_url: "https://osf.io/bm5fd/"
citations: 135
source: "raw/papers/olson2021naming.md"
added: "2026-08-22"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: ["analogical-distance", "novelty-usefulness-tradeoff"]
tags: ["dat", "metric", "semantic-distance", "divergent-thinking"]
---

# Naming unrelated words predicts creativity (the DAT)

## TL;DR

Introduces the **Divergent Association Task**: name 10 nouns as different
from each other as possible; keep the first 7 valid ones; compute cosine
distance between all 21 pairs in GloVe space; average and multiply by 100.
That single number correlates with established creativity batteries about
as well as those batteries correlate with each other — but it takes ~90
seconds, scores automatically, and needs no human raters. Validated across
~8,900 participants in 98 countries.

## Claims

- The DAT correlates with the Alternative Uses Task on **flexibility**
  (r = 0.51 [0.29, 0.68], p < 0.001) and **originality** (r = 0.50 [0.28,
  0.68], p < 0.001) in the manually screened subset; not significantly with
  fluency (r = 0.21, p = 0.057). Study 1B replicated without screening
  (flexibility r = 0.35, originality r = 0.32, fluency r = 0.30).
- It also correlates with convergent thinking (Bridge-the-Associative-Gap
  appropriateness: r = 0.34 screened, r = 0.22 full).
- **Test-retest reliability r = 0.73** [0.57, 0.84] at 2 weeks — comparable
  to or better than rater-scored AUT (r = 0.61-0.70).
- Scores are near-invariant to demographics: all demographic factors
  combined explain **1%** of variance.
- Scoring is absolute rather than sample-relative, which is what makes
  cross-sample and cross-cultural comparison tractable.

## Methods

- GloVe pretrained on Common Crawl; cosine distance over 21 pairs of 7
  words; score = 100 x mean distance.
- Practical calibration given by the authors: scores usually fall in 65-90,
  rarely exceed 100 (theoretical max 200); < 50 usually signals
  misunderstood instructions (e.g. naming opposites); average is 75-80,
  95 is very high.
- Studies 1A-1C (validation, replication, test-retest) + preregistered
  Study 2 (demographics, large sample).

## Results

- Headline for us: a cheap, automatable, absolutely-scaled semantic-distance
  metric with a real psychometric validation pedigree.

## Critique / open questions

- The metric scores the *spread of a word list*, not the quality of a
  solution. It is a divergent-thinking proxy and says nothing about
  usefulness — exactly the asymmetry [[novelty-usefulness-tradeoff]] warns
  about. Using DAT-style distance as the sole outcome for H2/H3 would be
  gameable in precisely the way the project has already ruled out.
- GloVe is a 2014-era static embedding. For this project's purposes a modern
  sentence embedding is the obvious substitute, but note that swapping the
  embedding **breaks the published calibration** (the 65-90 band, the "under
  50 is poor" rule) — those constants are GloVe-specific and must be
  re-derived, not inherited.
- Validated on humans. [[chen2023probing]] is the LLM application, and
  [[patel2026similarly]] observes heavy word repetition across models on
  DAT, which hints the task may be saturating/contaminated for LLMs.

## Trust signals

- **Credibility:** 5 — PNAS, preregistered confirmatory study, ~8,900
  participants across 98 countries, explicit test-retest reliability,
  scoring code and data public on OSF, 135 citations. Full text read from
  the Europe PMC open-access copy (PMC8237676).

## Follow-up

- **Relevance: 4** — the methodological ancestor of the distance machinery
  this project needs. Directly useful in two places: (1) as the design
  pattern for scoring how *spread* a set of sampled seeds is (a sanity check
  on [[sampling-frame]] draws, complementing the H1 entropy analysis), and
  (2) as a cautionary template — pair any distance score with a usefulness
  score. Do **not** adopt the GloVe constants; re-derive the band for
  whatever embedding `xpol` uses.
