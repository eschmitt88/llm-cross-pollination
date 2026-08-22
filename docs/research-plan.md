---
kind: plan
name: research-plan
status: active
added: "2026-08-22"
updated: "2026-08-22"
---

# Research plan — seeding LLMs with foreign disciplines

## The problem

An LLM asked to help with a STEM problem produces the *mode* of its training
distribution conditioned on the domain: the field's canonical methods,
phrased the way the field phrases them. That is usually what you want. It is
not what you want when you are stuck, when the field's toolkit is the thing
that has already failed, or when you suspect the interesting move lives
somewhere else. Left to itself the model also *converges* — across sessions
and across users its "creative" suggestions cluster on a few stereotyped
sources (biology, physics analogies, music). See
[[homogenization]].

We want a procedure that reliably injects a **foreign seed** —
[[foreign-seed]] — into a query such that what transfers is a *mechanism*
the home field can actually use, not a metaphor. Two sub-questions,
corresponding to the two halves of the project:

- **Q1 — choosing.** How to pick a foreign topic *truly* at random: from what
  population ([[sampling-frame]]), at what granularity (field / subfield /
  method), at what conceptual distance ([[analogical-distance]]), and with
  randomness that does not come from the model ([[external-randomness]]).
- **Q2 — integrating.** Which prompt structures turn the seed into usable
  transfer ([[abstract-then-reinstantiate]], [[seed-brief-isolation]],
  [[structure-mapping]]), and how to tell decoration from transfer
  ([[transfer-depth-ladder]]).

## Hypotheses

| id | hypothesis | how we would know |
|----|-----------|-------------------|
| H1 ✓ | Asking the model to "pick a random field" yields a heavily skewed distribution (a few favourite fields, entropy far below uniform over any reasonable taxonomy). External sampling is necessary, not optional. | Sample N≈500 "random discipline" answers at several temperatures / phrasings; compute entropy and top-k mass vs. uniform over the chosen taxonomy. Cheap, do first. |
| H2 ✓ | Integration strategy dominates topic choice: naive "incorporate ideas from X" produces vocabulary-level transfer; abstract-then-reinstantiate produces mechanism-level transfer with the *same* seeds. | Bake-off across strategies on a fixed problem set and fixed seed list; rate each output on the transfer-depth ladder (LLM judge + human spot check). |
| H3 | There is a useful-distance band ("far but not too far"): near seeds add nothing, very far seeds give metaphor only, mid-distance seeds give the most mechanism-level transfers. | Sweep seeds binned by embedding / taxonomy-hop distance from the problem; plot transfer depth and usefulness vs. distance. |
| H4 | Method-level seeds (a specific technique or phenomenon: "retrosynthesis", "Ziegler–Natta catalysis") transfer better than field-level seeds ("organic chemistry"). | Same bake-off with granularity as a factor. |
| H5 | Multiple seeds + selection (generate k, critic picks/merges) beats a single seed at equal token cost once k ≥ 3, and beats a "just be creative" / high-temperature baseline. | Tournament arm vs. single-seed arm vs. baselines, same judge. |
| H6 ✓(p=0.07) | Generating the foreign-domain brief in a *separate* context (no sight of the target problem) and then injecting it yields more genuine transfer than asking one context to do both, because the model otherwise retrieves only the parts of X that already resemble the problem. | Isolation arm vs. joint arm. |

## Design space

### Q1 — the sampler

- **Population.** Candidate sampling frames, to be compared on coverage,
  granularity and how easy "distance" is to compute:
  OpenAlex topics (4-level hierarchy, ~4.5 k leaves, has embeddings-friendly
  descriptions); Wikipedia vital articles / category graph; MSC2020; ACM CCS;
  arXiv categories; CPC patent classes (the TRIZ lineage — patents are
  *solutions*, which is what we want to borrow); hand-curated "mechanism"
  lists (named effects, named reactions, named algorithms).
- **Randomness.** OS RNG (`secrets` / seeded `random`), seed recorded in
  `config.yaml`. Stratify across top-level domains so a draw of five seeds
  does not land on five biology topics.
