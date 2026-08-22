---
kind: paper
title: "Homogenization Effects of Large Language Models on Human Creative Ideation"
authors: ["Barrett R. Anderson", "Jash Hemant Shah", "Max Kreminski"]
institutions: ["Independent Researcher", "Santa Clara University"]
year: 2024
venue: "Creativity and Cognition (C&C) 2024"
peer_reviewed: true
url: "https://arxiv.org/abs/2402.01536"
code_url: null
citations: null
source: "raw/papers/anderson2024homogenization.pdf"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["homogenization", "novelty-usefulness-tradeoff"]
tags: ["evidence", "homogenization", "evaluation", "embedding-similarity"]
---

# Homogenization Effects of Large Language Models on Human Creative Ideation

## TL;DR

The canonical controlled-experiment evidence for [[homogenization]]:
36-participant within-subjects study comparing ChatGPT vs. a non-AI
creativity support tool (the Oblique Strategies card deck) on four
divergent-ideation tasks (subset of the Torrance Tests of Creative
Thinking). Finds ChatGPT users produce ideas that are **more homogeneous
at the group level** (higher similarity to the average embedding of *all*
participants' ideas) but **not more homogeneous at the individual level**
— i.e. each ChatGPT user still explores a wide personal range, but
different users' ranges collapse onto each other. This individual-vs-group
distinction is the paper's central methodological contribution and should
directly shape this project's diversity metrics.

## Claims

- Group-level homogenization is real and measurable via sentence-
  embedding cosine similarity to the group-average embedding; individual-
  level diversity is *not* reduced — the ceiling on any one user's
  creativity is unaffected, but the *union* across users shrinks.
  This is the single most important methodological point for this
  project: diversity must be measured **across independent runs/users**,
  not just within one transcript, or the effect is invisible.
- ChatGPT users generate more ideas, more elaborated ideas (longer,
  higher stoplisted-word-count), and cover more idea *categories* than
  Oblique-Strategies users — i.e. GenAI raises fluency/elaboration/
  flexibility even while collapsing group-level originality. This
  mirrors Doshi & Hauser's "professionalizes but homogenizes" finding
  from an independent lab and method.
- ChatGPT users assign themselves markedly less ownership/responsibility
  for their own ideas (48.17% self-attributed vs. 63.63% for the
  non-AI tool, p=0.003) — a side effect worth tracking if the project's
  eventual skill gets used interactively (attribution/trust risk).
- "Ask the model to be creative" is not evaluated here directly, but the
  paper's broader argument (echoed by NoveltyBench, Doshi & Hauser) is
  that homogenization is a property of the *tool*, not fixable by
  prompting alone.

## Methods

- 36 participants, within-subjects: 4 TTCT-style divergent-ideation
  prompts, 2 with ChatGPT, 2 with the Oblique Strategies deck
  (order/assignment counterbalanced). 1,271 total ideas collected.
- **Group-level homogenization metric**: for each idea, cosine similarity
  between its sentence embedding and the *mean embedding of all
  participants' ideas for that task*. Lower mean similarity = more
  divergent = less homogenized.
- **Individual-level metric**: same computation but against the mean
  embedding of *that one participant's own* other ideas for the task —
  isolates whether a person's personal range narrowed, independent of
  whether it converged with others.
- Embedding model: `all-MiniLM-L6-v2` (SentenceTransformers), explicitly
  validated against human similarity judgments in an appendix (Table 2)
  before being trusted as the metric — a methodological step worth
  replicating for our own transfer-depth / diversity judge calibration.
- Other TTCT facets measured computationally: fluency (raw idea count),
  flexibility (human-coded idea categories, 181 categories from 1,271
  ideas), elaboration (stoplisted word count), originality/uniqueness
  (count of ideas no other participant also produced, plus a 5%-threshold
  variant and a frequency-weighted variant — all three converge on the
  same null result for uniqueness).

## Results

- **Group-level**: ChatGPT ideas M=.24 similarity (more homogeneous,
  i.e. closer to the group mean) vs. Oblique Strategies M=.28,
  t(32)=2.154, p=0.038, d=.47 (medium effect).
- **Individual-level**: no difference, ChatGPT M=.65 vs. OS M=.66,
  t(32)=.944, p=0.352, d=.12 (negligible) — confirms the effect is purely
  a between-person collapse, not a within-person one.
- Fluency: +15% more ideas with ChatGPT (8.39 vs 7.32, p=0.044, d=.32).
- Flexibility: +27% more idea *categories* hit with ChatGPT (8.58 vs
  6.77, p=0.001, d=.54).
- Elaboration: ChatGPT ideas had higher stoplisted word count (8.25 vs
  6.46, d=.48) though the reported p-value (0.237) appears inconsistent
  with the t-statistic in the source table — read the original if this
  number is load-bearing for a citation.
- Uniqueness/originality: **no significant difference** by any of three
  measures (raw uniqueness, 5%-threshold, frequency-weighted) — ChatGPT
  did not measurably reduce *individual* idea uniqueness, consistent with
  the group-vs-individual split above.
- Self-attributed responsibility: 48.17% (ChatGPT) vs. 63.63% (OS),
  t(32)=3.21, p=0.003, d=.67 (largest effect size in the paper).

## Critique / open questions

Single LLM (ChatGPT) vs. a *non-AI* comparison (physical cards) rather
than another ideation-support method — doesn't isolate whether
homogenization is intrinsic to LLMs specifically or to any centralized
idea source. No mitigation tested (higher temperature, external
seeding, tournament) — pure diagnosis, exactly the gap H1–H6 fill.
Embedding similarity validated against human judgment only on this
paper's own creative-writing dataset — validity for STEM outputs
(this project's domain) is untested.

## Trust signals

- **Credibility:** 5 — peer-reviewed at C&C 2024, TTCT-grounded task
  design, embedding model explicitly validated against human judgment in
  an appendix, transparent reporting including a null result that
  complicates rather than confirms the headline finding.

## Follow-up

- **Relevance: 5** — Canonical anchor citation for [[homogenization]].
  The individual-vs-group distinction is the single most important
  methodological takeaway for this project's evaluation design: diversity
  metrics must be computed at the *group* level (across independent runs
  of the pipeline), not within one transcript, or the effect is invisible
  — exactly as demonstrated here.
