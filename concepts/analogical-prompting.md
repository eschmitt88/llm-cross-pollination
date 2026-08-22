---
kind: concept
name: "analogical prompting"
status: seedling
added: "2026-08-22"
sources: ["yasunaga2023large"]
related_concepts: ["abstract-then-reinstantiate", "seed-brief-isolation", "transfer-depth-ladder", "structure-mapping"]
related_experiments: []
tags: ["q2-integrating", "prompt-strategy", "self-generation"]
---

# Analogical prompting

## Definition

A prompting technique (Yasunaga et al. 2023) where the LLM is asked to
self-generate K=3–5 relevant, mutually distinct exemplar problems (and
optionally a "knowledge" tutorial of core concepts, generated *before* the
exemplars) in the same context, then solve the target problem using its
own generated material — in place of either a generic "think step by
step" instruction or hand-labeled/retrieved few-shot exemplars. Core
prompt shape: `# Problem: [x] / # Relevant problems: Recall three
relevant and distinct problems... / # Solve the initial problem:`.

## Why it matters here

This is the **same-domain** sibling of
[[abstract-then-reinstantiate]] — self-generation instead of retrieval,
but the exemplars come from the same field as the problem, not a foreign
one. Its mechanics transfer directly to seed-brief generation and to the
"map back" step of abstract-then-reinstantiate:

- Explicitly instructing the model to generate *distinct* material
  prevents near-duplicate collapse — a concrete, testable technique for
  H1/H5's diversity goals, independent of external randomness.
- Generating the abstraction ("knowledge"/core concepts) *before*
  instances steers the model toward the true underlying mechanism rather
  than surface-lexical false matches (their example: knowledge-first
  finds the "prefix product algorithm"; without it, the model latches
  onto superficial "palindromic sequences").
- K=3 to 5 self-generated items is empirically the sweet spot — direct
  numeric support for H5's "k ≥ 3" multi-seed threshold.

## Connections

- Plugs into the "map back" step of [[abstract-then-reinstantiate]] and
  into brief-writing for [[seed-brief-isolation]].
- Its qualitative failure taxonomy (generalization gap / overreliance on
  a specific exemplar / irrelevant exemplar) is a candidate input to
  refining the [[transfer-depth-ladder]] judge rubric.
- Does not itself test cross-domain transfer — it is evidence for *how*
  to structure self-generation, not evidence for *whether* a foreign
  seed transfers.
