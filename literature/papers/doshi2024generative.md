---
kind: paper
title: "Generative AI enhances individual creativity but reduces the collective diversity of novel content"
authors: ["Anil R. Doshi", "Oliver P. Hauser"]
institutions: ["UCL School of Management", "University of Exeter"]
year: 2024
venue: "Science Advances 10, eadn5290"
peer_reviewed: true
url: "https://www.science.org/doi/10.1126/sciadv.adn5290"
code_url: "https://doi.org/10.5061/dryad.qfttdz0pm"
citations: null
source: "raw/papers/doshi2024generative.md"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["homogenization", "novelty-usefulness-tradeoff"]
tags: ["evidence", "homogenization", "causal", "evaluation"]
---

# Generative AI enhances individual creativity but reduces the collective diversity of novel content

## TL;DR

**Note on sourcing**: the publisher page (science.org) and the PMC PDF
viewer both blocked automated fetch (403 / proof-of-work JS challenge).
The full text below was obtained from Europe PMC's open-access REST API
(CC-BY, identical to the published version), not the publisher PDF, so
`status: read` reflects reading complete body text, just not the
typeset PDF. See `raw/papers/doshi2024generative.md` for provenance and
the full extracted text.

Preregistered, causal (randomized) two-phase online experiment: N=293
writers produce an 8-sentence short story, randomly assigned to
Human-only / Human+1 GPT-4 idea / Human+5 GPT-4 ideas; N=600 independent
evaluators rate all 293 stories blind to condition. GenAI access causally
*raises* both novelty and usefulness ratings (more so with 5 ideas than
1), with the largest gains for the *least* inherently creative writers
(measured via DAT). But GenAI-assisted stories are measurably *more
similar to each other* — the headline diversity-loss result — and are
directly anchored to the specific GenAI idea shown. Frames the whole
dynamic explicitly as a tragedy-of-the-commons: individually rational,
collectively erosive.

## Claims

- Access to GenAI ideas causally increases both novelty (+5.4%/+8.1% for
  1/5-idea conditions vs. no-AI) and usefulness (+3.7%/+9.0%) as rated by
  blind third-party evaluators — a genuine quality lift, not just a
  perception effect (writers' own self-ratings show no such difference,
  suggesting writers cannot accurately judge whether GenAI helped).
- The uplift is **not uniform**: it "equalizes" outcomes — high-DAT
  (inherently creative) writers see almost no benefit; low-DAT writers
  see the largest gains (novelty +10.7%, usefulness +11.5%, "well
  written" +26.6% in the five-idea condition). GenAI raises the floor,
  does not raise the ceiling.
- GenAI-assisted stories are measurably more similar to (a) each other
  within condition, and (b) the specific GenAI idea the writer was shown
  — both effects hold even though writers could not copy-paste the
  GenAI text (they had to re-type/paraphrase it), so the homogenization
  is not literal copying, it's anchoring on the idea's content/structure.
- Authors argue their design (single fixed uncustomized prompt per idea
  request, no multi-turn interaction, no prompt personalization) is
  likely a **lower bound** on both the creativity uplift and the
  homogenization risk — more interactive/customized GenAI use could
  push both effects further in either direction.

## Methods

Full instruction text to writers (topic-substituted, e.g. "open seas"):
> "We would like you to write a story about an adventure on the open
> seas. You can write about anything you like. The story must be exactly
> eight sentences long and it needs to be written in English and
> appropriate for a teenage and young adult audience (approximately 15
> to 24 years of age)."

GenAI idea-generation prompt passed to GPT-4 (topic-substituted):
> "Write a three-sentence summary of a story about an adventure on the
> open seas."

- Novelty index = mean(novel, original, rare); usefulness index =
  mean(appropriate, feasible, publishable); both 9-point Likert,
  Cronbach's α = 0.92 / 0.89 — a ready-made 6-item usefulness+novelty
  rubric this project could adapt (with STEM-appropriate substitutions)
  for the [[novelty-usefulness-tradeoff]] evaluation.
- Divergent Association Task (DAT; Olson et al. 2021) used as a
  trait-level creativity covariate — 10 maximally-different words, scored
  by cosine distance of word embeddings — worth considering as a
  covariate to control for participant/model baseline creativity in our
  own human-calibration subset.
- Diversity/similarity metric: OpenAI embeddings, cosine similarity ×100
  of each story to the mean embedding of all other stories in the same
  condition — directly the same "group-level" methodology as Anderson,
  Shah & Kreminski 2024, independently converged on.
- Preregistered at AsPredicted.org (ID 136723); ethics approval from
  both UCL and Exeter IRBs; full data + analysis code released via
  Dryad.

## Results

- Novelty: Human+1 idea +5.4% (b=0.207, P=0.021); Human+5 ideas +8.1%
  (b=0.311, P<0.001), all vs. Human-only baseline.
- Usefulness: Human+1 +3.7% (b=0.185, P=0.039); Human+5 +9.0%
  (b=0.453, P<0.001); +5.1% (P=0.0012) over Human+1.
- Story-to-group similarity: Human+1 b=0.871 (P<0.001), Human+5 b=0.718
  (P=0.003) — an increase equal to 10.7% / 8.9% of the entire
  Human-only-condition similarity range (8.10 points).
- Story-to-GenAI-idea similarity: +5.2% (b=4.29, P<0.001) and +5.0%
  (b=4.11, P<0.001) more similar to the shown idea than Human-only
  stories are to a randomly assigned idea from the same topic pool —
  direct evidence of anchoring, not just topical convergence.
- 88.4% of GenAI-condition participants used the tool at least once when
  offered (voluntary uptake is high, so intention-to-treat estimates are
  a conservative floor, per the authors).

## Critique / open questions

Single fixed low-effort prompt, no multi-turn interaction, no
customization — authors flag this as limiting generalizability; effects
may not transfer to a richer, iterative prompting setup (this project's
target use case) in either direction. Task is narrow (8-sentence
micro-fiction, three fixed topics) — external validity to STEM
problem-solving is untested. No comparison of *different* integration
strategies — measures the existence/scale of homogenization, not any
mitigation, same gap as Anderson et al. 2024.

## Trust signals

- **Credibility:** 5 — peer-reviewed at Science Advances, preregistered,
  two large independent samples (293 writers + 600 evaluators, 3,519
  evaluations), full data/code on Dryad, transparent about limitations
  and about a lower-bound framing of its own effect sizes.

## Follow-up

- **Relevance: 5** — Named explicitly in the research plan's H1 framing;
  anchors [[homogenization]] alongside Anderson, Shah & Kreminski 2024 —
  the two studies independently converge on the same group-level-
  collapse-without-individual-loss pattern via different tasks and
  different embedding models, strong triangulated evidence. "Equalizes
  low performers, doesn't raise the ceiling" is relevant to interpreting
  any future finding that our skill helps some problems more than
  others. The 9-point Likert novelty+usefulness index (α > 0.89) is a
  solid template for our own human-calibration rubric.
