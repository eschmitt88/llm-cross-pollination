---
kind: paper
title: "Death of the Novel(ty): Beyond n-Gram Novelty as a Metric for Textual Creativity"
authors: ["Arkadiy Saakyan", "Najoung Kim", "Smaranda Muresan", "Tuhin Chakrabarty"]
institutions: ["Columbia University", "Boston University", "Stony Brook University"]
year: 2026
venue: "ICLR 2026"
peer_reviewed: true
url: "https://arxiv.org/abs/2509.22641"
code_url: null
citations: null
source: "raw/papers/saakyan2026death.pdf"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["novelty-usefulness-tradeoff", "transfer-depth-ladder"]
tags: ["metrics", "llm-as-judge", "novelty", "appropriateness", "eval-design"]
---

# Death of the Novel(ty)

## TL;DR

The single most important methods warning for this project's evaluation
design. Creativity is dual — novelty *and* appropriateness — but the
field's default automatic metric (n-gram novelty, the basis of the
"Creativity Index") only measures the first half. With 8,618 expert-writer
annotations the authors show that **~91% of top-quartile n-gram-novel
expressions are not judged creative**, and that in open-source LLMs higher
n-gram novelty actively *correlates with lower pragmaticality*. LLM-as-judge
novelty ratings track expert preference better, including out of
distribution.

## Claims

- N-gram novelty is positively but weakly associated with expert-judged
  creativity; the ~91% false-positive rate in the top quartile makes it
  unusable as a standalone creativity metric.
- In open-source LLM text (unlike human text) novelty and pragmaticality are
  *negatively* related — pushing a model toward novel surface forms pushes
  it toward nonsense. This is the gameability failure mode made concrete.
- Frontier closed-source models are less likely than humans to produce
  expressions experts judge creative.
- Zero-shot / few-shot / finetuned models detect expert-perceived novelty
  well above random but struggle specifically to identify **non-pragmatic**
  expressions — the negative axis is the harder one to automate.
- LLM-as-judge novelty ratings align with expert writer preferences on an
  out-of-distribution dataset better than an n-gram metric does.

## Methods

- 8,618 expert writer annotations obtained by *close reading* of human- and
  AI-generated text, labelled on three separate axes: novelty,
  pragmaticality, sensicality. Separating pragmaticality from sensicality is
  what lets them show the novelty/pragmaticality inversion.
- Correlational analysis of n-gram novelty against those labels, then a
  detection study (zero-shot, few-shot, finetuned) and an OOD
  LLM-as-judge-vs-n-gram comparison.

## Results

- The 91% figure and the negative novelty-pragmaticality correlation are the
  two numbers to carry forward.

## Critique / open questions

- Domain is creative/literary writing with expert *writers* as annotators.
  This project's domain is STEM problem-solving, where "appropriateness"
  means the mechanism actually works, not that the prose is pragmatic —
  the analogy is strong but the annotator expertise does not transfer.
- Validating LLM-as-judge against expert humans is the right move, but the
  paper does not fully address judge self-preference bias when the judge and
  the generator come from the same family — a live concern for H2's judge.

## Trust signals

- **Credibility:** 5 — ICLR 2026 camera-ready, strong multi-institution NLP
  authorship (Muresan, Kim, Chakrabarty are established in exactly this
  area), an unusually large expert-annotation effort (8,618 close-reading
  judgments, not crowdworker skims), and a result that argues *against* the
  convenient metric rather than for the authors' own tool.

## Follow-up

- **Relevance: 5** — directly load-bearing for evaluation design, and it
  independently validates two commitments the project already made:
  [[novelty-usefulness-tradeoff]] (never score novelty alone) and the choice
  to rate outputs on a [[transfer-depth-ladder]] rather than a lexical
  distance. **Action items for H2:** (1) do not use n-gram or lexical
  novelty as an outcome measure — it would reward exactly the
  vocabulary-level pseudo-transfer H2 exists to detect; (2) adopt
  LLM-as-judge with a rubric, as this paper's OOD result supports; (3)
  guard the judge against self-preference by using a different model family
  from the generator, and keep the human spot-check arm.
