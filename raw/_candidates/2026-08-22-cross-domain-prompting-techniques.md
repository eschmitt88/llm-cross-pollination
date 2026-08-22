---
kind: candidates
topic: "prompting techniques that inject a foreign domain or analogy into an LLM query to produce cross-domain ideas"
discovered: 2026-08-22
source: discover
n_requested: 12
n_returned: 12
---

## 1. Large Language Models as Analogical Reasoners

- url: https://arxiv.org/abs/2310.01714
- type: paper
- summary: Yasunaga et al. (2023) introduce "analogical prompting," where the LLM self-generates relevant exemplars or abstracted knowledge in-context before solving a target problem, instead of relying on retrieved or hand-labeled exemplars.
- reason: This is the seminal prompting-technique paper the project topic explicitly names as its (a)/(b) reference point — self-generated analogical exemplars is a direct mechanism for "how to integrate a foreign idea into the prompt so it changes the output," even though the analogies here are same-domain reasoning analogies rather than cross-domain ones; it's the baseline the project's own techniques should be compared against.

## 2. Accelerating Innovation Through Analogy Mining

- url: https://arxiv.org/abs/1706.05585
- type: paper
- summary: Hope, Chan, Kittur & Shahaf (2017) learn "problem schema" (purpose/mechanism) vector representations from crowdsourced annotations + RNNs to retrieve structurally analogous products across domains, and show retrieved cross-domain analogies increase human ideation creativity versus IR baselines.
- reason: Seminal pre-LLM foundation for sub-question (a) — a concrete, load-bearing method for *selecting* a genuinely structurally-distant (not just surface-similar) foreign analog, which any "true randomness" or "true distance" discipline-selection method in this project should be benchmarked against.

## 3. SOLVENT: A Mixed Initiative System for Finding Analogies between Research Papers

- url: https://dl.acm.org/doi/10.1145/3274300
- type: paper
- summary: Chan, Chang, Hope, Shahaf & Kittur (CSCW 2018) build a mixed-initiative system where humans annotate papers' background/purpose/mechanism/findings and a computational model uses these schemas to surface cross-domain analogies that beat IR baselines and are judged useful by experts.
- reason: Explicitly named in the brief; extends #2 into an interactive schema-based retrieval architecture — directly relevant to sub-question (b) (how a retrieved foreign idea gets structured before it's handed to a solver), and is a natural precursor to today's LLM-based idea-retrieval systems (#7–#9).

## 4. AutoTRIZ: Automating Engineering Innovation with TRIZ and Large Language Models

- url: https://arxiv.org/abs/2403.13002
- type: paper
- summary: Jiang, Li, Qian, Zhang & Luo (2024) build an LLM-driven pipeline that automates the TRIZ inventive-problem-solving workflow — contradiction identification, mapping to the 40 inventive principles, solution generation — producing an interpretable ideation report from a plain problem statement.
- reason: TRIZ's 40 inventive principles are themselves a curated cross-domain analogy library (patterns abstracted from patents across all of engineering); this paper is the clearest, most-cited example of an LLM system operationalizing "inject a structured foreign-domain principle into the query" and is a strong candidate mechanism for sub-question (b).

## 5. IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs

- url: https://arxiv.org/abs/2606.00875
- type: paper
- summary: Carichon, Sharma, Girard, Rampa & Farnadi (2026) propose an evaluation framework specifically for prompting techniques designed to break LLM "fixation" (over-reliance on the most obvious/default approach) and measure whether defixation prompts actually broaden the solution space.
- reason: Closest primary source to the brief's "random-stimulus / Oblique-Strategies-style prompting with LLMs" ask — defixation is exactly the failure mode ("defaulting to the home field's standard methods") this project is about, and having an evaluation framework (not just a technique) is useful for the project's own eventual eval design.

## 6. Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

- url: https://arxiv.org/abs/2409.04109
- type: paper
- summary: Si, Yang & Hashimoto (2024) run the first head-to-head comparison of LLM-generated vs. expert-generated NLP research ideas, finding LLM ideas rated more novel but slightly less feasible, and surfacing limitations in LLM self-evaluation and idea diversity.
- reason: The rigorous human-evaluation bar this whole research area is measured against; establishes that novelty gains from LLM ideation are real but that diversity is a known weak point — directly motivates why deliberate cross-domain injection (rather than default LLM ideation) is needed.

