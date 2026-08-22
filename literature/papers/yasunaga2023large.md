---
kind: paper
title: "Large Language Models as Analogical Reasoners"
authors: ["Michihiro Yasunaga", "Xinyun Chen", "Yujia Li", "Panupong Pasupat", "Jure Leskovec", "Percy Liang", "Ed H. Chi", "Denny Zhou"]
institutions: ["Google DeepMind", "Stanford University"]
year: 2023
venue: "ICLR 2024"
peer_reviewed: true
url: "https://arxiv.org/abs/2310.01714"
code_url: null
citations: 173
source: "raw/papers/yasunaga2023large.pdf"
added: "2026-08-22"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: ["abstract-then-reinstantiate", "seed-brief-isolation", "structure-mapping"]
tags: ["q2-integrating", "prompt-strategy", "h2", "h5", "self-generation"]
---

# Large Language Models as Analogical Reasoners

## TL;DR

Introduces "analogical prompting": instead of retrieving or hand-labeling
few-shot exemplars, prompt the LLM to *self-generate* K=3–5 relevant-but-
distinct exemplar problems (and optionally a "tutorial" of core concepts)
in the same pass, then solve the target problem using its own generated
context. Beats 0-shot CoT and hand-labeled few-shot CoT on GSM8K, MATH,
Codeforces, and BIG-Bench, average +4% accuracy. All within-domain (math
recalls math, code recalls code) — not cross-domain transfer — but the
self-generation mechanic and its failure taxonomy are directly reusable.

## Claims

- Self-generated exemplars, tailored per-problem, beat both generic 0-shot
  CoT ("think step by step") and fixed hand-labeled few-shot CoT.
- Generating high-level "knowledge" (a tutorial of core concepts) *before*
  exemplars outperforms generating it after — the model identifies the
  abstract concept first, which then steers exemplar generation toward
  the concept rather than surface-lexical similarity (their example: with
  knowledge-first, exemplars converge on the "prefix product algorithm";
  without it, LLMs latch onto "palindromic sequences" — a surface-lexical
  false match).
- Self-generation beats retrieval from a labeled dataset once the base LLM
  is large enough (text-davinci-002/003); smaller models do better with
  retrieved exemplars, because self-generation "fails to produce useful or
  valid exemplars" when the LLM hasn't learned the relevant material.

## Methods

Core prompt (single pass, no separate calls):
```
# Problem: [x]
# Relevant problems: Recall three relevant and distinct problems. For each
problem, describe it and explain the solution.
# Solve the initial problem:
```
Key technical decisions, directly transferable to seed-brief generation:
- Explicitly instruct "generate problems that are **distinct from each
  other**" — without this, LLMs repetitively generate near-duplicate
  exemplars.
- K = 3 to 5 self-generated exemplars is the sweet spot (Table 5: K=1
  underperforms via over-reliance on a single exemplar; K=3 or 5 is best;
  diminishing/flat returns beyond that on GSM8K/MATH). Directly informs H5
  (multi-seed, k≥3).
- Single-pass generation (exemplars + solution in one prompt) performs
  comparably to independently sampling exemplars and re-prompting, but is
  simpler — no separate calls needed.
- Knowledge-before-exemplars ordering: `# Tutorial: Identify core concepts
  in the problem and provide a tutorial.` placed before the exemplar
  instruction.

## Results

- Average +4% accuracy over 0-shot/few-shot CoT baselines across GSM8K,
  MATH, Codeforces, BIG-Bench, GPT-3.5/GPT-4/PaLM2.
- Scale-dependent: analogical prompting only overtakes few-shot CoT once
  the base model is strong enough (text-davinci-002+); on weaker models
  (curie, davinci-001) hand-labeled few-shot still wins.

## Critique / open questions

Qualitative failure analysis on 50 correct + 50 incorrect solves
(GSM8K+MATH), reusable as a judge-rubric template: of 50 *incorrect*
solves, 28/50 had relevant+correct exemplars but the LLM still failed —
12/50 "generalization gap" (new problem harder than exemplars), 8/50
"overreliance on specific exemplars", 8/50 other/calculation errors. Note
this is same-domain analogy (math recalls math), not cross-domain seed
injection — it answers "how to structure self-generation" (Q2) but is
silent on choosing a *foreign* topic (Q1).

## Trust signals

- **Credibility:** 5 — Google DeepMind + Stanford, peer-reviewed at ICLR
  2024, 173 citations (Semantic Scholar, checked 2026-08-22).

## Follow-up

- **Relevance: 4** — Strongest evidence for the mechanics inside
  [[abstract-then-reinstantiate]]: self-generate before solving, force
  distinctness, generate abstraction before instances. The "distinct
  exemplars" instruction and K=3–5 finding should be baked directly into
  the sampler/integrator design (H5); the failure taxonomy is a starting
  point for refining the transfer-depth-ladder judge rubric.
