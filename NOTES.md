# NOTES

Running log of work sessions. `/wrap` appends a new dated section at the
end of each session with **Did / Findings / Next** subsections. The
SessionEnd hook backstops this if you forget.

<!-- entries go below this line, newest at bottom -->

## 2026-08-22

### Did

- Scaffolded the project (`/new-project llm-cross-pollination --experiments`,
  public, Pages enabled).
- Wrote `docs/research-plan.md` (problem, hypotheses H1–H6, design space for
  the sampler and the integrator, evaluation, phases) and ADR 0001 (scope).
- Seeded 10 concepts in two clusters — *choosing the seed* (foreign-seed,
  sampling-frame, external-randomness, analogical-distance) and *integrating
  the seed* (structure-mapping, abstract-then-reinstantiate,
  seed-brief-isolation, transfer-depth-ladder) — plus homogenization and
  novelty-usefulness-tradeoff for the problem/evaluation side.
- Ran three `/discover` triages (36 candidates) in `raw/_candidates/`:
  homogenization + diversity metrics; cross-domain prompting techniques;
  random-topic sampling + analogical distance.

### Findings

- The prior art splits cleanly along the project's two questions. Q1 has a
  concrete operationalisation already ("Directed Diversity" — embedding
  distance steering; Fu/Chan et al. on near/far analogical distance), plus
  evidence that LLMs are poor RNGs, which supports external randomness (H1).
  Q2 has analogical prompting, AutoTRIZ, SOLVENT/analogy mining, PopBlends,
  multi-persona, and the AI-scientist idea generators.
- Homogenization is well-evidenced (Doshi & Hauser; Anderson et al.;
  Padmakumar & He) and there are usable metrics (DAT, NoveltyBench,
  Verbalized Sampling as a prompting baseline).
- All 10 concepts are currently sourceless (lint flags them) — expected on
  day one; the next ingest pass fixes it.

### Next

- Curate the three candidate files: `/fetch-paper` + `/ingest` the top ~8
  (Fu et al. near/far; Directed Diversity; Yasunaga analogical prompting;
  AutoTRIZ; Doshi & Hauser; Anderson et al.; Verbalized Sampling; LLMs as
  bad dice players) and attach them as `sources:` on the concepts.
- Phase 1: build the `xpol` sampler (OpenAlex topics frame, stratified
  seeded draws, embedding distance) and run H1 — the LLM-randomness
  measurement — as the first `/new-experiment`.
- Write the dev problem set (10–20 STEM problems, scrubbed of private
  details) and reserve the held-out split.
