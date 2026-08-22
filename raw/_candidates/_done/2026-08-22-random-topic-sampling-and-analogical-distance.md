---
kind: candidates
topic: "how to sample a random foreign discipline and how far the analogical source should be from the target problem"
discovered: 2026-08-22
source: discover
n_requested: 12
n_returned: 12
---

## 1. Directed Diversity: Leveraging Language Embedding Distances for Collective Creativity in Crowd Ideation

- url: https://arxiv.org/pdf/2101.06030
- type: paper
- summary: Introduces "directed diversity" — using text-embedding distances to deliberately steer AI-generated creative prompts to a controllable distance from a seed idea, and shows it broadens the range of human ideation outcomes.
- reason: This is the closest existing operationalization of "sample a topic at cosine distance d from the problem" — directly actionable for sub-question (b) integration mechanics.

## 2. The Meaning of "Near" and "Far": The Impact of Structuring Design Databases and the Effect of Distance of Analogy on Design Output (Fu, Chan, Cagan, Kotovsky, Schunn, Wood)

- url: https://www.researchgate.net/publication/229432436_The_Meaning_of_Near_and_Far_The_Impact_of_Structuring_Design_Databases_and_the_Effect_of_Distance_of_Analogy_on_Design_Output
- type: paper
- summary: Best-paper-award study (ASME DTM 2012 / J. Mech. Des. 135(2), 021007, 2013) that builds an LSA + Bayesian structural-form clustering of patents to operationally define "near" vs. "far" analogical distance, then tests its effect on design output novelty and quality.
- reason: The canonical primary source on optimal analogical distance named explicitly in the brief; gives a concrete method (structured similarity clustering) for defining "how far" a source discipline is from a target problem.

## 3. On the Benefits and Pitfalls of Analogies for Innovative Design: Ideation Performance Based on Analogical Distance, Commonness, and Modality of Examples (Chan, Fu, Schunn, Cagan, Wood, Kotovsky)

- url: https://doi.org/10.1115/1.4004396
- type: paper
- summary: J. Mech. Des. 133(8), 081004 (2011). Experimentally varies analogical distance, commonness, and presentation modality of design examples and measures effects on ideation quantity, quality, novelty, and fixation risk.
- reason: Companion/foundational paper to #2 from the same Chan & Schunn line of work explicitly requested in the brief; gives the empirical basis for "far but not too far."

## 4. Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions

- url: https://arxiv.org/pdf/2601.05414
- type: paper
- summary: Systematic evaluation showing LLMs achieve near-zero pass rates on statistical-validity tests for random-number and random-choice generation, both in batch and independent-request settings, and concludes current LLMs lack a functional internal sampler.
- reason: Directly and recently establishes that LLM "pick a random X" is not uniform, which is the load-bearing justification for routing topic selection through an external randomness source rather than asking the model to self-sample.

## 5. Deterministic or Probabilistic? The Psychology of LLMs as Random Number Generators

- url: https://arxiv.org/pdf/2502.19965
- type: paper
- summary: Large-scale (75,600-call, 6-model) study finding LLMs systematically favor specific numbers (e.g., 7, 37, 73) when asked to "pick randomly," mirroring human cognitive biases baked into training data rather than producing uniform output.
- reason: Complements #4 with a psychology-of-bias framing and mechanism (training-data-inherited human number preferences) — useful for explaining *why* LLM self-sampling of a "random discipline" would likely be similarly skewed.

## 6. Atypical Combinations and Scientific Impact (Uzzi, Mukherjee, Stringer, Jones)

- url: https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/science-2013-uzzi-468-72.pdf
- type: paper
- summary: Science (2013), analyzing 17.9M papers, finds the highest-impact science is built on conventional combinations of prior work with an "intrusion" of atypical, unexpected combinations — pure novelty and pure convention both underperform.
- reason: Large-scale empirical evidence for the "far but not too far" principle at corpus scale, named explicitly in the brief; supports a calibration target for how atypical/foreign the sampled discipline should be.

## 7. Structure-Mapping: A Theoretical Framework for Analogy (Gentner, 1983)

