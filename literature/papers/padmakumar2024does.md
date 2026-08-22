---
kind: paper
title: "Does Writing with Language Models Reduce Content Diversity?"
authors: ["Vishakh Padmakumar", "He He"]
institutions: ["New York University"]
year: 2024
venue: "ICLR 2024"
peer_reviewed: true
url: "https://arxiv.org/abs/2309.05196"
code_url: "https://github.com/vishakhpk/hui-diversity"
citations: null
source: "raw/papers/padmakumar2024does.pdf"
added: "2026-08-22"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: ["homogenization"]
tags: ["homogenization", "rlhf", "co-writing", "diversity-metrics"]
---

# Does Writing with Language Models Reduce Content Diversity?

## TL;DR

A controlled three-arm co-writing experiment (solo / base GPT-3 /
feedback-tuned InstructGPT) on argumentative essays. Only the
*feedback-tuned* model reduces diversity — and the reduction is traceable
to the text the model itself contributed, not to any change in how humans
write when assisted. This is the cleanest causal isolation of
*instruction-tuning* (rather than "LLMs" generally) as the mechanism behind
[[homogenization]].

## Claims

- Co-writing with InstructGPT produces a statistically significant
  reduction in content diversity; co-writing with base GPT-3 does **not**
  differ significantly from the solo control.
- The effect shows up on both axes measured: *homogenization* (essays by
  different authors become more similar to each other) and *diversity*
  (lower lexical and content diversity across the essay set).
- Decomposing essays into human-contributed vs. model-contributed spans,
  the homogenization is attributable to the model's key points. The
  user-contributed text is essentially unaffected by the collaboration.
- Framing conclusion: the generation-quality gains from RLHF/feedback
  tuning may come at the direct cost of more homogeneous content.

## Methods

- Controlled user study, three setups, argumentative essay task.
- A purpose-built battery of diversity metrics separating the
  homogenization question ("do different authors converge?") from the
  set-diversity question ("is the corpus lexically/semantically narrower?").
- Attribution analysis: match model-contributed text to summarized key
  points per essay, then re-measure homogenization with those points
  isolated — this is what licenses the causal claim about *which* text
  drives the effect.

## Results

- Headline for us: base vs. instruction-tuned is the discriminating
  variable. Homogenization is not an inevitable property of "using a
  language model"; it is a property of the *aligned* model's output
  distribution.

## Critique / open questions

- Argumentative essays, not STEM problem-solving — the transfer to this
  project's task domain is an assumption, not a demonstrated result.
- The study measures diversity of *prose*, whereas this project cares about
  diversity of *mechanisms/approaches*. Lexical diversity metrics would
  likely miss a case where two solutions use identical vocabulary but
  different underlying methods, which is precisely the distinction
  [[transfer-depth-ladder]] is built to capture. Do not reuse these metrics
  uncritically as the H2 outcome measure.
- GPT-3 / InstructGPT era. Whether the base-vs-tuned gap has the same shape
  in current frontier models is untested here, though
  [[wenger2025different]] and [[patel2026similarly]] suggest the aligned-model
  convergence has, if anything, grown.

## Trust signals

- **Credibility:** 5 — ICLR 2024 (peer-reviewed, competitive venue), NYU,
  code released, controlled experiment with a genuine control arm and a
  mechanism-isolating attribution analysis rather than a correlational
  observation.

## Follow-up

- **Relevance: 4** — this is the strongest *causal* anchor available for
  [[homogenization]], and its base-vs-tuned contrast supplies the mechanistic
  story that [[zhang2025verbalized]] later formalizes as typicality bias.
  Directly supports the project's motivation. Not load-bearing for the
  sampler (Q1) — its value is in the problem statement and in warning
  against naive lexical diversity metrics for H2's judge.
