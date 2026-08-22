---
kind: candidates
topic: "LLM output homogenization and measuring idea diversity/novelty"
discovered: 2026-08-22
source: discover
n_requested: 12
n_returned: 12
---

## 1. Generative AI enhances individual creativity but reduces the collective diversity of novel content

- url: https://www.science.org/doi/10.1126/sciadv.adn5290
- type: paper
- summary: Doshi & Hauser (Science Advances, 2024) run an online short-story experiment showing LLM-generated ideas raise individual writers' creativity scores but make stories across writers more similar to each other, creating a social dilemma between individual and collective novelty.
- reason: The seminal empirical result motivating this project — direct causal evidence that defaulting to LLM suggestions narrows the collective idea space, which is exactly the failure mode cross-pollination is meant to counteract.

## 2. Homogenization Effects of Large Language Models on Human Creative Ideation

- url: https://arxiv.org/abs/2402.01536
- type: paper
- summary: Anderson, Shah & Kreminski (C&C 2024) find in a 36-participant study that ChatGPT users produce more detailed ideas individually but less semantically distinct ideas across users than users of an alternative creativity-support tool, while feeling less ownership of the output.
- reason: Named directly in the brief; establishes the "homogenization" term of art and a measurable between-subjects semantic-distinctness effect that a cross-pollination intervention could be benchmarked against.

## 3. Does Writing with Language Models Reduce Content Diversity?

- url: https://arxiv.org/abs/2309.05196
- type: paper
- summary: Padmakumar & He (ICLR 2024) show in a controlled co-writing study that InstructGPT (but not base GPT-3) assistance significantly increases similarity between different authors' essays and reduces lexical/content diversity, an effect traced to the model's own contributed text rather than the human-written portions.
- reason: Named directly in the brief; isolates instruction-tuning/RLHF as the mechanism behind homogenization, which is a specific lever (prompt/query design) this project's sub-question (b) needs to reckon with.

## 4. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity

- url: https://arxiv.org/abs/2510.01171
- type: paper
- summary: Zhang, Yu, Chong et al. (2025) trace mode collapse to "typicality bias" baked into RLHF preference data — annotators systematically prefer familiar text — and show a training-free prompting method (asking the model to verbalize a distribution over responses with probabilities) substantially restores output diversity.
- reason: Gives a mechanistic account of *why* LLMs default to the home field's standard methods, and a concrete, cheap prompting-level intervention directly relevant to sub-question (b) — integrating foreign framing into a prompt to actually change the output.

## 5. We're Different, We're the Same: Creative Homogeneity Across LLMs

- url: https://arxiv.org/abs/2501.19361
- type: paper
- summary: Compares creative outputs across multiple LLM families and finds a shared homogeneity signature — different models tend to converge on similar ideas even when their individual outputs look varied — suggesting homogenization is a cross-model property, not one vendor's quirk.
- reason: Tests whether homogenization is model-specific or systemic; relevant to whether "true random" foreign-topic injection (sub-question a) needs to fight a single model's bias or a broader industry-wide convergence.

## 6. Diverse AI Personas Can Mitigate the Homogenization Effect in Human-AI Collaborative Ideation

- url: https://arxiv.org/abs/2504.13868
- type: paper
- summary: Proposes assigning an LLM distinct personas during ideation sessions and finds this measurably reduces the homogenization effect documented in prior human-AI creativity studies, restoring more of the semantic spread seen in unassisted human ideation.
- reason: A direct prior attempt at the project's core intervention question (b) — using a structured perturbation, personas rather than foreign-discipline injection, to counteract homogenization — useful as a baseline/contrast method.

## 7. Naming unrelated words predicts creativity (the Divergent Association Task)

- url: https://www.pnas.org/doi/10.1073/pnas.2022340118
- type: paper
- summary: Olson et al. (PNAS, 2021) introduce the Divergent Association Task — list 10 nouns as semantically distant from each other as possible, scored by mean pairwise GloVe embedding distance — and validate it against established creativity batteries across nearly 9,000 participants in 98 countries.
- reason: Seminal, load-bearing metric: a cheap, automatable, embedding-based novelty score with a two-decade validation pedigree that this project can adopt directly as an experiment metric for "how foreign is the sampled topic / how novel is the resulting output."

## 8. Probing the Creativity of Large Language Models: Can models produce divergent semantic association?

