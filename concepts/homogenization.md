---
kind: concept
name: "homogenization"
status: growing
added: "2026-08-22"
sources: ["anderson2024homogenization", "doshi2024generative", "zhang2025noveltybench"]
related_concepts: ["external-randomness", "foreign-seed", "novelty-usefulness-tradeoff"]
related_experiments: []
tags: ["problem", "evidence"]
---

# Homogenization

## Definition

The tendency of LLM outputs — and of humans working with them — to converge
on a narrow set of ideas: higher individual quality, lower collective
diversity. Mode-seeking in the output distribution, amplified by
post-training.

## Why it matters here

It is the problem statement. The empirical literature — **Doshi & Hauser
2024** (Science Advances, causal RCT on 293 writers + 600 evaluators: GenAI
access raises novelty/usefulness ratings +5–9% but makes stories more
similar to each other and to the shown idea) and **Anderson, Shah &
Kreminski 2024** (36-participant study, ChatGPT vs. Oblique Strategies
deck) — establishes that homogenization is real, causal (not just
correlational), and that "be more creative" prompting does not fix it.
**NoveltyBench** (Zhang et al. 2025) extends this to raw model sampling
(no human in the loop at all): 20 frontier models average under 3 distinct
outputs in 10 independent samples, larger models are often *less* diverse
than smaller siblings within a family, and system-prompt/paraphrase
attempts to elicit diversity are only marginally effective — the most
effective mitigation they found, in-context regeneration (show the model
its own prior outputs, ask it to differ), is a *within-model* strategy
distinct from this project's *external*-seeding approach and is the
baseline our sampler needs to beat.

Anderson et al.'s key methodological finding shapes this project's
evaluation design directly: homogenization is a **group-level** effect
(different users'/runs' outputs converge on each other) that is *not*
visible as **individual-level** diversity loss (d=.47 for group-level
similarity vs. d=.12, n.s., for individual-level) — so diversity must be
measured across independent runs/seeds of the pipeline, not within one
transcript, or the effect this project targets is invisible to the metric.

Two consequences for the design: the model cannot be the source of its own
variety ([[external-randomness]]), and the evaluation has to measure
diversity *across* runs and seeds, not just quality within one.

## Connections

- Full literature notes: `literature/papers/anderson2024homogenization.md`,
  `literature/papers/doshi2024generative.md`,
  `literature/papers/zhang2025noveltybench.md`.
- The LLM judge used for scoring may share the bias it grades — calibrate
  against humans ([[novelty-usefulness-tradeoff]]).
