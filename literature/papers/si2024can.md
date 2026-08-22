---
kind: paper
title: "Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers"
authors: ["Chenglei Si", "Diyi Yang", "Tatsunori Hashimoto"]
institutions: ["Stanford University"]
year: 2024
venue: "ICLR 2025"
peer_reviewed: true
url: "https://arxiv.org/abs/2409.04109"
code_url: "https://github.com/NoviScl/AI-Researcher"
citations: null
source: "raw/papers/si2024can.pdf"
added: "2026-08-22"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: ["novelty-usefulness-tradeoff", "homogenization"]
tags: ["human-eval", "research-ideation", "novelty-feasibility", "eval-design"]
---

# Can LLMs Generate Novel Research Ideas?

## TL;DR

The methodological gold standard for this whole area: 100+ expert NLP
researchers write novel ideas and blind-review both human and LLM ideas,
with confounders controlled. LLM ideas are judged **more novel** (p < 0.05)
than expert human ideas but **slightly weaker on feasibility**. Two
secondary findings matter more for this project than the headline: LLM
self-evaluation fails, and LLM ideation **lacks diversity**.

## Claims

- First statistically significant head-to-head result: LLM-generated ideas
  are rated more novel than expert-written ideas (p < 0.05), with a small
  feasibility penalty.
- **LLM self-evaluation fails** — models are unreliable judges of their own
  ideas, which is a direct warning about cheap LLM-judge eval loops.
- **Lack of diversity in generation** is identified as an open problem: the
  ideation agent produces a narrow spread, so scaling generation does not
  scale idea variety.
- The authors flag that human novelty judgements are themselves hard and
  noisy even among experts, and propose an end-to-end follow-up where
  researchers actually *execute* the ideas, to test whether novelty and
  feasibility ratings predict real research outcomes.

## Methods

- Recruited 100+ NLP researchers; controlled for confounders (topic
  matching, style normalisation, review assignment); blind review of
  human-written vs LLM-generated ideas.
- Careful attention to the statistics of noisy expert judgement — the
  paper's real contribution is arguably the experimental design, not the
  result.

## Results

- The novelty-up / feasibility-down shape is exactly the
  [[novelty-usefulness-tradeoff]] this project committed to measuring
  jointly, observed here at expert-review scale.

## Critique / open questions

- Idea *generation*, not problem *solving* — the output is a research
  proposal, not a worked solution, so transfer depth is not assessed.
- Novelty ratings come from a single blind read; the authors themselves note
  expert disagreement, which caps the achievable effect resolution.
- The agent baseline is one particular RAG-style ideation pipeline; "LLMs
  are more novel than humans" is really "this pipeline was."

## Trust signals

- **Credibility:** 5 — Stanford (Yang, Hashimoto), ICLR 2025, an unusually
  expensive and well-controlled human study (100+ domain experts, blind
  review, pre-specified analysis), code released, and the authors
  foreground their own result's limitations rather than overselling.

## Follow-up

- **Relevance: 4** — supplies the evaluation bar and two concrete design
  constraints. **Action items:** (1) the self-evaluation failure argues
  against letting the generating model judge H2 outputs — use a different
  family and keep the human spot-check (this converges with
  [[saakyan2026death]]'s judge guidance from a different direction); (2)
  their novelty/feasibility rubric is a ready-made template for the
  usefulness half of the project's metric; (3) the diversity gap they
  identify is the opening this project's [[foreign-seed]] intervention is
  meant to fill — cite it as the motivating negative capability.
