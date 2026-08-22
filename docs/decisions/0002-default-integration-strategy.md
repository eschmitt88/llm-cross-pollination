---
kind: decision
id: 2
title: Default integration strategy and seed count for the cross-pollinate method
status: accepted
date: "2026-08-22"
---

# 0002 — Default integration strategy: abstract-reinstantiate-brief, k=5

## Context

H2 bake-off (`experiments/2026-08-22-h2-integration-bakeoff/`): with
identical seeds, `abstract-reinstantiate-brief` reached mean transfer depth
3.29 (88% ≥ mechanism) vs naive 2.12; paired 13 wins / 1 loss (p=0.002).
Persona prompting was indistinguishable from naive. Usefulness was flat
across arms and 94% of proposals were judged reachable by the home field;
only ~6% of seeded outputs were both foreign and useful.

## Decision

- Default template is `abstract-reinstantiate-brief`: the seed brief is
  written in a problem-blind context, then mapped in the problem context.
- Persona prompting is not offered as an option.
- Default seed count is 5 (was 3) because the foreign-and-useful rate is
  per-seed and low; the user filters.
- The method is described honestly as producing *foreign derivations of
  mostly-known methods*, not as a novelty engine, until H5/H3 move the
  foreign-and-useful rate.
- Refusals by the API safety classifier (medical/toxicology seeds) are
  handled by resampling one seed, not by rephrasing.

## Consequences

- `skill/cross-pollinate/SKILL.md` and `docs/method.md` §5 carry these
  defaults.
- Usefulness numbers from the Opus judge are provisional until a human
  rates a subset (next_candidates in the H2 README).
