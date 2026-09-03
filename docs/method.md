---
kind: method
name: cross-pollination-method
status: v0.1
added: "2026-08-22"
updated: "2026-09-03"
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

## 4. Which strategy wins — [H2 ✓, H6 ✓(directional)]

Same 18 seeds (3 per dev problem), four strategies, Opus 5 judge
(`experiments/2026-08-22-h2-integration-bakeoff/`):

| strategy | transfer depth (0–4) | ≥ mechanism | usefulness | paired vs naive |
|---|---|---|---|---|
| naive "incorporate ideas from X" | 2.12 | 41% | 2.24 | — |
| persona "you are an X expert" | 2.29 | 41% | 2.24 | 5 wins / 4 losses (n.s.) |
| abstract-reinstantiate | 2.94 | 76% | 2.18 | 11 / 1, p=0.006 |
| **abstract-reinstantiate-brief** | **3.29** | **88%** | 2.29 | **13 / 1, p=0.002** |

Three things the numbers say:

1. **Structure beats speaker.** Forcing abstraction + correspondence
   tables is what transfers a mechanism; giving the model a persona does
   nothing (the popular move, and it is worthless here).
2. **Problem-blind briefs help** (+0.35 depth, 7/1 over the joint-context
   version, p=0.07): a context that has seen the problem retrieves only the
   parts of the seed that already look like the problem.
3. **Transfer ≠ novelty.** Usefulness is flat across every arm (~2.2/4,
   same as a no-seed "be unconventional" prompt), and the judge marks 94%
   of proposals — including the method-level ones — as reachable by the
   home field: the seed usually leads, by a foreign path, to a method the
   field already has (CVaR → distributionally robust optimisation; plant
   stress priming → curriculum/adaptive regularisation). Only 4 of 72
   seeded outputs were judged both foreign *and* useful. Hard-constraint
   physical design problems (fixed shape, fixed material) transferred
   worst; modelling/algorithm problems best.

So the method as it stands reliably produces **foreign derivations of
mostly-known methods**, at a 5–10% rate of genuinely new-to-the-field
ideas, with the user as the filter.

**Accepted framing (user, 2026-09-03): a low per-seed hit rate is expected
and fine.** This matches the prior literature — far-field inspiration hits
rarely everywhere ([[fu2013meaning]]; [[uzzi2013atypical]]: atypical
combinations are rare tails on conventional cores, and that tail is where
impact lives) — and it reframes what to optimise: not hit rate per seed but
**cost per shot and quality of the filter**. Seeds are free and generations
are cheap; the scarce resource is user attention. Consequences: k goes up
rather than the band getting cleverer (H5 is the priority experiment), the
judge's job shifts from scoring to *pre-filtering* what reaches the user,
and judge calibration becomes the gating risk — with a rare-hit regime, a
judge that false-negatives the hits destroys the whole value. Rediscoveries
are not waste either: a correspondence table onto a method you did not know
is a tutorial for it.

Side cost: 4/72 seeded generations were refused outright by the API's
bio-safety classifier because the *seed* was medical/toxicological
(HIV/AIDS, pesticide toxicity). The sampler resamples on refusal.

## 5. Recommended procedure (v0.1)

1. Write the problem in 3–8 sentences, including what has been tried and
   why it failed — the abstraction step needs that.
2. `xpol sample -k 5 --problem @problem.txt` → five seeds (not three:
   the foreign-and-useful rate is ~6% per seed), home field excluded,
   mid-far band. Record the printed RNG seed. If a seed is medical or
   toxicological and you are on a model with a bio classifier, resample.
3. For each seed, in a **fresh context that has not seen the problem**,
   run `prompts/brief.md` → a one-page mechanisms brief. Then
   `xpol prompt --problem @problem.txt --seed <rng> --template
   abstract-reinstantiate-brief` with the brief, in the problem context.
4. Read the *correspondence tables and critiques* first. Expect most
   proposals to land on something your field already has — that is still
   the fastest way to learn about a method you did not know. Keep the one
   whose critique names a cheap experiment; discard the rest without guilt.
5. Do not use persona prompting for this; it measured as no better than
   pasting the seed's name.

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
