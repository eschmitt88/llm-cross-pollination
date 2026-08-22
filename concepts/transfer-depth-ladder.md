---
kind: concept
name: "transfer depth ladder"
status: growing
added: "2026-08-22"
sources: ["hope2017accelerating", "zhang2025noveltybench", "yasunaga2023large"]
related_concepts: ["structure-mapping", "novelty-usefulness-tradeoff", "foreign-seed"]
related_experiments: []
tags: ["evaluation", "q2-integrating"]
---

# Transfer depth ladder

## Definition

An ordinal rubric for what actually crossed from seed to problem:

0. **none** — seed ignored or mentioned and dropped
1. **vocabulary** — the output is the home-field answer wearing the seed's words
2. **metaphor** — a loose "it's like X" framing that suggests no concrete step
3. **mechanism** — a specific causal mechanism from the seed is mapped to a specific element of the problem, with the correspondence stated
4. **method** — a procedure (ideally with its math / algorithm) transferred and adapted so it could be run

## Why it matters here

Diversity metrics reward *different*; this rubric rewards *transferred*.
Levels 3–4 are the project's target. It is the primary outcome measure in
the integration bake-off (H2), the granularity test (H4), the isolation test
(H6), and the distance sweep (H3). Scored by an LLM judge with this rubric
and calibrated on a human-rated subset.

**NoveltyBench** (Zhang et al. 2025) independently validates the design
choice of an ordinal/judged rubric over a raw embedding-distance metric:
they found n-gram overlap, embedding distance, and BLEU/ROUGE/BERTScore
all diverge from human judgment of "functionally distinct," and instead
trained a classifier on 1,100 human-annotated pairs to judge functional
equivalence (79% accuracy, F1 0.811 vs. humans). Their `distinct_k` /
patience-weighted `utility_k` formalism is a reusable pattern for
combining a discrete judgment (here: equivalence class / here: ladder
rung) with a separate quality score into one number, worth adapting for
combining ladder rung with [[novelty-usefulness-tradeoff]].

**Hope et al. 2017**'s "good idea" rater criteria — (1) uses a different
mechanism than the original, (2) achieves the same purpose, (3) is
feasible — is a pre-LLM precedent for a similar three-part judged rubric
and a candidate scaffold for the rung-3/rung-4 boundary (does the
"different mechanism" actually still serve the original purpose, or is it
decoration?).

**Yasunaga et al. 2023**'s qualitative failure taxonomy on same-domain
analogical prompting (generalization gap / overreliance on the exemplar /
irrelevant exemplar) is a useful negative-space checklist: a rung-3/4
output can still fail for reasons other than shallow transfer (e.g. the
mechanism maps correctly but doesn't generalize to the specific problem
instance) — the ladder alone may not catch this failure mode and could
need a secondary "does it actually solve the problem" flag, tying back to
[[novelty-usefulness-tradeoff]].

## Connections

- Derived from [[structure-mapping]]: the rungs are increasing amounts of
  relational structure surviving the mapping.
- Paired with usefulness in [[novelty-usefulness-tradeoff]] — a level-4
  method that is wrong for the problem is still not useful.
