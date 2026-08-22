---
kind: paper
title: "Diverse AI Personas Can Mitigate the Homogenization Effect in Human-AI Collaborative Ideation"
authors: ["Yun Wan", "Yoram M. Kalman"]
institutions: ["University of Houston - Downtown", "The Open University of Israel"]
year: 2026
venue: "Computers in Human Behavior: Artificial Humans"
peer_reviewed: true
url: "https://arxiv.org/abs/2504.13868"
code_url: null
citations: null
source: "raw/papers/wan2026diverse.pdf"
added: "2026-08-22"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["homogenization", "foreign-seed", "novelty-usefulness-tradeoff"]
tags: ["persona-prompting", "homogenization", "h2-baseline", "replication"]
---

# Diverse AI Personas Can Mitigate the Homogenization Effect

## TL;DR

A direct extension of [[doshi2024generative]]'s story-writing experiment
that flips its conclusion's scope. Doshi & Hauser gave every writer plots
from a *uniformly* prompted model and found convergence. Here, plots are
generated through 10 deliberately varied GenAI personas first; with that
change, collective story diversity is preserved relative to a human-only
baseline. The creativity-diversity trade-off is therefore an artifact of
**uniform deployment practice**, not an inherent property of GenAI.

## Claims

- Phase 1: structured prompting with 10 diverse personas produced 300 story
  plots whose diversity was confirmed by text-embedding analysis — i.e. the
  perturbation demonstrably moved the *input* distribution.
- Phase 2: participants writing with access to those diverse plots produced
  stories that preserved diversity versus a human-only baseline, with some
  evidence of *enhancement* in the 1-plot condition.
- Therefore the trade-off "emerges from uniform deployment practices rather
  than from an inherent limitation of GenAI."
- Design implication the authors draw: treat GenAI as a *configurable
  partner*, not a static tool; prompt variation is a first-class design
  lever and over-standardization is a risk.

## Methods

- Two-phase replication-and-extension of Doshi & Hauser's design, preserving
  their task (short story writing) and their outcome construct (collective
  diversity via semantic similarity) while intervening on plot generation.
- Embedding-based diversity checks at both the stimulus level (Phase 1) and
  the output level (Phase 2), which is the right structure — it separates
  "did the intervention change the seeds" from "did changed seeds change the
  outputs."

## Results

- Headline for us: an input-side perturbation, applied *before* the human
  ever sees the model, is sufficient to defeat measured homogenization. That
  is structurally the same claim this project makes for [[foreign-seed]]
  injection, with personas standing in for foreign disciplines.

## Critique / open questions

- Personas are a *weaker and less principled* perturbation than an external
  random topic draw: the 10 personas were themselves author-chosen, so the
  diversity ceiling is set by human curation and the procedure is not
  reproducible or scalable in the way [[sampling-frame]] + [[external-randomness]]
  is. It also inherits the LLM's own persona priors.
- "Some evidence of enhancement in the 1-plot condition" is hedged language;
  the enhancement claim is weaker than the preservation claim.
- Story writing, not STEM problem-solving. Diversity of *plots* is measured,
  not depth of mechanism transfer — nothing here speaks to
  [[transfer-depth-ladder]].
- Effect sizes and the exact statistical tests are not extractable from the
  abstract-level read done here; a deep-read is warranted before this is used
  to power H2.

## Trust signals

- **Credibility:** 4 — peer-reviewed and forthcoming in *Computers in Human
  Behavior: Artificial Humans*, a direct and honest extension of a
  high-profile prior result (which is the most useful kind of replication),
  with two-phase validation. Docked one for no released code/data and hedged
  effect language.

## Follow-up

- **Relevance: 4** — this is the closest published relative of the project's
  core intervention and therefore the natural **baseline arm for H2**: does
  a principled foreign-discipline seed beat persona variation at equal cost?
  It also strengthens the project's premise by showing the input-side lever
  works at all. Pair with the multi-persona design-science study
  ([[feng2025enhancing]]) which compares persona *strategies* rather than
  persona-vs-nothing.
