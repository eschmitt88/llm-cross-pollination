---
kind: paper
title: "Deterministic or Probabilistic? The Psychology of LLMs as Random Number Generators"
authors: ["Javier Coronado-Blázquez"]
institutions: ["Telefónica Tech, AI & Data Unit"]
year: 2025
venue: "arXiv preprint"
peer_reviewed: unknown
url: "https://arxiv.org/abs/2502.19965"
code_url: null
citations: null
source: "raw/papers/coronadoblazquez2025deterministic.pdf"
added: "2026-08-22"
relevance: 4
credibility: 2
status: read
related_experiments: []
related_concepts: ["external-randomness"]
tags: ["h1", "llm-randomness", "prompt-language"]
---

# Deterministic or Probabilistic? The Psychology of LLMs as Random Number Generators

## TL;DR

LLMs asked to output a single "random" number are close to deterministic:
they collapse onto one or two favorite values, the favorite depends on the
model *and* on the prompt's language, and formal uniformity tests reject the
null overwhelmingly. Chain-of-thought inspection (DeepSeek-R1) shows the
model reasoning about *how a human would pick a random number* (digits of
π, current date/time, "gut instinct") rather than sampling from its own
output distribution.

## Claims

- For a 1-5 range, models settle on a single dominant value and largely
  ignore the extremes (e.g. one model answers "3" in Spanish but "4" in
  English for the same request, essentially every time).
- Uniformity is formally rejected: lowest p-value reported is 2.19e-15
  (Llama 3.1-8B, T=0.1, Spanish) — far below any reasonable significance
  threshold.
- Prompt *language* is an independent axis of bias, not just model choice —
  the same model, same temperature, different language, gives a
  meaningfully different "random" distribution.
- DeepSeek-R1's exposed CoT reveals human-mimicking heuristics standing in
  for genuine randomness: ~10% invoke digits of π, ~30% invoke
  current date/time, ~60% invoke a Python `randint` call it can't actually
  execute, ~60% appeal to "instinct" — i.e. the model retrieves *descriptions
  of how humans randomize*, not a random draw.

## Methods

- Cross-model, cross-language (7 languages), cross-temperature comparison
  of "give me a random number in [range]" outputs; goodness-of-fit testing
  against uniform; qualitative CoT trace analysis for DeepSeek-R1.

## Results

- Confirms and extends the "LLMs are bad dice players" finding
  ([[zhao2026large]] equivalent, if that note exists) with a second,
  independent methodology and explicit attention to prompt language — a
  variable this project's sampler prompts will also vary across strategies.
- The CoT trace analysis is the most useful thing here for us: it's direct
  evidence that when a model is asked to "be random" it retrieves and
  narrates *cultural scripts about randomness* rather than executing one.
  That is exactly the mechanism [[homogenization]] predicts for "pick a
  random field" too — expect the same kind of retrieved-script behavior,
  not just skew, when we run H1.

## Critique / open questions

- Single author, industry (not academic) lab, no released code — the
  headline finding (skew) replicates and is consistent with other
  independent-randomness literature, but the CoT-heuristics taxonomy is a
  single small qualitative pass on one model and should be treated as
  suggestive, not definitive.
- Numeric-range randomness is a much simpler task than "name a field from a
  4,500-leaf taxonomy" — the *direction* of the finding should transfer to
  H1, the magnitude should not be assumed to.

## Trust signals

- **Credibility:** 2 — single independent author at a corporate AI lab
  (Telefónica Tech), CC-BY preprint, no peer-reviewed venue found, no code
  released, no citation record yet. The result itself is unsurprising given
  convergent findings elsewhere, which raises confidence in the direction
  even though the source alone is weak.

## Follow-up

- **Relevance: 4** — strengthens [[external-randomness]] with a second,
  independent replication of "LLM randomness is not uniform," plus the
  prompt-language axis (worth controlling for in our own sampler prompts)
  and the CoT-heuristics mechanism, which is a plausible *causal* story for
  why H1 will show skew, not just a second measurement of the skew itself.
