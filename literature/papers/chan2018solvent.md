---
kind: paper
title: "SOLVENT: A Mixed Initiative System for Finding Analogies between Research Papers"
authors: ["Joel Chan", "Joseph Chee Chang", "Tom Hope", "Dafna Shahaf", "Aniket Kittur"]
institutions: ["University of Maryland", "Carnegie Mellon University", "Hebrew University of Jerusalem"]
year: 2018
venue: "Proc. ACM Hum.-Comput. Interact. 2 (CSCW), Article 31"
peer_reviewed: true
url: "https://doi.org/10.1145/3274300"
code_url: null
citations: 94
source: "https://doi.org/10.1145/3274300"  # no raw/ artifact — OA but Cloudflare-blocked, see note
added: "2026-08-22"
relevance: 4
credibility: 5
status: skimmed
related_experiments: []
related_concepts: ["structure-mapping", "analogical-distance", "abstract-then-reinstantiate"]
tags: ["analogy-mining", "purpose-mechanism", "schema", "cross-domain-retrieval"]
---

# SOLVENT

## NOTE ON SOURCE

**Full text not fetched.** The paper is genuinely open access (Unpaywall
confirms `is_oa: true`, publisher-hosted), but the ACM Digital Library PDF
endpoint is behind Cloudflare bot-defense and returned a challenge page on
every attempt; three plausible author-site mirrors 404'd. This note is
written from the **complete publisher abstract** (retrieved via the
Semantic Scholar API) plus Crossref metadata — so the claims below are the
authors' own summary, not a read of the full text. Methods and results
detail is correspondingly thin. **Anyone with ACM DL access should pull the
PDF and deepen this note before it is used to justify a design decision.**

## TL;DR

Scientific discovery is often driven by analogies from distant domains, but
the volume of literature makes those analogies impossible to find by hand.
SOLVENT has humans annotate four aspects of a paper — **background** (the
high-level problem), **purpose** (the specific problem), **mechanism** (how
it was achieved), and **findings** (what was learned) — and builds a
semantic representation from those annotations that supports analogy search
across domains. It beats information-retrieval baselines, the annotation
scheme generalizes beyond the domain it was developed on, and experts judge
the retrieved analogies useful.

## Claims

- The system finds more analogies than baseline information-retrieval
  approaches.
- **Annotators and annotations generalize beyond domain** — the
  purpose/mechanism schema is not tied to the field it was built on, which
  is what makes cross-domain retrieval possible at all.
- The analogies found are judged **useful by experts**, not merely
  structurally valid.
- Framed as a path toward computationally supported knowledge sharing across
  research communities.

## Methods

- Mixed-initiative: human annotation of the four-part schema plus a
  computational model that constructs a semantic representation from those
  annotations and retrieves structural matches. (Further detail not
  available without the full text.)

## Critique / open questions

- The core dependency is **human annotation**, which is exactly the
  bottleneck an LLM could now remove — the obvious modern reframing, and one
  the LLM-era successors ([[wang2024scimon]], co-authored by Hope) partially
  pursue.
- Whether the purpose/mechanism decomposition is the *right* abstraction, or
  merely a workable one, is not settled by this paper.
- Effect sizes, baselines, and the expert-usefulness protocol are all
  unverified here — see the source note.

## Trust signals

- **Credibility:** 5 — CSCW 2018 (rigorous peer review), an unusually strong
  author group for this exact problem (Kittur and Shahaf are central to
  computational analogy; Hope and Chan carry this line into
  [[hope2017accelerating]] and [[wang2024scimon]]), 94 citations. Credibility
  is high on venue and provenance grounds; note that *this note's* fidelity
  is limited by the abstract-only read, which is a separate axis.

## Follow-up

- **Relevance: 4** — the purpose/mechanism decomposition is essentially a
  hand-built, retrieval-oriented version of what
  [[abstract-then-reinstantiate]] asks the model to do internally: strip a
  source to its relational mechanism, then map it onto a target. That makes
  it strong prior art for the H2 integrator, and its schema is a ready-made
  **rubric for the [[transfer-depth-ladder]]** — "did the output transfer the
  *mechanism* or only the *background*?" is precisely the ladder's question,
  and SOLVENT supplies validated category definitions for it. **Action
  item:** obtain the full text and extract the annotation guidelines
  verbatim; they are likely directly reusable as judge instructions.
