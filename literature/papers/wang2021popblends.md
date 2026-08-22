---
kind: paper
title: "PopBlends: Strategies for Conceptual Blending with Large Language Models"
authors: ["Sitong Wang", "Savvas Petridis", "Taeahn Kwon", "Xiaojuan Ma", "Lydia B. Chilton"]
institutions: ["Columbia University", "Hong Kong University of Science and Technology"]
year: 2021
venue: "CHI 2023"
peer_reviewed: true
url: "https://arxiv.org/abs/2111.04920"
code_url: null
citations: null
source: "raw/papers/wang2021popblends.pdf"
added: "2026-08-22"
relevance: 3
credibility: 4
status: read
related_experiments: []
related_concepts: ["seed-brief-isolation", "abstract-then-reinstantiate"]
tags: ["q2-integrating", "conceptual-blending", "hallucination", "ensemble"]
---

# PopBlends: Strategies for Conceptual Blending with Large Language Models

## TL;DR

Automates *conceptual blending* between two fixed domains (a pop-culture
franchise + a product) by expanding each domain divergently into
associations, then convergently finding a connecting concept, then
repeating divergent/convergent for scenes to actually blend. Compares
three pipelines — **No-GPT** (pure knowledge extraction from Wikipedia
plot text), **Half-GPT** (knowledge-base entities + GPT-3 for
attributes), **Full-GPT** (GPT-3 for everything) — and finds all three
about equally *accurate* but with different, complementary
*characteristics*, arguing for using them as an ensemble rather than
picking one winner. A user study shows the system more than doubles the
rate of successful blend ideation and roughly halves self-reported
mental demand.

## Claims

- Knowledge bases (accurate, narrow) and LLMs (broad, occasionally
  hallucinated) are complementary rather than substitutable — the
  Half-GPT hybrid (structured entity list from Wikipedia + GPT-3 for
  free-associated attributes) captures information neither source alone
  provides.
- The three pipelines were "equally accurate but with very different
  characteristics" — i.e. accuracy alone is not sufficient to rank
  strategies; qualitative fit to the task matters, and an ensemble beats
  any single method.
- LLMs (GPT-3, pre-RLHF-alignment/InstructGPT era) essentially never say
  "I don't know" and will confidently hallucinate attributes for entities
  that structurally cannot have them (their example: asked for
  catchphrases of Dementors — a mute Harry Potter creature — GPT-3
  invented plausible-sounding but false ones). This is a concrete,
  reusable failure mode name for our failure-mode taxonomy.

## Methods

Two-stage divergent/convergent pipeline (structurally close to a
domain-brief + connect approach, relevant to [[seed-brief-isolation]]):

- **Stage 1** (find a connecting concept between the two input domains):
  - *No-GPT*: rank Wikipedia plot sentences of the pop-culture domain by
    semantic similarity to the product's embedding; extract the single
    most-relevant word per top sentence as the connecting concept.
  - *Half-GPT*: extract named entities (people/orgs/locations/objects)
    from Wikipedia via NER, then query GPT-3 per entity with the prompt
    `"What five {activities/adjectives/catchphrases} do you associate
    with {entity name} in {pop culture domain}?"`, producing 600
    attributes per domain (4 entity types × 10 entities × 3 attribute
    types × 5 items); rank attributes by semantic match to the product.
  - *Full-GPT*: ask GPT-3 directly which entity it associates with the
    product and why (no knowledge-base scaffolding at all).
- **Stage 2**: repeat divergent/convergent to find matching *scenes*
  (rather than words) from both domains around the connecting concept,
  for visual blending.
- Technical evaluation: 10 annotators rated accuracy of Stage 1/2 outputs
  per pipeline (Figures 7–8, "average accuracy" and "at least one of
  five accurate").
- User study: 10 amateur designers, within-subjects, 6 blend tasks each
  (3 with PopBlends, 3 with a plain internet-search baseline), NASA-TLX
  administered after each condition.

## Results

- Ideation rate: **2.03 ideas per pop-culture/product pair with
  PopBlends vs. 0.87 with the search-engine baseline** (paired Wilcoxon,
  p < 0.001) — roughly 2.3x.
- NASA-TLX mental demand: **2.85 (PopBlends) vs. 5.80 (baseline)**, p =
  0.004 (Bonferroni-corrected); Effort 3.05 vs 5.00 (p=0.006); Frustration
  1.65 vs 3.25 (p=0.026); Performance (self-rated) 2.10 vs 3.60 (p=0.004,
  lower=better on this scale).
- All 10/10 participants preferred PopBlends over the search baseline.
- The three Stage-1 pipelines were reported as roughly equally accurate
  in the technical evaluation but each surfaced a different flavor of
  connection (No-GPT: precise plot-grounded but sometimes zero relevant
  hits; Half-GPT/Full-GPT: broader coverage but sometimes hallucinated).

## Critique / open questions

Domain is narrow and closed (5 fixed pop-culture franchises), not an open
"sample any foreign field" setting — the transfer target (blend a product
with a franchise) is closer to marketing creativity than STEM
problem-solving, so the *task* generalizes only partially. Still, the
divergent-expand-then-convergent-connect shape is directly analogous to
[[abstract-then-reinstantiate]]'s "expand the seed, then map back" move.
No calibration/refusal mechanism for the hallucination problem — flagged
as a genuine unsolved limitation, not addressed.

## Trust signals

- **Credibility:** 4 — Columbia + HKUST, peer-reviewed at CHI 2023, solid
  mixed technical + user-study evaluation with significance testing, but
  modest sample sizes (10 annotators, 10 study participants); no public
  code repository found.

## Follow-up

- **Relevance: 3** — Doesn't seed a load-bearing concept on its own
  (blending two *fixed* domains is narrower than sampling a random
  foreign domain), but strengthens [[seed-brief-isolation]] as prior art
  for "divergent-expand, then convergent-connect," and its "ensemble the
  strategies rather than pick one" finding is a candidate input for the
  multi-seed tournament (H5). The hallucination failure mode is worth
  folding into the transfer-depth-ladder judge's rubric as a red flag.
