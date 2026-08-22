---
kind: concept
name: "seed brief isolation"
status: growing
added: "2026-08-22"
sources: ["wang2021popblends", "carichon2026ideafix", "feng2025enhancing"]
related_concepts: ["abstract-then-reinstantiate", "foreign-seed", "homogenization", "conceptual-blending"]
related_experiments: []
tags: ["q2-integrating", "prompt-strategy", "h6"]
---

# Seed brief isolation

## Definition

Generate the description of the seed domain — its most important mechanisms,
tricks, and failure modes — in a *fresh context that has not seen the
problem*, then inject that brief into the problem-solving context.

## Why it matters here

When one context is asked both "what is interesting about X" and "apply it
to my problem", the model retrieves the parts of X that already resemble
the problem — collapsing the seed back towards the home field. Isolation
forces the retrieval to be problem-blind, so the brief contains the seed's
own structure. Hypothesis H6. Cheap to implement with `claude -p`: two calls
instead of one.

**PopBlends** (Wang et al. 2023) is structurally close prior art: its
Stage-1 pipeline is a divergent step (expand each domain into
associations, independent of the other domain — the "Half-GPT" approach
uses the prompt `"What five {activities/adjectives/catchphrases} do you
associate with {entity} in {domain}?"`, generated per-entity without
reference to the target domain) followed by a convergent step (find the
association that best matches the *other* domain). That divergent step is
effectively an isolated brief-per-entity, generated blind to the eventual
pairing — a validated precedent that domain expansion done before (and
independent of) the connection step surfaces material a joint prompt
would miss. Their finding that GPT-3 confidently hallucinates attributes
for entities that structurally can't have them (e.g. catchphrases for a
mute character) is a concrete brief-writing failure mode to guard
against: an isolated brief-writer with no grounding can fabricate
"mechanisms" the seed domain doesn't actually have.

## Connections

- Plugs into step 2 of [[abstract-then-reinstantiate]].
- A mild form of the same idea: ask the brief-writer for mechanisms at the
  *method* level so granularity (H4) is controlled at brief time.
- [[conceptual-blending]] (PopBlends) demonstrates the divergent-then-
  convergent shape this concept relies on, in a narrower two-fixed-domains
  setting.
