---
kind: concept
name: "novelty–usefulness trade-off"
status: seedling
added: "2026-08-22"
sources: []
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

## Connections

- [[analogical-distance]] is expected to trade these off: far seeds raise
  novelty and lower usefulness; the H3 sweep maps the curve.
- The judge inherits [[homogenization]] — it may rate the conventional answer
  as more useful simply because it is familiar. Human calibration is not
  optional.
