---
kind: concept
name: "abstract then reinstantiate"
status: growing
added: "2026-08-22"
sources: ["jiang2024autotriz", "ding2023fluid", "yasunaga2023large", "chan2018solvent", "fauconnier1998conceptual"]
related_concepts: ["structure-mapping", "foreign-seed", "seed-brief-isolation", "transfer-depth-ladder", "analogical-prompting", "conceptual-blending"]
related_experiments: []
tags: ["q2-integrating", "prompt-strategy", "h2"]
---

# Abstract then reinstantiate

## Definition

A three-step integration template: (1) restate the problem in
domain-neutral terms — the contradiction, the invariant, the resource being
traded off; (2) ask how the seed domain handles *that abstract problem*;
(3) map the seed's mechanism back onto the concrete problem with an explicit
correspondence table, then critique the table for surface-only matches.

## Why it matters here

This is TRIZ's core move (specific problem → generic problem → generic
solution → specific solution) and the direct operationalisation of
[[structure-mapping]]. Hypothesis H2 says it beats naive injection and
persona prompting on the [[transfer-depth-ladder]] with the same seeds. If
H2 holds it becomes the backbone of the packaged skill.

**AutoTRIZ** (Jiang et al. 2024) is this exact pipeline already built and
partially validated for engineering design: four LLM/lookup modules
implementing specific→general→general→specific, with the "general" layer
pinned to a *fixed external* knowledge base (39 engineering parameters,
the 39×39 contradiction matrix, 40 inventive principles) rather than
LLM-recalled knowledge — a RAG-style external-grounding choice worth
adopting directly. It also contributes a reusable **randomness
diagnostic**: run the "abstract" step 100 times on the same input and
compute the information entropy of the resulting distribution over
identified contradictions, useful for our own H1 measurement.

Complication from **Fluid Transformers** (Ding et al. 2023): in their
prompt-engineering exploration, an earlier design that asked the LLM to
first generate a free-form "abstracted schema" of the problem
*underperformed* a more structured decomposition (stakeholder / context /
goal / obstacle slots) at controlling distance and usefulness. This does
not refute the abstract-then-reinstantiate move itself, but suggests the
abstraction step needs *structured slots*, not a freeform schema prompt —
worth testing as a variant in the H2 bake-off.

**Yasunaga et al. 2023** (analogical prompting, same-domain not
cross-domain) supplies mechanics reusable inside the "map back" step:
explicitly instruct the model to generate *distinct* exemplars/mappings
(else it repeats near-duplicates), and generate the abstract "knowledge"
*before* instances/exemplars — ordering knowledge-first steered the model
toward the true mechanism rather than surface-lexical false matches in
their qualitative examples (see [[analogical-prompting]]).

## Connections

- Step 2 is where [[seed-brief-isolation]] plugs in: the seed's mechanisms
  can be retrieved in a context that has not seen the problem.
- The correspondence-table critique is a built-in guard against
  rung-1/rung-2 outputs.
- [[analogical-prompting]] is the same-domain (not cross-domain) cousin of
  this technique — self-generate before solving, but without a foreign
  seed; its self-generation mechanics (distinctness instruction,
  knowledge-before-exemplars ordering, K=3–5) transfer directly.
- [[conceptual-blending]] (PopBlends) is a structurally similar
  divergent-expand-then-convergent-connect pipeline for a narrower task
  (blend two fixed domains rather than transfer a mechanism into one).
