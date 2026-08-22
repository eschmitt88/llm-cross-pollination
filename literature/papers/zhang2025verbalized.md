---
kind: paper
title: "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity"
authors: ["Jiayi Zhang", "Simon Yu", "Derek Chong", "Anthony Sicilia", "Michael R. Tomz", "Christopher D. Manning", "Weiyan Shi"]
institutions: ["Northeastern University", "Stanford University", "West Virginia University"]
year: 2025
venue: "ICML 2026 (PMLR 306)"
peer_reviewed: true
url: "https://arxiv.org/abs/2510.01171"
code_url: "https://github.com/CHATS-lab/verbalized-sampling"
citations: null
source: "raw/papers/zhang2025verbalized.pdf"
added: "2026-08-22"
relevance: 3
credibility: 5
status: read
related_experiments: []
related_concepts: ["external-randomness"]
tags: ["mode-collapse", "prompting-technique", "diversity"]
---

# Verbalized Sampling

## TL;DR

Post-training alignment (RLHF) causes mode collapse because preference
annotators have a *typicality bias* — they systematically rate familiar,
predictable text as better — so even a perfect reward model trained on that
data would learn to prefer the mode. The fix is inference-time, not
training-time: instead of asking for one instance ("tell me a joke about
coffee"), ask the model to verbalize a distribution over several responses
with probabilities ("generate 5 jokes about coffee and their probabilities")
and sample from that. This alone recovers much of the pretraining-time
diversity that alignment suppressed, with no fine-tuning.

## Claims

- Typicality bias in preference data is formalized and verified empirically
  as the data-level driver of mode collapse (not just algorithmic/optimizer
  causes, the standard story in prior work).
- Verbalized Sampling (VS) increases diversity 1.6-2.1x over direct
  prompting on creative-writing tasks (poems, stories, jokes), without
  sacrificing measured quality, safety, or factual accuracy.
- More capable models benefit *more* from VS — an emergent trend, not a
  workaround for weak models.
- VS is training-free, model-agnostic (works via prompting alone on
  GPT/Claude/Gemini/Llama), and orthogonal to temperature.

## Methods

- Analytical model of how typicality-weighted preference data shifts the
  post-training modal response; empirical verification on real preference
  datasets.
- Semantic diversity score (embedding-based) + ROUGE-L (lower = more
  diverse) + a quality score, benchmarked across direct prompting,
  temperature scaling, and VS on poem/story/joke generation and dialogue
  simulation.

## Results

- The headline number for us: 1.6-2.1x diversity gain from a pure prompting
  change, no training, no external randomness source.

## Critique / open questions

- This is *model-internal* diversity — the opposite premise from this
  project's `external-randomness` stance (never ask the model to pick).
  It's relevant less as a technique for *choosing the seed* and more as a
  candidate technique for the *integrator* side (Q2): if we ever want the
  model to generate several candidate mappings/interpretations of a fixed
  foreign seed and pick the best, VS-style "verbalize k candidates with
  weights" is a stronger elicitation method than naive "be creative," and
  a plausible mechanism inside the multi-seed tournament (H5).
- Does not address whether VS-elicited diversity is *uniform* over any
  external reference distribution — it increases spread relative to direct
  prompting, which is a different claim than "matches a target
  distribution" (the claim [[zhao2026large]] and
  [[coronadoblazquez2025deterministic]] show LLMs fail at).

## Trust signals

- **Credibility:** 5 — Stanford (incl. Christopher Manning) + Northeastern
  co-authorship, accepted at ICML 2026, code and data released, model-
  agnostic empirical validation across multiple frontier models.

## Follow-up

- **Relevance: 3** — doesn't anchor [[external-randomness]] (it's a
  model-internal diversity technique, not evidence about sampling
  fidelity), but it's a concrete, well-evidenced prompting primitive worth
  testing as one of the Q2 integrator strategies (multi-candidate
  elicitation for [[foreign-seed]] mapping, H5's tournament arm) and as a
  possible ablation baseline: does VS-style elicitation for "name k diverse
  fields" get any closer to uniform than naive single-shot asking, before
  we conclude external RNG is strictly required?
