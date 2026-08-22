---
kind: paper
title: "SciMON: Scientific Inspiration Machines Optimized for Novelty"
authors: ["Qingyun Wang", "Doug Downey", "Heng Ji", "Tom Hope"]
institutions: ["UIUC", "Allen Institute for AI", "Hebrew University of Jerusalem"]
year: 2024
venue: "ACL 2024"
peer_reviewed: true
url: "https://arxiv.org/abs/2305.14259"
code_url: "https://github.com/EagleW/CLBD"
citations: null
source: "raw/papers/wang2024scimon.pdf"
added: "2026-08-22"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: ["foreign-seed", "novelty-usefulness-tradeoff", "analogical-distance"]
tags: ["retrieval", "inspiration", "novelty-optimization", "h2", "architecture"]
---

# SciMON

## TL;DR

Reframes literature-based discovery away from binary link prediction:
models take *background context* (problems, experimental settings, goals)
and emit natural-language ideas grounded in literature. Two mechanisms
matter for us — retrieval of **"inspirations"** from past papers (the
foreign-seed analogue), and an **explicit iterative novelty loop** that
compares each candidate idea against prior work and revises until
sufficiently novel. Notably, GPT-4 alone produces ideas of low technical
depth and novelty; SciMON only *partially* mitigates this.

## Claims

- Natural-language idea generation grounded in retrieved literature is a
  strictly more expressive setting than binary link prediction, which had
  dominated literature-based discovery.
- Explicitly optimizing for novelty — iteratively comparing to prior papers
  and updating — measurably raises novelty over not doing so.
- **GPT-4 tends to generate ideas with low technical depth and novelty**;
  the framework partially mitigates but does not solve this. The authors
  frame the work as "a first step," which is unusually candid.
- Retrieved "inspirations" are the operative input: idea quality tracks what
  gets retrieved.

## Methods

- Retrieval over a scientific-literature knowledge graph to surface
  inspirations for a given background context; generation conditioned on
  those; then an iterative novelty-check-and-revise loop against prior work.
- Comprehensive evaluation across the generation setting, including
  comparison to strong LLM baselines.

## Results

- Headline for us: the **retrieve → inject → iterate** loop is a validated
  architecture, and the novelty gain is attributable to the explicit
  comparison step, not to the raw retrieval.

## Critique / open questions

- Inspirations are retrieved by *relevance* to the background context, which
  systematically biases toward **near** analogies — the opposite of this
  project's deliberate far-seed sampling. SciMON asks "what related work
  should inform this?"; `xpol` asks "what unrelated field should perturb
  this?" The architecture transfers; the retrieval objective does not.
- The novelty loop optimizes a *measured* novelty signal, which invites the
  gameability failure [[saakyan2026death]] documents — novel-scoring text
  that experts would not call creative. Whether SciMON's gains survive
  expert close-reading is untested.
- "Partially mitigates" is doing real work in the abstract; the residual gap
  is not quantified in a way that is easy to act on.

## Trust signals

- **Credibility:** 5 — ACL 2024, strong authorship (Heng Ji at UIUC; Doug
  Downey at AI2; Tom Hope, who also co-authored [[hope2017accelerating]] and
  SOLVENT, bridging the pre-LLM analogy-mining line into the LLM era), code
  and resources released, and honest negative reporting about GPT-4's
  baseline weakness.

## Follow-up

- **Relevance: 4** — the clearest published instance of the Q2 integration
  architecture this project needs, and a useful contrast on the Q1 side.
  **Action items:** (1) adopt the iterate-against-prior-work loop as a
  candidate H2 arm; (2) treat SciMON's relevance-based retrieval as the
  *near-seed* pole for H3's distance sweep — it is a real, published system
  sitting at one end of the band; (3) note the shared authorship lineage
  with [[hope2017accelerating]] when writing the related-work section.