- **Distance control.** Embed the problem statement and every frame entry
  (local sentence-embedding model on the 5080); sample from a cosine-distance
  band. Alternative: hop distance in the taxonomy. Both logged so H3 can use
  either.
- **Granularity.** Field → subfield → named method. Sampler takes a level
  argument; H4 tests it.

### Q2 — the integrator

Prompt strategies, each a Markdown template under `prompts/`:

1. *Naive injection* — "incorporate ideas from {X}". The baseline to beat.
2. *Persona* — "you are an expert in {X} looking at this problem".
3. *Abstract → retrieve → map back* ([[abstract-then-reinstantiate]]):
   restate the problem domain-neutrally (what is the contradiction, the
   invariant, the resource being traded), ask how {X} handles that abstract
   problem, then build an explicit correspondence table and critique it for
   surface-only matches.
4. *Forced connection* (de Bono random-word): list the 5–7 most important
   mechanisms of {X}, force a link from each to the problem, keep the
   survivors.
5. *Isolated brief* ([[seed-brief-isolation]]): a fresh context writes a
   one-page mechanisms brief on {X}; the main context receives only the brief.
6. *Dialectic* — home-field expert and {X}-expert personas argue; a third
   pass extracts what survived.
7. *Multi-seed tournament* — k seeds → k proposals → judge merges/selects.

### Evaluation

- **Problem set.** 10–20 concrete STEM problems drawn from this user's own
  backlog (FEA of printed clay vessels, submerged-platform stability,
  Dota win-probability modelling, RL on hex physics, 3D-design QA, …) plus a
  few public ones. Split dev / held-out per the HCE rule; the held-out set is
  never used while tuning prompts.
- **Metrics.**
  - *Diversity*: pairwise embedding distance among outputs across seeds and
    across runs; DAT-style semantic spread.
  - *Transfer depth*: 0–4 on the [[transfer-depth-ladder]] (none / vocabulary
    / metaphor / mechanism / method-with-math), LLM judge with rubric,
    calibrated against human ratings on a subset.
  - *Usefulness*: would the user actually try it? Judge + human on a subset.
    Novelty without usefulness is noise — [[novelty-usefulness-tradeoff]].
- **Baselines.** No seed; "be creative / unconventional"; higher
  temperature; model-chosen foreign topic (the H1 condition).

## Phases

0. **Framing (now).** Literature triage on the three threads (homogenization
   + metrics; cross-domain prompting; sampling frames + analogical distance),
   concept seedlings, this plan.
1. **Sampler + H1.** Build `xpol` (small Python package): frame loaders,
   stratified seeded sampling, embedding distance. Run the LLM-randomness
   measurement. Cheap and decisive — do before anything else.
2. **Integrator bake-off (H2, H4, H6).** Fixed seeds, fixed dev problems,
   seven strategies, judge + human spot check.
3. **Distance sweep (H3)** and **tournament (H5)** with the winning strategy.
4. **Package.** The winning pipeline becomes a Claude Code skill
   (`/cross-pollinate <problem> [--distance band] [--k N]`) proposed to
   `claude-system` via `/elevate`. That skill is the deliverable; everything
   above is how we earn the right to write it.

## Status (2026-08-22)

H1 confirmed (sampler necessary), H2 confirmed (abstract-reinstantiate ≫ naive ≈ persona), H6 directionally confirmed (problem-blind brief +0.35 depth). New finding: transfer is mostly *rediscovery* — 94% of proposals judged reachable by the home field; only ~6% foreign *and* useful. Method v0.1 in `docs/method.md`; skill in `skill/cross-pollinate/`. Next: H5 (more seeds), human judge calibration, H3 (distance sweep).

## Open questions

- Is "random" even the goal, or is "uniformly surprising but usable" — which
  argues for distance-controlled rather than uniform sampling? H3 decides.
- Does the judge share the homogenization bias it is grading? Calibrate
  against human ratings early.
- Seeds that are *themselves* methods of the home field in disguise (e.g.
  "simulated annealing" for an optimisation problem) — detect and reject, or
  let the distance band handle it?
