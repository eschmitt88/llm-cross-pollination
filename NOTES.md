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

## 2026-08-22 (session 2 — agency: max burst)

### Did

- Switched `budget.yaml` to `agency: max`; headroom verdict slow/low (GPU
  shared) → one batch at a time, CPU embeddings.
- Built `xpol` (OpenAlex frame: 4/26/245/4516/45154 entries; OS-entropy or
  logged seed; domain-stratified round-robin; home-field exclusion by
  nearest-topic vote; cosine-percentile distance band; CLI `sample` /
  `prompt` / `stats`; 8 tests). Prompt templates in `prompts/`.
- H1 (450 `claude -p` calls): model-chosen "random topics" mode-collapse.
- Ingested 15 papers via two Sonnet agents; the nightly `/curate` cron then
  drained the remaining 21 candidates (33 literature notes, 14 concepts,
  2 MoCs). Lint clean.
- H2/H6 bake-off: 6 dev problems × 3 seeds × 4 strategies + 2 baselines,
  Sonnet 5 generator, Opus 5 judge.
- `docs/method.md` v0.1, ADR 0002, install-ready `skill/cross-pollinate/`,
  `docs/sampler-demo.md` (20 blind seeds).
- Ops: every `claude -p` call fired the SessionEnd hook (journal commit +
  push per call, 108 junk commits) → all batch runners now call
  `claude -p` with `cwd=~/projects/.claude-p-cwd`; saved as a memory. One
  API bio-safety refusal crashed the bake-off pool once → runner now
  records refusals per job and retries transients.

### Findings

- **H1 ✓, hard.** Sonnet 5: 71% duplicate answers, "ethnomusicology of
  Andean panpipe traditions" 33×/100; Haiku "random discipline": mycology
  41%; "a field far from ML": forestry+ecology 60%. Best phrasing still
  0.7% health sciences. Sampler: 0% dup, 25–26/26 fields.
- **H2 ✓.** abstract-reinstantiate-brief 3.29 mean depth (88% ≥ mechanism)
  vs naive 2.12 (41%); paired 13/1, p=0.002. Persona ≈ naive (5/4).
- **H6 ✓ directional.** Problem-blind brief +0.35 depth, 7/1, p=0.07.
- **Transfer ≠ novelty.** Usefulness flat (~2.2/4) in every arm, equal to a
  no-seed "be unconventional" prompt; 94% of proposals judged reachable by
  the home field. The common outcome is *rediscovery by a foreign path*;
  ~6% foreign-and-useful. Hard-constraint physical design transfers worst.
- 5.6% of seeded generations refused by the bio classifier (medical /
  toxicology seeds).

### Next

- H5 tournament (k=8 seeds, brief template, judge selects) — does the
  foreign-and-useful rate scale with k?
- Human calibration: user blind-rates ~20 proposals on usefulness and
  home-field-default; agreement with the Opus judge.
- H3 distance sweep with the brief template (4 bands).
- H4 granularity (subfield vs topic vs keyword) — keyword level looked
  noisy in the demo.
- Sampler: resample-on-refusal flag; optional `--exclude-fields Medicine`.
- Install the skill: `ln -s .../skill/cross-pollinate ~/.claude/skills/`.
