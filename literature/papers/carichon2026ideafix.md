---
kind: paper
title: "IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs"
authors: ["Florian Carichon", "Soumya Sharma", "Meaghan Girard", "Golnoosh Farnadi", "Romain Rampa"]
institutions: ["McGill University", "Mila — Quebec AI Institute", "Concordia University"]
year: 2026
venue: "arXiv preprint"
peer_reviewed: false
url: "https://arxiv.org/abs/2606.00875"
code_url: null
citations: null
source: "raw/papers/carichon2026ideafix.pdf"
added: "2026-08-22"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["homogenization", "seed-brief-isolation", "novelty-usefulness-tradeoff"]
tags: ["defixation", "eval-framework", "prompting-strategy", "h2", "fixation"]
---

# IDEAFix

## TL;DR

The closest published work to this project's exact framing. *Fixation* —
an LLM defaulting to the most obvious approach — is named as the failure
mode, and IDEAFix is a controlled evaluation framework for **defixation
prompting**: generate multiple original solutions to controlled variations
of short design scenarios, systematically varying task formulation,
attribute selection, and defixation strategy. Two results matter: simple
prompting strategies *do* boost originality, **and** output homogenization
persists across models regardless.

## Claims

- Existing creativity evaluations are either too narrow/decontextualized to
  capture goal-oriented generation, or too broad and confound task
  formulation with prompting with evaluation design. IDEAFix separates
  these factors by construction.
- **Task formulation and attribute selection significantly affect
  performance** — i.e. how the problem is posed is a first-order variable,
  not a nuisance parameter.
- Simple prompting strategies can boost the originality of solutions.
- **Persistent output homogenization remains across models**, confirming an
  inherent limit that prompting alone does not remove.

## Methods

- Controlled variations of short design scenarios; models prompted for
  multiple original solutions; factorial manipulation of scenario, task
  attributes, and defixation prompting strategy; extensible framework
  design intended for reuse.

## Results

- The two-sided result is the valuable part: prompting helps *and* is not
  sufficient. That is a more honest position than most of this literature.

## Critique / open questions

- Preprint, no peer-review signal, no released code found — the main
  credibility limit given that the contribution is a *framework* whose value
  depends on being reusable.
- "Simple prompting strategies boost originality" is not decomposed in the
  abstract into which strategies and by how much; the actionable detail
  requires a deep-read.
- Short design scenarios rather than STEM problems; originality is scored,
  but nothing here measures whether a *mechanism* transferred.
- Defixation via prompting is a different lever from injecting an external
  foreign seed — the framework is more directly reusable than the technique.

## Trust signals

- **Credibility:** 3 — credible group (McGill / Mila / Concordia; Farnadi is
  established in responsible-AI and evaluation), and the framing is
  unusually well-matched to a real gap. Held at 3 because it is an
  unreviewed preprint proposing its own evaluation framework with no
  released artifacts, which is exactly the situation where independent
  replication matters most.

## Follow-up

- **Relevance: 4** — most valuable as **evaluation-design prior art** rather
  than as a technique. It names this project's target failure mode
  (fixation) and provides a factorial structure that separates task
  formulation from prompting strategy from scoring — a decomposition the H2
  bake-off should copy, since H2 otherwise risks confounding "which
  integration strategy" with "which problem." **Action items:** (1) mirror
  its factor separation in the H2 design; (2) treat its persistent-
  homogenization finding as the prior that prompt-only interventions
  plateau — which is the argument for an *external* seed source; (3)
  re-check for a peer-reviewed version and released code before depending
  on it.