## 7. SciMON: Scientific Inspiration Machines Optimized for Novelty

- url: https://arxiv.org/abs/2305.14259
- type: paper
- summary: Wang, Downey, Ji & Hope (2023/ACL 2024) retrieve "inspirations" (related problems + solutions) from a scientific literature knowledge graph and iteratively revise generated ideas against prior work until sufficient novelty is achieved.
- reason: A concrete architecture for sub-question (b) — retrieval-then-injection-then-iterate — and co-authored by Tom Hope, directly bridging the pre-LLM analogy-mining line (#2, #3) into an LLM-era system; requested by name in the brief.

## 8. Chain of Ideas: Revolutionizing Research via Novel Idea Development with LLM Agents

- url: https://arxiv.org/abs/2410.13185
- type: paper
- summary: Li et al. (2024) organize literature into chain/progression structures so an LLM agent can trace a research trend and propose the next novel idea, plus an idea-evaluation protocol aligned with human researcher preferences.
- reason: Requested by name; a contrasting design choice to Nova/SciMON — structures *within-field* progression rather than cross-domain injection, useful as a negative/contrast case for what this project is explicitly trying to avoid (defaulting to home-field trajectory).

## 9. Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas

- url: https://arxiv.org/abs/2410.14255
- type: paper
- summary: Hu et al. (2024) use iterative, planned external-knowledge retrieval to broaden LLM ideation, reporting 3.4x more unique novel ideas than baseline prompting in automated and human evaluation.
- reason: Requested by name; the strongest recent quantitative evidence that *deliberately planned* (vs. default single-shot) knowledge injection measurably increases idea diversity — a directly load-bearing result for sub-question (b)'s "does it actually change the output" question.

## 10. Enhancing Design Concept Diversity: Multi-Persona Prompting Strategies for Large Language Models

- url: https://www.cambridge.org/core/journals/design-science/article/enhancing-design-concept-diversity-multipersona-prompting-strategies-for-large-language-models/3B346E253508337A4EE899499BE49D9B
- type: paper
- summary: Feng, Hélie & Panchal (Design Science, 2025) test parallel, collective, and sequential multi-persona prompting strategies (e.g., "act as a biologist / act as an architect") and measure their effect on the diversity of generated design concepts.
- reason: Directly answers the brief's "role/persona prompting effects on diversity" ask with a controlled comparison of persona-injection *strategies* — relevant to sub-question (b) as a cheap, prompt-only alternative to full retrieval systems for injecting a foreign disciplinary lens.

## 11. PopBlends: Strategies for Conceptual Blending with Large Language Models

- url: https://arxiv.org/abs/2111.04920
- type: paper
- summary: Wang, Petridis, Kwon, Ma & Chilton (UIST 2023) use LLMs plus knowledge extraction to find connecting concepts between two disparate input domains, via a divergent-then-convergent generation pipeline, to produce conceptual blends.
- reason: The clearest primary source on LLM-based conceptual blending explicitly requested in the brief; its divergent/convergent connecting-concept pipeline is a reusable pattern for the project's own sub-question (b) prompt design, even though its target domain (pop-culture references) differs from STEM problem solving.

## 12. Fluid Transformers and Creative Analogies: Exploring Large Language Models' Capacity for Augmenting Cross-Domain Analogical Creativity

- url: https://arxiv.org/abs/2302.12832
- type: paper
- summary: Ding, Srinivasan, MacNeil & Chan (C&C 2023) systematically test whether LLMs can help humans generate useful cross-domain analogies for creative problem reformulation, finding LLM-generated analogies frequently judged helpful, alongside identified risks (e.g., low-quality or harmful suggestions).
- reason: The most direct empirical test of the project's core premise — that LLM-mediated cross-domain analogy measurably helps creative/problem-reformulation tasks — and co-authored by Joel Chan, again bridging the classic analogy-mining line into an LLM evaluation; strong candidate for the project's foundational literature note.
