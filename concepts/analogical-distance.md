---
kind: concept
name: "analogical distance"
status: growing
added: "2026-08-22"
sources: ["fu2013meaning", "uzzi2013atypical", "olson2021naming", "chan2018solvent", "wang2024scimon", "malthouse2021influence", "chan2011benefits"]
related_concepts: ["foreign-seed", "sampling-frame", "structure-mapping", "transfer-depth-ladder"]
related_experiments: []
tags: ["q1-choosing", "h3"]
---

# Analogical distance

## Definition

How far the seed's domain is from the problem's domain. Operationalised two
ways here: cosine distance between embeddings of the problem statement and
the frame entry, and hop distance in the frame's taxonomy.

## Why it matters here

The design-by-analogy literature (Fu, Chan, Cagan et al. on "near" vs "far";
Chan & Schunn) reports a non-monotone effect: near sources add little, very
far sources produce metaphor without mechanism, and a middle band is most
productive. Hypothesis H3 tests whether that holds for LLM-assisted STEM
work. If it does, the sampler should draw from a **distance band** rather
than uniformly — "random" becomes "random within the useful band".

[[fu2013meaning]] is the primary source of the "near vs. far" design
literature (full text unreachable at ingest time — bot-blocked and
paywalled; note is abstract/secondary-source only, flagged for re-fetch
with institutional access before H3's power analysis). Independently,
[[uzzi2013atypical]]'s bibliometric analysis of 17.9M papers gives
large-N, real-world evidence for the same non-monotone shape at a
different unit of analysis: the highest-impact papers combine an
exceptionally *conventional* core of citations with an *atypical* fringe,
not atypicality throughout — "hit" papers were twice as likely to have
this mixed profile. It's a different mechanism (citation-combination
novelty, not injected mechanism transfer) but the same "mixture beats
purity" shape H3 predicts, which is independent corroboration worth citing
when framing the expected result curve.

## Connections

- Relational vs. surface similarity ([[structure-mapping]]) is the deeper
  notion; embedding distance is a cheap proxy that mostly tracks surface
  similarity. A seed can be far in embedding space and structurally near —
  which is exactly the kind we want. Worth a second metric eventually.
- Output of the sweep is plotted as [[transfer-depth-ladder]] score vs.
  distance.
