# Project: llm-cross-pollination

Short orientation only. User-level `~/.claude/CLAUDE.md` holds the durable
principles; this file refines them for this project.

## What this project is about

Strategies for forcing **cross-pollination** in LLM-assisted STEM work: when
an LLM helps with a problem it defaults to the home field's canonical
toolkit; we want a reproducible procedure that (a) picks a genuinely random
*foreign* topic and (b) integrates it into the query so that mechanisms —
not just vocabulary — transfer. End product: a reusable Claude Code skill.
Plan + hypotheses: `docs/research-plan.md`. Scope decision: `docs/decisions/0001-*`.

## Layout (see user CLAUDE.md for the full rationale)

- `raw/` — immutable source material. Read only.
- `literature/` — processed notes on papers, repos, posts.
- `concepts/` — atomic ideas. Promote to `mocs/` when ≥5 cluster.
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs.
- `docs/decisions/` — lightweight ADRs.
- `journal/` — daily session files (hook-written).
- `_meta/` — index, log, templates.

## Scoped rules

Detailed conventions live in `.claude/rules/` and are auto-loaded when you
touch matching paths:

@.claude/rules/experiments.md
@.claude/rules/notebooks.md
@.claude/rules/data.md

Framework rules load here (per-project, not globally — they only cost
context where they can apply):

@~/claude-system/claude/rules/evaluation.md
@~/claude-system/claude/rules/agency.md

## Budget & compute

Autonomous runs read `budget.yaml` at this project's root for hard
ceilings (wall time, tokens, disk) and model roles (ideator vs
implementer). Before proposing anything with non-trivial resource
demands — multi-hour training, large downloads, many seeds — read
`budget.yaml` and make sure the ask fits under the remaining headroom.
If it doesn't fit, say so in the proposal's `risks:` and either scope
down or explicitly flag the need to raise a ceiling.

@budget.yaml

## Project-specific facts

- Primary language: Python (sampler + evaluation harness); prompts as Markdown.
- LLM access: `claude -p` on the subscription (see user memory) — never a raw
  API key. Pin `--model` in any unattended job.
- Randomness is **external** to the LLM (OS RNG, seeded, logged in
  `config.yaml`). Never ask the model to "pick a random field" except as the
  baseline being measured.
- Evaluation pairs novelty with usefulness (`concepts/novelty-usefulness-tradeoff.md`);
  novelty alone is gameable.
- Environment: managed by `uv`; run `make env` to sync.
- Data: tracked by DVC. Large artifacts on SN850X via `~/projects/`.

## Housekeeping

- End sessions with `/wrap`. The SessionEnd hook backstops this.
- Use `/new-experiment <slug>` — don't hand-roll experiment folders.
- Run `/lint` weekly.
