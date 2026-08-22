---
kind: method
name: cross-pollination-method
status: draft            # draft until H2 fills §4
added: "2026-08-22"
updated: "2026-08-22"
---

# The cross-pollination method (v0.1)

How to make an LLM borrow a *mechanism* from a randomly chosen foreign field
when working on a STEM problem. Two halves: **choosing** the seed (a
sampler the model does not control) and **integrating** it (a prompt
structure that forces relational mapping rather than decoration). Evidence
status is marked per claim: **[H1 ✓]** measured in this repo,
**[lit]** supported by the ingested literature, **[untested]** design
choice awaiting its experiment.

## 1. Why the model cannot pick its own seed — [H1 ✓]

Asked, in 100–150 independent fresh-context calls, to "name one randomly
chosen academic research topic, uniformly at random across all of science
and scholarship":

| model / prompt | duplicate answers | fields covered (of 26) | modal answer |
|---|---|---|---|
| Sonnet 5, specific-subfield prompt | **71%** | 8 | "ethnomusicology of Andean panpipe traditions" ×33 |
| Haiku 4.5, specific-subfield prompt | 11% | 17 | dendrochronology ×5 |
| Haiku 4.5, "random scientific discipline" | 79% | 10 | mycology ×41 |
| Haiku 4.5, "a field far from ML to borrow from" | 79% | 10 | forestry ×32, ecology ×28 |
| `xpol` sampler (reference) | 0% | 25–26 | — |

The realistic user prompt — "pick a field far from mine" — is the worst
case: the same two answers 60% of the time. The more capable model
collapsed harder. Details: `experiments/2026-08-22-h1-llm-random-topic-skew/`.
This agrees with the LLM-randomness literature ([[zhao2026large]]: 0/11
models pass distributional tests; [[coronadoblazquez2025deterministic]]:
models narrate a *script about randomness* rather than sample) and with the
homogenization literature ([[doshi2024generative]], [[anderson2024homogenization]]).

Consequence: randomness must be **external** to the model —
[[external-randomness]].

## 2. Choosing the seed — the `xpol` sampler

`xpol sample -k K [--level L] [--stratify S] [--problem TEXT] [--band lo,hi] [--seed N]`

| design choice | default | rationale | status |
|---|---|---|---|
| **Frame** = OpenAlex topics: 4 domains › 26 fields › 245 subfields › 4 516 topics › 45 154 keywords | `topic` | explicit finite population so "uniform" is defined and the model's picks can be scored against it; every topic has a description + keywords, so it is embeddable and self-describing in the prompt ([[sampling-frame]]) | built; frame has some mislabelled topics (OpenAlex noise) |
| **RNG** = OS entropy (`secrets`) or a logged integer seed | OS entropy | reproducible when you want it, never the model ([[external-randomness]]) | **[H1 ✓]** |
| **Stratification** = round-robin over strata, uniform within | `domain` | the frame is 35/33/19/14 % physical/social/health/life; unstratified draws over-sample physical sciences; stratifying gives 25/25/25/25 | built |
| **Granularity** = `domain`/`field`/`subfield`/`topic`/`keyword` | `topic` | `field` is too coarse to name a mechanism; `keyword` is noisy ("Leadership", "Social Welfare" appear as seeds); `topic` is the level at which OpenAlex writes a paragraph of description (H4 predicts method-level beats field-level — the `topic` description already lists mechanisms) | **[untested]** (H4) |
| **Home-field exclusion** = embed the problem, take its 10 nearest topics, exclude their majority field | on | a seed from the home field is not foreign | built; correct on all 6 dev problems |
| **Distance band** = cosine-distance percentile band between problem and topic embeddings (bge-small, CPU) | `0.5–0.9` when a problem is given | design-by-analogy literature finds a non-monotone "far but not too far" effect ([[fu2013meaning]], [[hope2017accelerating]], [[uzzi2013atypical]]); the band is a percentile so it is robust to the embedding model's compressed distance range; embedding distance is a *surface*-similarity proxy ([[structure-mapping]]) | **[untested]** — H3 will sweep it; `0.5–0.9` is a literature-informed prior, not a measured optimum |

What a seed carries into the prompt: name, taxonomy path, OpenAlex's
paragraph description, 6 keywords, and (if a problem was given) its
distance percentile.

## 3. Integrating the seed — prompt structure

Templates in `prompts/`. The candidate strategies, all run with the *same*
seeds in the H2 bake-off:

| template | what it does | theory |
|---|---|---|
| `naive` | "incorporate ideas from X" | baseline to beat |
| `persona` | "you are an expert in X; look at this problem" | multi-persona diversity work ([[anderson2024homogenization]] mitigation; Feng et al.) |
| `abstract-reinstantiate` | (1) restate the problem with no domain vocabulary — what is optimised, the contradiction, the invariant; (2) list 5–7 named mechanisms of X *without looking at the problem*; (3) build an explicit correspondence table per mechanism, discard word-only matches; (4) write the survivors out as a runnable method; (5) critique what is lost in translation | TRIZ's specific→generic→generic→specific loop ([[jiang2024autotriz]]) operationalising Gentner's systematicity principle ([[gentner1983structuremapping]]); see [[abstract-then-reinstantiate]] |
| `abstract-reinstantiate-brief` | as above, but step (2) is done by a *separate, problem-blind* call (`prompts/brief.md`) and the brief is injected | prevents the model from retrieving only the parts of X that already resemble the problem — [[seed-brief-isolation]] (H6) |

Judge rubric (`prompts/judge.md`): **transfer depth** 0–4 on the
[[transfer-depth-ladder]] (none / vocabulary / metaphor / mechanism /
method), **usefulness** 0–4, and a `home_field_default` flag (could the
field have produced this without the seed?). Generator and judge are
different models (Sonnet 5 / Opus 5) to dampen self-preference
([[zhang2025noveltybench]] on judge/metric pitfalls).

## 4. Which strategy wins — [H2 pending]

_Filled in from `experiments/2026-08-22-h2-integration-bakeoff/` when the
run completes._

## 5. Recommended procedure (v0.1)

1. Write the problem in 3–8 sentences, including what has been tried and
   why it failed — the abstraction step needs that.
2. `xpol sample -k 3 --problem @problem.txt` → three seeds, home field
   excluded, mid-far band. Record the printed RNG seed.
3. For each seed, `xpol prompt --problem @problem.txt --seed <rng>
   --template <winner from §4>` and run the rendered prompt.
4. Read the *critique* sections first: they tell you which of the three
   transfers is worth an experiment. Keep one; discard the rest without
   guilt — two-thirds of random seeds are expected to be duds; the sampler
   is cheap, the judgment is yours.

## 6. Known limitations

- OpenAlex's taxonomy has mislabelled topics (a "Linguistic and Cultural
  Studies" topic sits under Plant Science). Harmless for randomness,
  confusing in a prompt; filter by eye.
- Embedding distance is surface similarity. A seed can be embedding-far
  and structurally near (good) or embedding-mid and useless (common). The
  band shapes the draw; it does not guarantee transfer.
- The judge is an LLM and may share the homogenization bias it grades —
  usefulness scores in particular should be spot-checked by a human before
  being trusted ([[novelty-usefulness-tradeoff]]).
- Only the dev problem set has been used; `data/problems/heldout.yaml`
  is reserved for a final pass.
