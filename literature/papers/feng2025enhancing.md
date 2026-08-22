---
kind: paper
title: "Enhancing design concept diversity: multi-persona prompting strategies for large language models"
authors: ["Wangchuan Bradley Feng", "Sébastien Hélie", "Jitesh H. Panchal"]
institutions: ["Purdue University"]
year: 2025
venue: "Design Science 11, e10037"
peer_reviewed: true
url: "https://doi.org/10.1017/dsj.2025.10037"
code_url: null
citations: null
source: "raw/papers/feng2025enhancing.pdf"
added: "2026-08-22"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["seed-brief-isolation", "foreign-seed", "homogenization"]
tags: ["persona-prompting", "h6", "h2-baseline", "design-concepts", "prompt-architecture"]
---

# Enhancing design concept diversity: multi-persona prompting strategies

## TL;DR

Compares three *architectures* for injecting multiple professional personas
into LLM design-concept generation, holding the personas constant:
**parallel** (one prompt per persona), **collective** (all personas in a
single prompt), and **sequential** (a chain of prompts, each persona
generating and updating). Parallel and sequential produce more diverse
concepts; collective — cramming every persona into one context — does not.
The prompt *architecture*, not the persona content, is what moves diversity.

## Claims

- LLMs provide more diverse design concepts under **parallel** prompting
  (multiple prompts, each with one professional persona) and under
  **sequential** prompting (a chain that generates and progressively
  updates), relative to the collective single-prompt strategy.
- Personas are backed by constructed professional knowledge bases rather
  than bare role labels, so the manipulation is a knowledge injection and
  not only a stylistic instruction.
- Builds on the authors' own earlier finding that a single professional
  persona already increases design-concept diversity (Feng, Hélie &
  Panchal 2024).

## Methods

- Formal setup: construct professional knowledge bases, select design
  problems, select personas, then generate concepts under each of the three
  prompting strategies and measure concept diversity.
- Crucially the persona *set* is held fixed across conditions, so the
  comparison isolates architecture from content.

## Results

- Headline for us: **isolation beats sharing a context.** One prompt holding
  all the perspectives underperforms N separate prompts each holding one.

## Critique / open questions

- Design-concept generation, not STEM problem-solving; concepts are scored
  for diversity, not for whether a mechanism genuinely transferred
  ([[transfer-depth-ladder]] would ask a different question).
- Personas are occupations ("act as a biologist"), which is a much weaker
  and more surface-level foreign signal than a specific foreign *mechanism*
  or *method* — the granularity distinction H4 is built to test.
- Diversity metric details and effect sizes were not extracted in this pass;
  a deep-read is needed before using it to power an H6 comparison.
- No released code or data found.

## Trust signals

- **Credibility:** 4 — peer-reviewed in *Design Science* (Cambridge, open
  access, CC-BY), an established engineering-design group at Purdue
  (Panchal is well known in design methodology), and a clean factorial
  comparison that isolates the variable of interest. Docked one for no
  released artifacts and unextracted effect sizes.

## Follow-up

- **Relevance: 4** — the most direct external evidence for **H6** found so
  far, arriving from an unexpected direction. H6 predicts that generating a
  foreign-domain brief in a *separate* context and then injecting it beats
  asking one context to do both; this paper reports the analogous result for
  personas (parallel/sequential > collective) and supplies independent
  support for [[seed-brief-isolation]]. **Action items:** (1) cite as prior
  art for H6 rather than treating H6 as untested; (2) reuse the three-way
  architecture taxonomy (parallel / collective / sequential) as the arm
  structure for the H6 experiment — it is a cleaner decomposition than a
  binary isolated-vs-joint split; (3) pair with [[wan2026diverse]] as the two
  persona-based baselines for the H2 bake-off.
