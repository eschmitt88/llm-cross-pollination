---
kind: concept
name: "seed brief isolation"
status: seedling
added: "2026-08-22"
sources: []
related_concepts: ["abstract-then-reinstantiate", "foreign-seed", "homogenization"]
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

## Connections

- Plugs into step 2 of [[abstract-then-reinstantiate]].
- A mild form of the same idea: ask the brief-writer for mechanisms at the
  *method* level so granularity (H4) is controlled at brief time.
