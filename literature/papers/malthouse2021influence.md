---
kind: paper
title: "The influence of exposure to randomness on lateral thinking in divergent, convergent, and creative search"
authors: ["Eugene Malthouse", "Yuanjing Liang", "Serena Russell", "Thomas T. Hills"]
institutions: ["University of Warwick"]
year: 2021
venue: "Cognition 218, 104937"
peer_reviewed: true
url: "https://doi.org/10.1016/j.cognition.2021.104937"
code_url: null
citations: 5
source: "raw/papers/malthouse2021influence.pdf"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["external-randomness", "foreign-seed", "analogical-distance", "structure-mapping"]
tags: ["null-result", "disconfirming", "oblique-strategies", "wikipedia-random", "h3", "preregistered"]
---

# The influence of exposure to randomness on lateral thinking

## ⚠️ This is a NULL RESULT and it cuts against the project's naive premise

The `/discover` triage summarised this paper as a "direct empirical test of
'random foreign stimulus improves problem solving'" — which is true, but it
omitted the direction. **The test failed.** Read this note before citing
the paper.

## TL;DR

A pre-registered study gave 592 British participants random Wikipedia
articles (the Oblique-Strategies premise, operationalised exactly as this
project's most naive baseline would) while they worked one convergent
forecasting task and two divergent fluency tasks. There was **no
improvement, and often significant impairment**. A Bayesian meta-analysis
returns strong support for the null. The authors conclude that lateral
thinking via random stimuli is "non-trivial and may require such stimuli to
be sufficiently task-related or 'optimally random'."

## Claims

- No positive effect of random-stimulus exposure on any of the three tasks;
  several comparisons show significant *impairment*.
- Bayes factors favour the null throughout: BF10 = 0.24 (Study 1), 0.82
  (Study 2 fluency), 0.53 (Study 2 judge-scored creativity), 0.29 (Study 2
  SemDis-scored creativity), 0.47 (Study 3 fluency), 0.51 (Study 3
  judge-scored), 0.43 (Study 3 SemDis-scored). Study 1's data were ~4.3x
  more likely under the null.
- The Bayesian meta-analysis across all three studies provides "compelling
  evidence in favor of the null hypothesis."
- Authors' interpretation: raw randomness is not enough; stimuli likely need
  to be *task-related* or "optimally random" to help.

## Methods

- Pre-registered; 592 participants; random stimulus = Wikipedia's random
  page generator; three tasks (1 convergent forecasting, 2 divergent
  fluency). Creativity scored three ways (fluency counts, human judges, and
  SemDis semantic-distance scoring) — the multi-measure design is what makes
  the null credible rather than an artifact of one metric.
- Bayesian ANCOVAs (JASP) per study plus a Bayesian meta-analysis.
- Study 3 was constrained to one-third of the intended sample size.

## Results

- The headline for us is negative and it is the most important negative
  result in the corpus so far.

## Critique / open questions

- **Scope of the disconfirmation.** This tests *unassisted humans* given a
  *raw, unprocessed, uniformly random* stimulus with *no integration step*.
  That is precisely the naive intervention, and precisely **not** what this
  project proposes. The project's design already contains the two things the
  authors say are missing: distance control ([[analogical-distance]], H3 —
  their "optimally random") and a structured integration procedure
  ([[structure-mapping]], [[abstract-then-reinstantiate]], H2). So the paper
  is better read as *motivating the project's design choices* than as
  refuting its premise.
- But it is genuinely disconfirming for one live hypothesis: that a foreign
  seed helps *by itself*, through mere juxtaposition. It does not, in humans.
  The burden of proof now sits on the integration step.
- Fluency/forecasting tasks are far from STEM problem-solving, and humans
  are not LLMs — an LLM may exploit a random seed differently than a person
  with limited working memory. Untested either way.
- Only 5 citations; the null-result literature is chronically under-cited,
  which is not itself evidence against it.

## Trust signals

- **Credibility:** 5 — pre-registered, n = 592, three tasks, three
  independent scoring methods, Bayesian analysis reported with per-study
  Bayes factors and a meta-analysis, published in *Cognition* (a top venue,
  which is notable for a null result). Senior author Thomas Hills is an
  established researcher in search/foraging models of cognition. Full text
  read from the Warwick WRAP open-access copy.

## Follow-up

- **Relevance: 5** — load-bearing, and the single best argument in the
  literature for why this project must be about *integration*, not merely
  *injection*. **Action items:** (1) cite it explicitly in
  `docs/research-plan.md` as the disconfirming prior for the naive arm; (2)
  make the "raw seed, no integration" condition an actual **control arm** in
  H2 — this paper predicts it will not beat baseline, and if our version
  does beat baseline, that difference is the finding; (3) treat "optimally
  random" as an independent restatement of H3's useful-distance band, from
  a human-subjects direction. Do not let the project's framing assume
  random stimuli help; the honest prior is that they don't, unassisted.
