---
kind: paper
title: "OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts"
authors: ["Jason Priem", "Heather Piwowar", "Richard Orr"]
institutions: ["OurResearch"]
year: 2022
venue: "STI 2022 (26th Int. Conf. on Science, Technology and Innovation Indicators)"
peer_reviewed: false
url: "https://arxiv.org/abs/2205.01833"
code_url: "https://docs.openalex.org/"
citations: null
source: "raw/papers/priem2022openalex.pdf"
added: "2026-08-22"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["sampling-frame", "external-randomness", "foreign-seed"]
tags: ["infrastructure", "taxonomy", "sampler", "h1"]
---

# OpenAlex

## TL;DR

The system paper for the scholarly knowledge graph that `xpol` uses as its
[[sampling-frame]]. Built by OurResearch (the Unpaywall team) to replace the
discontinued Microsoft Academic Graph: 209M works, ~213M disambiguated
authors, 124k venues, 109k institutions, and 65k Wikidata-linked concepts
assigned by an automated hierarchical multi-tag classifier. Fully open —
CC0 data dump, free REST API, no key required.

## Claims

- Complete, open replacement for MAG, covering all of scholarship rather
  than one publisher's or one field's slice.
- Concepts are linked to works via an automated hierarchical multi-tag
  classifier and grounded in Wikidata, giving a machine-readable
  domain > field > subfield > topic hierarchy.
- Access via three routes — web GUI, full data dump, and high-volume REST
  API — which is what makes seeded, reproducible offline sampling possible.
- Explicitly self-described as "under active development," with accuracy
  and coverage of citations and author/institution parsing named as known
  weak spots.

## Methods

- Infrastructure/resource paper: describes ingest sources, the entity model
  (works, authors, venues, institutions, concepts), and the classifier,
  rather than testing a hypothesis.

## Results

- Headline for us: a free, comprehensive, hierarchically-structured,
  programmatically-sampleable inventory of scholarly topics — the concrete
  artifact that makes [[external-randomness]] implementable. Without a frame
  like this, "pick a random field" has no denominator.

## Critique / open questions

- **The frame is not uniform over "fields" in any principled sense.** Topic
  sizes are wildly unequal (biomedicine dwarfs, say, numismatics), and the
  classifier is automated and imperfect. Sampling uniformly over *topics*
  is not the same as sampling uniformly over *intellectual territory*, and
  neither is obviously the right target. This is exactly why `xpol`
  stratifies rather than drawing flat — a design choice this paper
  motivates but does not solve.
- Classifier errors propagate directly into seed quality: a mislabelled
  topic yields a seed that isn't really from the field it claims.
- The concepts taxonomy described here has since been superseded by
  OpenAlex's newer **topics** scheme (~4,500 topics); the paper predates it,
  so treat the specific numbers as of-2022 and verify against current docs.
- Not peer-reviewed in the usual sense (STI is a conference with proceedings
  but this is a resource description by the vendor).

## Trust signals

- **Credibility:** 4 — authored by the team that also built Unpaywall
  (well-established, widely trusted open-scholarship infrastructure), and
  the claims are about a public artifact that can be, and has been,
  independently verified by using it. Docked one because it is a
  self-description of the authors' own product rather than an independent
  evaluation, and the accuracy caveats are acknowledged but unquantified.

## Follow-up

- **Relevance: 5** — this is the sampler's foundation and the citation that
  anchors [[sampling-frame]]. **Action items:** (1) pin the OpenAlex
  snapshot/version in `config.yaml` so H1/H3 draws stay reproducible as the
  taxonomy evolves; (2) record which taxonomy level (domain / field /
  subfield / topic) each draw came from, since H4 tests exactly the
  granularity question; (3) treat classifier noise as a known error source
  when interpreting distance bands in H3.
