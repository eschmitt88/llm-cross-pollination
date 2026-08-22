---
kind: decision
id: 1
title: Scope and framing of llm-cross-pollination
status: accepted
date: "2026-08-22"
---

# 0001 — Scope and framing

## Context

The user wants LLM-assisted STEM work to borrow methods from foreign fields
rather than defaulting to the home field's toolkit, and asked for research
on (1) how to choose a foreign topic truly at random and (2) how to integrate
it into the query.

## Decision

- **Scope:** STEM problem-solving with Claude (via `claude -p` on the
  subscription). Not general creative writing, though the creativity /
  homogenization literature is in scope as evidence and as a source of
  metrics.
- **Deliverable:** a reusable Claude Code skill (working name
  `/cross-pollinate`) backed by a small Python sampler package. Research
  phases exist to earn the design of that skill, not as ends in themselves.
- **Randomness is external.** The model never selects the foreign topic in
  the production path; it may do so only as the baseline condition under
  measurement (H1).
- **Evaluation pairs novelty with usefulness** and rates *transfer depth*
  (vocabulary → metaphor → mechanism → method), so that "weird" cannot win
  on its own. HCE applies: a held-out problem set is never used while
  iterating on prompts.
- **Order of work:** sampler + LLM-randomness measurement first (cheap,
  decisive), then the integration-strategy bake-off, then distance sweep
  and tournament, then packaging.
- **Repo:** public, `agency: standard` for now. `--experiments` skill group
  linked because phases 1–3 are empirical.

## Consequences

- `docs/research-plan.md` is the living plan; hypotheses H1–H6 there are
  the experiment backlog.
- Problem set is drawn partly from the user's other research repos; those
  problem statements must be written so they do not leak private details
  (this repo is public).
