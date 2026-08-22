---
kind: moc
name: "integrating the seed"
status: active
added: "2026-08-22"
concepts:
  - "[[concepts/structure-mapping]]"
  - "[[concepts/abstract-then-reinstantiate]]"
  - "[[concepts/seed-brief-isolation]]"
  - "[[concepts/analogical-prompting]]"
  - "[[concepts/conceptual-blending]]"
  - "[[concepts/foreign-seed]]"
  - "[[concepts/transfer-depth-ladder]]"
  - "[[concepts/novelty-usefulness-tradeoff]]"
sources:
  - "[[literature/papers/gentner1983structuremapping]]"
  - "[[literature/papers/jiang2024autotriz]]"
  - "[[literature/papers/ding2023fluid]]"
  - "[[literature/papers/yasunaga2023large]]"
  - "[[literature/papers/wang2021popblends]]"
  - "[[literature/papers/hope2017accelerating]]"
  - "[[literature/papers/zhang2025noveltybench]]"
  - "[[literature/papers/doshi2024generative]]"
tags: ["moc", "q2-integrating"]
---

# Integrating the seed

**Q2.** A correctly-sampled foreign seed still fails if the prompt
retrieves only the parts of it that already resemble the problem — the
output wears the seed's vocabulary with none of its mechanism. This is a
prompt-structure question, not a sampling one: the same seed, differently
integrated, ranges from decoration to a working method. This MoC organizes
the eight concepts around what makes integration deep, and how depth is
measured.

## Problem / theory: why naive injection produces decoration

- [[concepts/structure-mapping]] — Gentner's account of analogy: good
  transfer aligns *relations* (causal, higher-order), not surface
  attributes — the theoretical reason "incorporate ideas from X" fails.
  Its systematicity principle ([[literature/papers/gentner1983structuremapping]]:
  prefer mappings that carry a coherent relational system over isolated
  surface matches) underlies both the templates below and the rubric.
- [[concepts/foreign-seed]] is the shared input to every strategy here —
  granularity/distance are set by Q1 ([[mocs/choosing-the-seed]]); this
  MoC covers only what happens to it after the draw.

## Operational design: integration templates

- [[concepts/abstract-then-reinstantiate]] — the backbone candidate:
  restate the problem domain-neutrally (contradiction/invariant/traded
  resource), ask how the seed handles that abstract problem, map back with
  an explicit correspondence table, critique it for surface-only matches.
  TRIZ's core move, already built as **AutoTRIZ**
  ([[literature/papers/jiang2024autotriz]]: pinned to a fixed external
  knowledge base rather than LLM-recalled facts — a RAG-style grounding
  choice worth adopting; also an entropy-based randomness diagnostic).
  [[literature/papers/ding2023fluid]] complicates step 1: a freeform
  "abstracted schema" prompt underperformed a structured-slot
  decomposition — a variant worth testing in H2.
- [[concepts/seed-brief-isolation]] — generate the seed's mechanisms in a
  fresh context that hasn't seen the problem, then inject only the brief.
  Cheap with `claude -p` (two calls). Validated by PopBlends'
  divergent-then-convergent design ([[literature/papers/wang2021popblends]]:
  expand each domain independently before connecting), including its
  warning that an ungrounded expander confidently hallucinates attributes
  an entity can't have — a brief-writing failure mode to guard against.
- [[concepts/conceptual-blending]] — PopBlends' narrower two-*fixed*-domain
  version of the same shape; not directly usable but contributes two
  findings: an ensemble of expansion strategies beat picking one winner
  (candidate for H5), and unconstrained expansion hallucinates confidently
  under constraints it can't satisfy.
- [[concepts/analogical-prompting]] — same-domain sibling: self-generate
  K=3–5 distinct exemplars (optionally a "knowledge" abstraction first),
  then solve. Reuses inside "map back" and brief-writing: distinctness
  instructions prevent near-duplicate collapse, and abstracting before
  instances steered the model toward the true mechanism over surface-
  lexical false matches ([[literature/papers/yasunaga2023large]]); K=3–5
  is the numeric precedent for H5's "k ≥ 3" threshold.

## Evaluation: telling transfer from decoration

- [[concepts/transfer-depth-ladder]] — ordinal rubric (0 none / 1
  vocabulary / 2 metaphor / 3 mechanism / 4 method) operationalizing
  structure-mapping's relational-alignment criterion; levels 3–4 are the
  target and primary outcome for H2, H4, H6.
  [[literature/papers/hope2017accelerating]]'s three-part rater criteria
  (different mechanism / same purpose / feasible) precedes the rung-3/4
  boundary; [[literature/papers/zhang2025noveltybench]] validates judged
  scoring over raw embedding-distance (diverges from human "functionally
  distinct" judgment) and supplies a reusable `distinct_k`/`utility_k`
  pattern for combining rung with quality score.
- [[concepts/novelty-usefulness-tradeoff]] — the second axis every
  experiment must report: novelty-only metrics are maximized by nonsense,
  usefulness-only by the home-field answer the project escapes.
  [[literature/papers/doshi2024generative]]'s 6-item Likert instrument
  (novelty = novel/original/rare, usefulness = appropriate/feasible/
  publishable, α > 0.89) is directly adaptable; self-assessment proved
  unreliable — a caution against trusting the model's own rating.

## What's established so far

Nothing in Q2 tested yet — H1 closed Q1 (external randomness is
necessary) but says nothing about integration.
`experiments/2026-08-22-h2-integration-bakeoff/` is a scaffold (naive vs.
persona vs. abstract-then-reinstantiate, ± isolated brief, on the dev set)
not yet run.

## What's still open

- **H2 — bake-off.** Does abstract-then-reinstantiate beat naive
  injection and persona prompting on the ladder, same seeds? Next
  experiment per `docs/research-plan.md` phase 2.
- **H4 — granularity**, tested jointly with H2: field vs. subfield vs.
  named-method seeds.
- **H6 — isolation.** Problem-blind brief-writer context vs. single joint
  context, not run.
- **Ding et al.'s structured-slot variant** of the abstraction step —
  worth an explicit H2 arm rather than assuming freeform abstraction fine.
- **Judge calibration.** Both judges may inherit the homogenization bias
  they're grading — human calibration on a subset is required, not done.
