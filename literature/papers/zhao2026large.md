---
kind: paper
title: "Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions"
authors: ["Minda Zhao", "Yilun Du", "Mengyu Wang"]
institutions: ["Harvard University"]
year: 2026
venue: "arXiv preprint"
peer_reviewed: unknown
url: "https://arxiv.org/abs/2601.05414"
code_url: "https://github.com/Mininda/LLM_Bad_Dice_Player"
citations: null
source: "raw/papers/zhao2026large.pdf"
added: "2026-08-22"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: ["external-randomness"]
tags: ["h1", "llm-randomness", "sampling-fidelity"]
---

# Large Language Models Are Bad Dice Players

## TL;DR

First large-scale, statistically powered audit of native LLM probabilistic
sampling: 11 frontier models across 15 target distributions, under both
batch (N=1000 in one response) and independent (N=1000 stateless calls)
generation. Verdict: LLMs do not have a functional internal sampler, and the
failure gets sharply worse the more the target distribution departs from a
trivial case and the longer the sampling horizon.

## Claims

- Batch generation of "random" numbers passes goodness-of-fit tests only
  7% of the time (median pass rate across models/distributions).
- Independent, stateless requests collapse almost completely: 10 of 11
  models pass **zero** of the 15 target distributions.
- Fidelity degrades monotonically with distributional complexity and with
  sampling horizon N — the problem is not just "hard for N=1", it compounds.
- The failure propagates into applied tasks: MCQ generation fails to keep
  answer position uniform across A/B/C/D (e.g. GPT-4o: 12.6% / 46.8% / 35.1%
  / 5.5% against a 25%-each target, χ²=444.5, p<.001), and demographic
  attribute generation for image prompts systematically misses target
  proportions (GPT-4o: 33.5% Asian vs. a stated target, 0% Hispanic vs. a
  stated 20% target).

## Methods

- Dual-protocol design (Batch vs. Independent Requests) to separate
  "can't sample" from "can't maintain state across calls" as failure modes.
- KS test (continuous, two-sample), chi-square goodness-of-fit (discrete),
  and Wasserstein-1 distance as fidelity metrics, α=0.01.
- 15 target distributions in 3 complexity tiers (Tier I: Uniform, Gaussian;
  harder tiers add structure).

## Results

- Directly quantifies the thing H1 needs a number for: asking a model to
  emit a value "uniformly" is not close to uniform, and the gap widens with
  distribution complexity and with how many draws you ask for at once.
- The MCQ and demographic-attribute experiments are a template for our own
  H1 measurement: don't just ask for a field name, measure the realized
  distribution against the stated target with a formal test, and report
  effect size (χ², W1), not just "it's skewed."

## Critique / open questions

- Distributions tested are numeric (Gaussian, uniform-over-integers, etc.),
  not categorical-over-a-taxonomy like our sampling frame — the numeric
  finding is suggestive, not a direct transfer, but the MCQ position-bias
  result *is* categorical and directly analogous to "pick uniformly among
  these labeled options."
- Single-lab (Harvard), preprint as of ingest; code released but no
  independent replication yet.

## Trust signals

- **Credibility:** 3 — reputable single institution (Harvard), code and
  data released on GitHub, large-scale statistically powered design (11
  models × 15 distributions), but not yet peer-reviewed and no external
  citation record at time of ingest.

## Follow-up

- **Relevance: 5** — this is close to canonical evidence for H1
  ([[external-randomness]]): it directly measures LLM sampling fidelity
  against a stated uniform target and reports the effect size (χ², p-value)
  our own H1 write-up should match in rigor. The MCQ-position experiment is
  a ready-made template for a categorical "pick uniformly among N labeled
  options" pilot before we build the full sampling-frame harness.
