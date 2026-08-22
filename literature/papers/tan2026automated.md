---
kind: paper
title: "Automated Creativity Evaluation of Language Models Across Open-Ended Tasks"
authors: ["Min Sen Tan", "Zachary Kit Chun Choy", "Syed Ali Redha Alsagoff", "Nadya Yuki Wangsajaya", "Mohor Banerjee", "Swaagat Bikash Saikia", "Alvin Chan"]
institutions: ["Raffles Institution", "Nanyang Technological University"]
year: 2026
venue: "ACL 2026 (Main Conference)"
peer_reviewed: true
url: "https://arxiv.org/abs/2606.11762"
code_url: "https://github.com/tanminsen/creativity-eval"
citations: null
source: "raw/papers/tan2026automated.pdf"
added: "2026-08-22"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["novelty-usefulness-tradeoff"]
tags: ["metrics", "semantic-entropy", "llm-judge", "eval-design", "macgyver"]
---

# Automated Creativity Evaluation Across Open-Ended Tasks

## TL;DR

A domain-agnostic, two-sided creativity evaluation framework: **divergent**
creativity via *semantic entropy* (reference-free, sampling-based —
cluster generations by meaning via an entailment model, take entropy over
cluster probabilities), and **convergent** creativity via a retrieval-based
multi-agent LLM judge. The key design move is separating the measurement
apparatus from the task, so the same instrument works across domains.
Validated on problem-solving (MacGyver), research ideation (HypoGen), and
creative writing (BookMIA).

## Claims

- Semantic entropy (adapted from Farquhar et al.'s hallucination-detection
  work) is a reference-free metric for novelty/diversity that faithfully
  reflects divergent creativity, validated against human annotations,
  LLM-based novelty judgments, and baseline diversity measures.
- Clustering by *meaning* before computing entropy is what makes it work:
  naive entropy over raw probabilities rewards surface-level rephrasings,
  while semantic entropy separates a model that rephrases from one that
  produces genuinely distinct ideas.
- The retrieval-based multi-agent judge gives context-sensitive task-
  fulfilment assessment with >60% efficiency improvement over the
  alternative.
- The framework recovers expected effects of model size, temperature,
  recency, and reasoning on creative performance.

## Methods

- Semantic clustering via an entailment model, then entropy over cluster
  probabilities; sampling-based, needs no reference text.
- Multi-agent retrieval judge for the convergent/appropriateness half.
- Three qualitatively distinct validation domains, chosen for spread rather
  than convenience — MacGyver in particular is a **physical
  problem-solving** benchmark, the closest of the three to this project.

## Results

- Headline for us: an off-the-shelf, published, code-released implementation
  of exactly the two-sided structure this project needs — a spread metric
  that is robust to paraphrase, plus a separate appropriateness judge.

## Critique / open questions

- Semantic entropy measures spread *within one model's samples for one
  prompt*. That is a good instrument for "did the intervention broaden this
  model's output distribution," but it is **not** the same as
  [[transfer-depth-ladder]], which asks a qualitative question (did a
  mechanism transfer, or only vocabulary?). Two outputs can be semantically
  distinct and both be vocabulary-level pseudo-transfer. Use it as a
  complementary diversity measure, not a replacement for the ladder.
- Depends on an entailment model for clustering; cluster granularity is a
  free parameter that will move the entropy number, and sensitivity to it is
  relegated to the appendix.
- Unusual author profile (lead authors from Raffles Institution, a secondary
  school, with NTU senior authorship). The venue is the real signal here.

## Trust signals

- **Credibility:** 4 — ACL 2026 main conference (competitive, peer
  reviewed), code publicly released, validation against human annotations
  across three distinct domains rather than one, and it builds on an
  established metric (Farquhar et al.'s semantic entropy, *Nature* 2024)
  rather than inventing one. Held at 4 pending independent replication —
  it is very recent and the framework is the authors' own proposal.

## Follow-up

- **Relevance: 4** — a strong candidate for the **diversity half** of this
  project's metric stack, and it pairs naturally with
  [[saakyan2026death]]'s warning: use semantic entropy (paraphrase-robust)
  rather than n-gram novelty (paraphrase-fooled) wherever a spread number is
  needed. **Action items:** (1) evaluate the released code against `xpol`
  outputs before building anything bespoke; (2) look at MacGyver as a
  possible ready-made source of STEM-ish problems for the dev problem set;
  (3) keep the ladder as the primary H2 outcome, with semantic entropy as a
  secondary, cheaper signal.
