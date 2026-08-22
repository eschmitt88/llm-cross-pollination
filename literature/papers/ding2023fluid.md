---
kind: paper
title: "Fluid Transformers and Creative Analogies: Exploring Large Language Models' Capacity for Augmenting Cross-Domain Analogical Creativity"
authors: ["Zijian Ding", "Arvind Srinivasan", "Stephen MacNeil", "Joel Chan"]
institutions: ["University of Maryland", "Temple University"]
year: 2023
venue: "Creativity and Cognition (C&C) 2023"
peer_reviewed: true
url: "https://arxiv.org/abs/2302.12832"
code_url: null
citations: null
source: "raw/papers/ding2023fluid.pdf"
added: "2026-08-22"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["abstract-then-reinstantiate", "analogical-distance", "transfer-depth-ladder"]
tags: ["q1-choosing", "q2-integrating", "prompt-strategy", "h3", "h4", "h6", "problem-decomposition"]
---

# Fluid Transformers and Creative Analogies

## TL;DR

The most directly on-target paper in this batch. Systematically tests
LLM-generated **cross-domain** analogies (not same-domain, unlike Yasunaga
et al.) for creative problem *reformulation*, across three studies:
prompt-engineering exploration (zero/one/few-shot), a helpfulness study
with real users doing problem reformulation, and a harm/bias audit. Key
prompt-design finding directly answers part of Q2: decomposing the source
problem into **stakeholder / context / goal / obstacle** before asking
for an analogy controls the near/far distance far better than asking the
model to build an abstract "schema" first — the opposite of what schema-
theoretic priors would predict.

## Claims

- One-shot prompting (a single worked example of a cross-domain analogy)
  beat both zero-shot and few-shot (3 examples) on judged potential
  usefulness *and* on semantic distance from the source problem — more
  examples did not monotonically help.
- Decomposing the problem into **stakeholder, context, goal, obstacle**
  and asking the model to vary stakeholder+context while holding
  goal+obstacle fixed gave *much* better distance/usefulness balance than
  an earlier design that asked the LLM to first generate an "abstracted
  schema" of the problem (i.e., abstraction-first hurt here, contrary to
  the TRIZ/abstract-then-reinstantiate intuition — a genuine tension
  worth testing directly in our bake-off).
- LLM-generated cross-domain analogies are usable: median helpfulness
  rating 4/5 in a real reformulation task, and analogies drove *observed*
  changes in problem framing ~80% of the time.
- There is a real harm/toxicity cost to unconstrained cross-domain
  generation that the project should track as a side metric: up to ~25%
  of outputs flagged potentially harmful by at least 2/5 raters, mostly
  "upsetting" content (not overtly biased/toxic) — an artifact of forcing
  analogies from arbitrary domains into sensitive real-world problems.

## Methods

Prompt structure (Section 3.1, directly reusable): source problem is
represented as four labeled slots — **Stakeholder / Context / Goal /
Obstacle** — e.g.
```
Stakeholder: people who stay at home for a long time
Context: international travel is restricted under the pandemic
Goal: find interesting places to visit, eat and have fun
```
The prompt asks GPT-3 (text-davinci-002, temperature=1, 400 tokens) to
generate an analogy that varies stakeholder+context (source of "distance")
while preserving goal+obstacle (source of relevance/usefulness) — an
explicit, deliberate distance-control knob baked into the prompt itself,
not left to sampling. Zero/one/few-shot variants tested with 3 hand-built
example problem→analogy pairs; 480 analogies generated across 6 design
problems (food insecurity, job security, entertainment, etc.).
Human rating: a blinded PhD rater judged (1) whether an analogical mapping
existed, (2) uniqueness vs. duplicate, (3) potential usefulness, plus
semantic similarity (SentenceTransformers) to the source problem as an
automatic distance proxy.
Study 1 (n≈?, real ideation task): participants received the
best-performing one-shot analogies and rated helpfulness 1–5, plus
open-ended coding of whether/how they changed their problem
reformulation.

## Results

- Table 1: one-shot ≈80% judged potentially useful, semantic similarity
  <0.5 to the source problem; zero-shot ≈40% useful, >0.7 similarity
  (collapses toward the source domain); few-shot ≈67% useful, similarity
  ≈0.3 (more distant, slightly less useful) — consistent with H3's "far
  but not too far" tradeoff, visible directly in their own data though
  they don't frame it that way. Best config: 70% of outputs both unique
  and judged potentially useful.
- Study 1: median helpfulness 4/5; 84.09% (185/220) of coded
  reformulation instances "added" new considerations from the analogy.
  No significant correlation between researchers' a priori usefulness
  judgment and participants' actual ratings (point-biserial ≈ -0.03,
  p=0.69) — expert pre-judging of analogy quality does not predict real
  usefulness, relevant to how much to trust an LLM judge vs. humans.
- Study 2: ~25% upper bound on potentially harmful outputs, majority
  "upsetting" rather than biased/toxic.

## Critique / open questions

Model is GPT-3/text-davinci-002 (2022, pre-RLHF-chat) — one-shot vs.
few-shot ordering may not transfer to modern models; authors themselves
say they're "not confident" it generalizes. Domain sampling is hand-picked,
not external/random — answers Q2, says nothing about Q1. The "abstracted
schema first" design that *underperformed* structured slots complicates
[[abstract-then-reinstantiate]]'s assumption that abstraction always
helps — may depend on *how* the abstraction is elicited.

## Trust signals

- **Credibility:** 4 — Maryland + Temple, peer-reviewed at C&C 2023,
  mixed rigorous quantitative + qualitative methods, transparent about a
  complicating finding. No code/data repository; single-model study.

## Follow-up

- **Relevance: 5** — Most directly answers Q2 with cross-domain (not
  same-domain) analogies; empirical ammunition for H3 (near/far tradeoff
  visible in their own data) and H6. Strongest actionable item: **test
  whether stakeholder/context/goal/obstacle decomposition beats a
  freeform abstraction step** inside [[abstract-then-reinstantiate]] —
  flagged there.
