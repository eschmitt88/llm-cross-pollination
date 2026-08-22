---
kind: paper
title: "Structure-Mapping: A Theoretical Framework for Analogy"
authors: ["Dedre Gentner"]
institutions: ["Bolt Beranek and Newman Inc."]
year: 1983
venue: "Cognitive Science 7(2), 155-170"
peer_reviewed: true
url: "https://doi.org/10.1207/s15516709cog0702_3"
code_url: null
citations: 5686
source: "raw/papers/gentner1983structuremapping.pdf"
added: "2026-08-22"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["structure-mapping"]
tags: ["theory", "analogy", "foundational"]
---

# Structure-Mapping: A Theoretical Framework for Analogy

## TL;DR

The foundational paper the [[structure-mapping]] concept is named after.
Formalizes analogy as a mapping of *relations* (predicates taking two or
more arguments — CAUSE, GREATER-THAN, COLLIDE) from a base domain to a
target domain, deliberately discarding object *attributes* (one-place
predicates like LARGE, YELLOW). The mapping is governed by the
**systematicity principle**: prefer mappings that carry over coherent,
interconnected systems of relations (especially higher-order relations —
relations *between* relations, like CAUSE) over mappings of isolated facts,
even when the isolated-fact mapping is locally as good a match.

## Claims

1. Knowledge is represented as predicates over objects; attributes (1-place)
   and relations (2+-place) are the essential distinction.
2. A good analogy maps relations and preserves the relational structure —
   what predicates are true of the objects (their attributes) matters much
   less than how the objects relate to each other.
3. **Systematicity**: mappings are preferred when the predicates being
   carried over are themselves embedded in a system of higher-order
   relations, not isolated. This is presented as an *implicit* preference —
   people don't need to be told to prefer systematic mappings, it falls out
   of preferring deeply interconnected predicate structure.
4. Worked example: the solar-system/atom analogy maps REVOLVES-AROUND,
   ATTRACTS, and the causal relation between them (attraction CAUSES
   revolution), not the surface attributes (sun is YELLOW, nucleus is not).

## Methods

- Purely theoretical/formal — propositional representation of domains as
  predicate networks, interpretation rules (discard attributes → try to
  preserve relations → prefer systems of relations over isolated ones),
  worked examples. No empirical study in this paper.

## Results

- N/A (theory paper). The framework has since been validated extensively
  in follow-on empirical work (not covered here).

## Critique / open questions

- The theory explains *why* a good analogy works once one is found; it does
  not by itself give a procedure for *finding* candidate analogies at scale
  — that's the province of later computational-analogy work
  (Structure-Mapping Engine, and modern LLM-based analogy retrieval).
- "Systematicity" is a preference over mappings a reasoner already has in
  hand; operationalizing it as a *filter or scoring function* for
  LLM-generated cross-domain mappings (i.e., a computable proxy for "how
  much relational structure survived") is exactly the open engineering
  problem for this project's [[transfer-depth-ladder]] rubric.

## Trust signals

- **Credibility:** 5 — the founding paper of structure-mapping theory,
  5,686 citations (Semantic Scholar), peer-reviewed in Cognitive Science,
  the basis for essentially all subsequent computational and psychological
  analogy work cited elsewhere in this project's literature.

## Follow-up

- **Relevance: 5** — this *is* the canonical source for
  [[structure-mapping]], the theoretical grounding for why naive
  "incorporate ideas from X" fails (surface/attribute matching) and why
  [[abstract-then-reinstantiate]] is designed the way it is (force
  relational, not attribute, correspondence). The systematicity principle
  is the closest thing in the literature to a definition of "mechanism
  transfer" vs. "decoration" — worth quoting directly when writing the
  transfer-depth-ladder judge rubric.
