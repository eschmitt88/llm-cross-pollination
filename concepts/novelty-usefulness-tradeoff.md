---
kind: concept
name: "novelty–usefulness trade-off"
status: growing
added: "2026-08-22"
sources: ["doshi2024generative", "zhang2025noveltybench", "wan2026diverse", "olson2021naming", "saakyan2026death", "tan2026automated", "carichon2026ideafix", "si2024can", "wang2024scimon", "hu2024nova", "chan2011benefits"]
related_concepts: ["transfer-depth-ladder", "homogenization", "analogical-distance"]
related_experiments: []
tags: ["evaluation"]
---

# Novelty–usefulness trade-off

## Definition

Creativity is conventionally defined as novel *and* useful. Any metric that
scores only novelty (embedding spread, n-gram novelty, DAT-style distance)
is maximised by nonsense; any metric that scores only usefulness is
maximised by the home-field answer the project is trying to escape.

## Why it matters here

Every experiment reports both, and the headline outcome is the
**Pareto front**: strategies that raise [[transfer-depth-ladder]] score
without dropping usefulness. Usefulness is judged ("would the user actually
try this next?") by an LLM judge calibrated on a human-rated subset; the
held-out problem set (HCE rule) is scored once, at the end.

Two reusable instruments for this pairing:

- **Doshi & Hauser 2024** operationalize exactly this pair with a 6-item,
  9-point-Likert instrument: novelty = mean(novel, original, rare),
  usefulness = mean(appropriate, feasible, publishable), each with
  Cronbach's α > 0.89 — a directly adaptable rubric (swap "publishable"
  for a STEM-appropriate criterion like "buildable"/"testable") for our
  own human-calibration subset. They also show self-assessment is
  unreliable (writers show no significant novelty/usefulness difference
  across conditions where blind third-party evaluators do) — a caution
  against ever trusting the generating model's own self-rating of its
  output's usefulness.
- **NoveltyBench**'s `utility_k` formalizes the *combination* rather than
  just the pairing: a generation's marginal utility is its quality score
  if — and only if — it is functionally distinct from prior generations,
  else zero, summed with geometric patience-decay across k samples. This
  is a candidate formula for combining [[transfer-depth-ladder]] rung
  with a usefulness score into one number per run of the sampler+
  integrator pipeline (patience parameter would need its own
  sensitivity check before adoption).

## Connections

- [[analogical-distance]] is expected to trade these off: far seeds raise
  novelty and lower usefulness; the H3 sweep maps the curve.
- The judge inherits [[homogenization]] — it may rate the conventional answer
  as more useful simply because it is familiar. Human calibration is not
  optional.
