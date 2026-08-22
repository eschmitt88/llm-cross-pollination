---
name: cross-pollinate
description: /cross-pollinate <problem-or-@file> [--k N] [--band lo,hi] [--level topic|subfield|keyword] [--template T]. Draws N genuinely random foreign topics (OpenAlex frame, OS entropy, home field excluded, mid-far distance band) with the xpol sampler and works each through an abstract→retrieve→map→re-instantiate→critique prompt so that a mechanism — not vocabulary — transfers into a STEM problem. Use when stuck, when the field's standard toolkit has already failed, or when the user asks for ideas "from outside the field".
---

# cross-pollinate

Force cross-disciplinary transfer into a STEM problem. The model must NOT
choose the foreign topic itself (measured: Sonnet 5 gives the same "random"
topic 33 times in 100 calls — see llm-cross-pollination H1). The sampler
chooses; the model integrates.

## Arguments

- `<problem>` — free text, or `@path` to a file. Should include what has
  been tried and why it failed; the abstraction step needs that.
- `--k N` — number of seeds (default 3).
- `--band lo,hi` — distance-percentile band from the problem (default
  `0.5,0.9`, "far but not too far").
- `--level` — `topic` (default), `subfield`, or `keyword`.
- `--template` — `abstract-reinstantiate` (default) or
  `abstract-reinstantiate-brief` (problem-blind brief first, then map).

## Steps

1. **Sample.** From the project root of llm-cross-pollination (or wherever
   `xpol` is installed):
   ```sh
   uv run xpol sample -k <N> --problem @problem.txt --band <lo,hi> --level <level> --json
   ```
   Record the printed RNG seed in whatever log the calling project keeps —
   it reproduces the draw.
2. **Render** one prompt per seed:
   ```sh
   uv run xpol prompt --problem @problem.txt --seed <rng> -k <N> --template <template>
   ```
   For `abstract-reinstantiate-brief`, first run `prompts/brief.md` for
   the seed in a **fresh context** (a separate `claude -p` call, or a
   subagent that has not seen the problem) and pass the brief in.
3. **Run** each rendered prompt — as a subagent each, so the seeds do not
   contaminate one another.
4. **Select.** Read the critique sections. Report to the user: for each
   seed, the mechanism named, the transfer-depth rung you would assign
   (0 none · 1 vocabulary · 2 metaphor · 3 mechanism · 4 method), and the
   cheapest experiment that would test it. Recommend one; say plainly when
   none transferred — two-thirds of random seeds are expected to be duds.

## What this skill does NOT do

- Does not let the model pick the seed, ever — not even "one more, you
  choose". That is the failure mode the skill exists to avoid.
- Does not claim usefulness: the judgment is the user's. It surfaces
  candidate mechanisms with explicit correspondence tables so the user can
  reject them fast.

## Install

```sh
ln -s ~/projects/research/llm-cross-pollination/skill/cross-pollinate ~/.claude/skills/cross-pollinate
```
