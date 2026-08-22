---
kind: concept
name: "verbalized sampling"
status: seedling
added: "2026-08-22"
sources: ["zhang2025verbalized"]
related_concepts: ["external-randomness", "foreign-seed"]
related_experiments: []
tags: ["q2-integrating", "method"]
---

# Verbalized sampling

## Definition

A training-free prompting technique (Zhang, Yu, Chong et al., ICML 2026):
instead of asking a model for one instance of something ("tell me a joke
about coffee"), ask it to verbalize a small distribution over several
candidates with probabilities ("generate 5 jokes about coffee and their
probabilities"), then sample from that. Recovers much of the output
diversity that post-training alignment suppresses (RLHF mode collapse),
without fine-tuning — reported 1.6-2.1x diversity gain on creative-writing
tasks, with the effect *larger* for more capable models.

## Why it matters here

Its premise is the mirror image of [[external-randomness]]: this project's
default stance is "never trust the model to pick," because
[[external-randomness]]'s sources (LLMs asked for a random number or a
random field are measurably non-uniform, sometimes catastrophically so)
show naive model-internal sampling fails. Verbalized sampling is evidence
that a *specific elicitation format* — not temperature, not fine-tuning —
substantially closes that gap for open-ended generation tasks. It doesn't
show the result matches an external uniform target (a different, untested
claim), so it's not a substitute for [[external-randomness]] in the
sampler. Where it's plausibly useful is on the *integrator* side (Q2): the
multi-seed tournament (H5) needs the model to propose several candidate
mappings from a fixed [[foreign-seed]] to the problem, and "verbalize k
candidates with weights" is a stronger, better-evidenced elicitation
format for that than naive "be creative."

## Connections

- Candidate technique for H5's tournament arm (k proposals → judge
  merges/selects) — worth a direct ablation against naive multi-sample
  prompting at equal token cost.
- Worth one explicit ablation before treating [[external-randomness]] as
  strictly necessary: does asking for "k diverse fields with probabilities"
  get closer to uniform over the [[sampling-frame]] than single-shot
  asking? If yes, it doesn't replace external RNG (still model-controlled)
  but it bounds how much of H1's expected skew is a prompting-format
  artifact vs. a deeper sampling limitation.