- url: https://courses.csail.mit.edu/6.803/pdf/gentner.pdf
- type: paper
- summary: Foundational cognitive-science paper proposing that successful analogy transfers relational structure (systematic, connected relations) between domains rather than surface-level object attributes.
- reason: The theoretical backbone for *why* distance/foreignness alone isn't sufficient — a sampled foreign discipline only improves an LLM's output if the integration step surfaces relational, not superficial, structure; essential for designing sub-question (b).

## 8. OpenAlex: A Fully-Open Index of Scholarly Works, Authors, Venues, Institutions, and Concepts

- url: https://arxiv.org/pdf/2205.01833
- type: paper
- summary: Describes OpenAlex's open, hierarchical Concepts/Topics classification (domain > field > subfield > topic, ~4500 topics) covering all of scholarship, built from and mappable onto other taxonomies.
- reason: A concrete, free, machine-readable, near-uniform sampling frame candidate for "sample a random foreign discipline" — more tractable than Wikipedia's category graph and more comprehensive than MSC/ACM CCS/arXiv categories alone.

## 9. A Random Walk Sampling on Knowledge Graphs for Semantic-Oriented Statistical Tasks

- url: https://www.sciencedirect.com/science/article/abs/pii/S0169023X22000295
- type: paper
- summary: Proposes a random-walk sampling method over knowledge graphs designed to preserve semantic/statistical structure of the source graph, rather than drifting into noise as naive random walks do.
- reason: Directly addresses the "random walks on knowledge graphs" sourcing strategy named in the brief, and specifically tackles the failure mode (drift to weakly-related/incoherent nodes) that a naive walk-based topic sampler would hit.

## 10. The Influence of Exposure to Randomness on Lateral Thinking in Divergent, Convergent, and Creative Search