- url: https://arxiv.org/abs/2310.11158
- type: paper
- summary: Chen & Ding apply the Divergent Association Task to LLMs directly, finding GPT-4 and similar models can exceed average human DAT scores, though follow-up work (see below) questions whether DAT alone validly ranks model creativity.
- reason: First application of DAT as an LLM evaluation metric rather than a human psychometric — the direct precedent for using DAT-style scoring in an LLM cross-pollination experiment.

## 9. Death of the Novel(ty): Beyond n-Gram Novelty as a Metric for Textual Creativity

- url: https://arxiv.org/abs/2509.22641
- type: paper
- summary: Saakyan, Kim, Muresan & Chakrabarty (ICLR 2026) collect 8,618 expert creativity annotations and show n-gram novelty (the basis of the widely used "Creativity Index") correlates only weakly with judged creativity — ~91% of top-quartile novel n-grams are not judged creative, and novelty even trades off against pragmatic sense in open-source LLM text — then show LLM-as-judge ratings track expert judgment better.
- reason: A load-bearing methods caveat for this project's own metric design: warns against relying on n-gram/lexical-novelty scores alone as the outcome measure for a cross-pollination experiment and points toward LLM-as-judge as a better-validated alternative.

## 10. NoveltyBench: Evaluating Language Models for Humanlike Diversity

- url: https://arxiv.org/abs/2504.05228
- type: paper
- summary: Zhang, Diddee, Holm et al. (2025) build a benchmark of prompts curated to elicit multiple valid distinct answers and score 20 leading LLMs on whether they actually produce that diversity; finds current models fall well short of human writers, and larger models within a family are sometimes less diverse than smaller ones.
- reason: A ready-made, general-purpose diversity benchmark and scoring harness the project could reuse or adapt as an outcome metric, plus an empirical baseline (model scale does not fix homogenization) relevant to framing sub-question (a).

## 11. Automated Creativity Evaluation of Language Models Across Open-Ended Tasks

- url: https://arxiv.org/abs/2606.11762
- type: paper
- summary: Proposes evaluating divergent creativity via semantic entropy (a reference-free novelty/diversity metric over embeddings) and convergent creativity via a retrieval-based multi-agent LLM judge, validating both against human annotations and prior baseline diversity measures.
- reason: Offers a two-sided metric design (semantic-entropy for spread + LLM-judge for quality/appropriateness) that maps well onto measuring whether a cross-pollinated output is both novel and actually good — the two things this project needs to jointly optimize.

## 12. Are LLMs becoming similarly creative? Evidence from three years of models

- url: https://arxiv.org/abs/2608.19437
- type: paper
- summary: Tracks creative-output similarity across LLM releases over roughly three years, examining whether successive model generations are converging toward more similar creative outputs over time rather than diversifying.
- reason: Most recent (2026) longitudinal data point on the homogenization trend itself, useful for framing the project's motivation ("is the problem getting worse") and for methodology on measuring cross-model/cross-time idea similarity.

## Disposition (curated 2026-08-22)

- INGESTED: 1. Generative AI enhances individual creativity but reduces the collective diversity of novel content — `literature/papers/doshi2024generative.md`
- INGESTED: 2. Homogenization Effects of Large Language Models on Human Creative Ideation — `literature/papers/anderson2024homogenization.md`
- DEFERRED: 3. Does Writing with Language Models Reduce Content Diversity? — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- INGESTED: 4. Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity — `literature/papers/zhang2025verbalized.md`
- DEFERRED: 5. We're Different, We're the Same: Creative Homogeneity Across LLMs — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- DEFERRED: 6. Diverse AI Personas Can Mitigate the Homogenization Effect in Human-AI Collaborative Ideation — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- DEFERRED: 7. Naming unrelated words predicts creativity (the Divergent Association Task) — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- DEFERRED: 8. Probing the Creativity of Large Language Models: Can models produce divergent semantic association? — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- DEFERRED: 9. Death of the Novel(ty): Beyond n-Gram Novelty as a Metric for Textual Creativity — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- INGESTED: 10. NoveltyBench: Evaluating Language Models for Humanlike Diversity — `literature/papers/zhang2025noveltybench.md`
- DEFERRED: 11. Automated Creativity Evaluation of Language Models Across Open-Ended Tasks — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
- DEFERRED: 12. Are LLMs becoming similarly creative? Evidence from three years of models — deferred — secondary to the first ingest pass; re-curate after the H2 bake-off if the evaluation or prompting design needs it
