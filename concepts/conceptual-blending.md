---
kind: concept
name: "conceptual blending"
status: seedling
added: "2026-08-22"
sources: ["wang2021popblends", "fauconnier1998conceptual"]
related_concepts: ["seed-brief-isolation", "abstract-then-reinstantiate", "foreign-seed"]
related_experiments: []
tags: ["q2-integrating", "prompt-strategy"]
---

# Conceptual blending

## Definition

A two-stage divergent/convergent pipeline (PopBlends, Wang et al. 2023)
for combining two *fixed* domains (e.g. a pop-culture franchise and a
product) into a shared creative artifact: (1) expand each domain
independently into associations — entities, attributes, scenes — via a
mix of knowledge extraction and LLM querying; (2) find the
highest-matching connection between the two expansions, then repeat the
divergent/convergent cycle one level deeper (scenes rather than words) to
produce a concrete blend.

## Why it matters here

Narrower than this project's goal — PopBlends blends two *given* domains
rather than transferring a *mechanism* from a randomly sampled foreign
domain into an unrelated STEM problem — but the pipeline shape (expand
each side independently, then connect) is structurally the same move
[[seed-brief-isolation]] and step 2 of [[abstract-then-reinstantiate]]
rely on: generate the seed domain's structure *before* — and somewhat
independently of — the connection step, so the expansion isn't
pre-collapsed toward the target.

Two transferable findings:

- **Ensemble over pick-one.** Three expansion strategies (pure knowledge
  extraction, hybrid knowledge-base + LLM, pure LLM) were found equally
  *accurate* but with different characteristics, and the authors argue
  for using all three rather than choosing a winner — a candidate design
  input for the multi-seed tournament (H5): different integration
  strategies may be complementary rather than substitutable.
- **Unconstrained LLM expansion hallucinates confidently.** Queried for
  attributes of an entity that structurally can't have them, GPT-3
  fabricated plausible-sounding but false answers rather than declining —
  a concrete failure mode to guard against when a brief-writer is asked
  to expand a foreign domain it may only shallowly know.

## Connections

- Structurally parallel to [[seed-brief-isolation]]'s "generate the
  brief blind to the problem" move, in a narrower two-fixed-domains
  setting.
- The ensemble finding is a candidate ingredient for [[abstract-then-reinstantiate]]'s
  eventual multi-seed tournament design (H5).
