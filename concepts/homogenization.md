---
kind: concept
name: "homogenization"
status: seedling
added: "2026-08-22"
sources: []
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

It is the problem statement. The empirical literature (Doshi & Hauser 2024;
Anderson, Shah & Kreminski 2024; Padmakumar & He 2024) establishes that it
is real and that "be more creative" prompting does not fix it. Two
consequences for the design: the model cannot be the source of its own
variety ([[external-randomness]]), and the evaluation has to measure
diversity *across* runs and seeds, not just quality within one.

## Connections

- Candidate literature in
  `raw/_candidates/2026-08-22-llm-homogenization-and-diversity-metrics.md`.
- The LLM judge used for scoring may share the bias it grades — calibrate
  against humans ([[novelty-usefulness-tradeoff]]).
