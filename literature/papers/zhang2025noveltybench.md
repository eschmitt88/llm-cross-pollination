---
kind: paper
title: "NoveltyBench: Evaluating Language Models for Humanlike Diversity"
authors: ["Yiming Zhang", "Harshita Diddee", "Susan Holm", "Hanchen Liu", "Xinyue Liu", "Vinay Samuel", "Barry Wang", "Daphne Ippolito"]
institutions: ["Carnegie Mellon University"]
year: 2025
venue: "COLM 2025"
peer_reviewed: true
url: "https://arxiv.org/abs/2504.05228"
code_url: "https://novelty-bench.github.io"
citations: null
source: "raw/papers/zhang2025noveltybench.pdf"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["novelty-usefulness-tradeoff", "transfer-depth-ladder", "homogenization"]
tags: ["evaluation", "metric", "benchmark", "h1", "h5", "mode-collapse"]
---

# NoveltyBench: Evaluating Language Models for Humanlike Diversity

## TL;DR

A ready-made, reusable **evaluation metric** for exactly the diversity
problem this project is built around. Defines `distinct_k` (the number
of *functionally distinct* equivalence classes among k independent
samples, via a fine-tuned classifier, not surface embedding distance) and
a patience-weighted `utility_k` that combines distinctness with per-sample
quality into a single number. Evaluates 20 frontier models and finds
severe mode collapse (most models produce <3 distinct answers in 10
tries), that *larger* models within a family are often *less* diverse
than smaller siblings, and — most directly useful for H1/H5 — that
prompting for creativity (system prompt, paraphrasing) barely helps,
while **in-context regeneration** (show the model its own prior outputs,
ask it to differ) closes most of the gap to human-level diversity.

## Claims

- Diversity should be measured as *functional* (would a user benefit
  from seeing the second output?) not lexical/surface — n-gram overlap,
  embedding distance, and BLEU/ROUGE/BERTScore all diverge from human
  judgment of "meaningfully different." This directly validates the
  project's [[transfer-depth-ladder]] design choice (an ordinal rubric of
  what actually transferred, not a distance score) over a pure embedding-
  distance diversity metric.
- Mode collapse gets *worse*, not better, with scale and alignment within
  a model family — "capability on standard benchmarks" does not predict
  "generative utility" when a user wants several distinct good answers.
  Directly relevant to model-choice decisions for both the ideator and
  judge roles in this project's pipeline.
- **"Be creative" prompting does not work.** System-prompt instruction
  ("You are a producer of unique answers...") and prompt paraphrasing
  only marginally improve diversity. This is direct, recent (2025),
  large-scale (20 models) empirical confirmation of this project's
  CLAUDE.md premise that "randomness is external to the LLM... never ask
  the model to 'pick a random field' except as the baseline being
  measured" — this paper is exactly that baseline, measured, and found
  wanting.
- **In-context regeneration** (ask for a different answer while keeping
  prior answers in context) is the most effective mitigation tested,
  bringing Claude 3 Opus, GPT-4o, and Gemini 2.0 Pro roughly to — in two
  cases above — human-writer diversity levels. This is a cheap,
  concrete technique the project's own multi-seed tournament (H5) or
  isolated-brief (H6) design should consider as a baseline/ingredient,
  distinct from external random seeding.

## Methods

- Two datasets: **NB-Curated** (hand-designed prompts across categories
  known to elicit multiple valid answers) and **NB-WildChat** (filtered
  real user queries from WildChat, deduplicated by IP, filtered by GPT-4o
  for prompts admitting multiple good answers, validated against 100
  human-labeled examples).
- **Functional equivalence classifier**: authors hand-annotated 1,100
  pairs of generations for "would a user benefit from seeing both,"
  fine-tuned a `deberta-v3-large` classifier on 1,000 pairs — held-out
  test accuracy 79%, F1 0.811 vs. human labels. New generations are
  greedily assigned to the first existing equivalence class the
  classifier judges them equivalent to, else start a new class.
- **`distinct_k`** = number of equivalence classes among k independent
  samples.
- **`utility_k`**: patience-weighted (geometric decay, patience p=0.8 in
  their setup) sum of *marginal* utility, where a generation's marginal
  utility is its quality score if it starts a new equivalence class, else
  zero (a repeat contributes nothing). Formula:
  `utility_k = (1-p)/(1-p^k) * Σ_i p^(i-1) · 1[c_i ≠ c_j ∀j<i] · u_i`.
  As patience→0 this degenerates to standard single-best-generation
  quality evaluation — a nice property for ablating "how much do you
  actually care about diversity" as a single dial.
- Per-generation quality via `Skywork-Reward-Gemma-2-27B-v0.2` (a
  RewardBench-leading reward model), calibrated to a 1–10 scale against
  GPT-4-judged MT-Bench scores.
- 20 frontier models evaluated with 10 independent samples each,
  temperature=1 (their stated best-case setting for diversity — most
  APIs default lower). Four diversity-elicitation strategies compared on
  a 100-prompt subset with Claude 3 Opus / GPT-4o / Gemini 2.0 Pro:
  resampling (baseline), paraphrasing the prompt, system-prompt
  instruction, in-context regeneration.
- Human baseline: 8 of the paper's own authors independently answered
  the curated prompts, establishing a "human diversity" reference line.

## Results

- Best frontier models still average fewer than 3 distinct responses out
  of 10 independent samples on curated prompts; several closed models
  (Claude 3, Gemini, GPT-4o) scored below 4/10 on `utility_k`.
- Smaller models (Gemma 2-2B, Llama 3.2-1B) show *higher* raw diversity
  than their larger siblings; as "patience" (weight on seeing more
  outputs) increases, larger models' utility degrades faster than
  smaller models' — single-best-generation benchmarks systematically
  mislead about which model is "better" for a diversity-seeking user.
- Diversity-elicitation comparison (100-prompt subset, 8 generations):
  paraphrasing and system-prompt are only marginally effective;
  in-context regeneration is clearly the strongest, bringing GPT-4o and
  Gemini 2.0 Pro to *match or exceed* the human-author utility baseline.

## Critique / open questions

The functional-equivalence classifier is trained on general/creative
prompts (jokes, recommendations, opinions) — transfer to judging whether
two STEM problem-solving outputs are "functionally distinct" is
untested; would need a validation pass on our own problem set before
reuse. `utility_k`'s patience parameter (p=0.8) lacks extensive
sensitivity analysis — worth an ablation before adopting. In-context
regeneration is evaluated only as "ask again in the same context," not
identical to this project's planned multi-seed tournament (independently,
externally seeded proposals then judged/merged) — whether *externally
seeded* diversity beats *self-directed* regeneration is precisely the
open question H1 vs. H5 should resolve.

## Trust signals

- **Credibility:** 5 — CMU, peer-reviewed at COLM 2025, large-scale
  (20 models), methodologically careful (classifier validated against
  human labels, calibrated reward model, human baseline), code and data
  publicly released.

## Follow-up

- **Relevance: 5** — `distinct_k` / `utility_k` are directly adoptable as
  the project's headline diversity+quality metric, likely stronger than
  the "pairwise embedding distance" plan in `docs/research-plan.md` per
  this paper's own critique of embedding/BLEU/ROUGE metrics, and
  validates the ladder-style (ordinal, judged) approach already chosen
  for [[transfer-depth-ladder]]. The in-context-regeneration finding is
  the strongest available baseline to beat: any external-seeding
  strategy (H1, H5) should be benchmarked against "ask the same model to
  differ from its own prior outputs" before claiming external randomness
  is necessary.