- url: https://www.sciencedirect.com/science/article/abs/pii/S0010027721003607
- type: paper
- summary: Pre-registered study testing whether exposure to randomly-selected Wikipedia articles (modeled on Brian Eno's Oblique Strategies) improves human performance on divergent, convergent, and creative search tasks by derailing habitual trains of thought.
- reason: Direct empirical test of "random foreign stimulus improves problem solving," using Wikipedia-random-article as the randomness source named in the brief — human-subject evidence worth checking for transfer to LLM-assisted problem solving.

## 11. Conceptual Integration Networks (Fauconnier & Turner, 1998)

- url: https://markturner.org/cin.web/cin.html
- type: paper
- summary: Cognitive Science 22(2), 133–187. Lays out conceptual blending theory: two input mental spaces plus a generic space combine into a blended space with emergent structure not present in either input.
- reason: Named in the brief; offers a distinct mechanism (blending, with emergent structure) from Gentner's structure-mapping (alignment/transfer) for how sub-question (b)'s integration step could actually combine a foreign topic with the target problem.

## 12. The Act of Creation (Koestler, 1964) — bisociation

- url: https://en.wikipedia.org/wiki/The_Act_of_Creation
- type: post
- summary: Koestler's seminal theory that creative acts across humor, science, and art share a common pattern — "bisociation" — the collision/combination of two previously unrelated frames of reference into one new matrix of meaning.
- reason: Seminal, load-bearing older work naming the phenomenon this whole project operationalizes (deliberately colliding a foreign frame with a target problem); the conceptual ancestor of both Gentner's and Fauconnier & Turner's later formal theories.

## Disposition (curated 2026-08-22)

- INGESTED: 1. Directed Diversity: Leveraging Language Embedding Distances for Collective Creativity in Crowd Ideation — `literature/papers/cox2021directed.md`
- INGESTED: 2. The Meaning of "Near" and "Far": The Impact of Structuring Design Databases and the Effect of Distance of Analogy on Design Output (Fu, Chan, Cagan, Kotovsky, Schunn, Wood) — `literature/papers/fu2013meaning.md`
- INGESTED: 3. On the Benefits and Pitfalls of Analogies for Innovative Design: Ideation Performance Based on Analogical Distance, Commonness, and Modality of Examples (Chan, Fu, Schunn, Cagan, Wood, Kotovsky) — `literature/papers/chan2011benefits.md`
- INGESTED: 4. Large Language Models Are Bad Dice Players: LLMs Struggle to Generate Random Numbers from Statistical Distributions — `literature/papers/zhao2026large.md`
- INGESTED: 5. Deterministic or Probabilistic? The Psychology of LLMs as Random Number Generators — `literature/papers/coronadoblazquez2025deterministic.md`
- INGESTED: 6. Atypical Combinations and Scientific Impact (Uzzi, Mukherjee, Stringer, Jones) — `literature/papers/uzzi2013atypical.md`
- INGESTED: 7. Structure-Mapping: A Theoretical Framework for Analogy (Gentner, 1983) — `literature/papers/gentner1983structuremapping.md`
- INGESTED: 8. OpenAlex: A Fully-Open Index of Scholarly Works, Authors, Venues, Institutions, and Concepts — `literature/papers/priem2022openalex.md`
- DECLINED: 9. A Random Walk Sampling on Knowledge Graphs for Semantic-Oriented Statistical Tasks — declined — off the chosen design path. `xpol` samples a flat/stratified OpenAlex topic frame (see priem2022openalex), not knowledge-graph walks, so the drift failure mode this paper fixes does not arise. Also paywalled (Elsevier, not OA). Revisit only if the frame changes to a graph walk.
- INGESTED: 10. The Influence of Exposure to Randomness on Lateral Thinking in Divergent, Convergent, and Creative Search — `literature/papers/malthouse2021influence.md`
- INGESTED: 11. Conceptual Integration Networks (Fauconnier & Turner, 1998) — `literature/papers/fauconnier1998conceptual.md`
- DECLINED: 12. The Act of Creation (Koestler, 1964) — bisociation — declined — tertiary source. The URL is the Wikipedia article *about* Koestler's 1964 book, not the book or any primary text. Bisociation as a mechanism is already covered by fauconnier1998conceptual and gentner1983structuremapping, both primary and both ingested.

### Re-curation 2026-08-22 (deferral pass)

The first pass deferred 6 of 12 items. This pass resolved all 6 — zero open
items remain.

- **Ingested (4):** `chan2011benefits`, `priem2022openalex`,
  `malthouse2021influence`, `fauconnier1998conceptual`.
- **Declined (2):** #9 *Random Walk Sampling on Knowledge Graphs* — off the
  chosen design path (`xpol` samples a stratified OpenAlex topic frame, not
  graph walks) and paywalled; #12 *The Act of Creation* — the URL is the
  Wikipedia article *about* Koestler's book, a tertiary source, and
  bisociation is already covered by two ingested primary sources.

**⚠️ Highlight — #10 (Malthouse et al., _Cognition_) is a NULL RESULT and the
triage summary mischaracterized it.** The triage described it as a "direct
empirical test of 'random foreign stimulus improves problem solving'" without
noting the direction. The actual finding: across 592 pre-registered
participants and three tasks, random Wikipedia stimuli produced **no
improvement and often significant impairment**, with a Bayesian meta-analysis
giving strong support for the null. The authors conclude random stimuli must
be "sufficiently task-related or 'optimally random'" to help.

This is disconfirming for the naive version of the project's premise (that a
foreign seed helps by mere juxtaposition) and is the strongest argument in
the corpus that the *integration* step, not the *injection*, is where the
value must come from. It also independently restates H3's useful-distance
band from a human-subjects direction. It should be cited in
`docs/research-plan.md` as the disconfirming prior, and the "raw seed, no
integration" condition should become an explicit control arm in H2.

- **Fetch notes:** #3 (Chan et al. 2011) is paywalled with no abstract
  available anywhere — its note is explicitly marked inference-only, matching
  the existing `fu2013meaning` precedent, and both should be pulled together
  via institutional access. #11 (Fauconnier & Turner) — the markturner.org
  URL serves only a landing stub, so its note is flagged as written from
  established secondary understanding.

**Final totals: ingested=4, declined=2, already-in-graph=6.**
