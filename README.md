# llm-cross-pollination

**How to seed an LLM with a random foreign discipline so STEM problem-solving borrows real mechanisms from other fields instead of defaulting to the home field's toolkit.**

📂 **[Browse this repo →](https://eschmitt88.github.io/llm-cross-pollination/)** —
interactive, always-live view of experiments, concepts, literature, and maps of
content. Served via GitHub Pages from `docs/index.html`; reads the live file
tree, no build step. _(Link is live once the repo is public and Pages is enabled
— `/new-project` does both by default.)_

## What this is

When an LLM helps with a STEM problem it reaches for the field's standard
methods — the mode of the training distribution conditioned on the domain.
This project studies how to *deliberately* pull in ideas from unrelated
fields (organic chemistry → neural-network training, say: protecting groups
→ layer freezing, retrosynthesis → backward goal decomposition, catalysis →
annealing the loss landscape). Two questions:

1. **Choosing the foreign topic.** How to sample a topic *truly* at random —
   from what population, at what granularity, at what conceptual distance from
   the problem — rather than letting the model "pick" (it won't pick uniformly).
2. **Integrating it into the query.** Which prompt structures turn a seed into
   transferable mechanisms rather than decorative vocabulary.

Success = a reproducible procedure, measured on a small STEM problem set for
novelty *and* usefulness, packaged as a Claude Code skill. The research plan
with hypotheses and phases is in [`docs/research-plan.md`](docs/research-plan.md).

## How it's organized

Plain Markdown + flat YAML frontmatter, cross-linked with double-bracket wikilinks:

- `concepts/` / `mocs/` — atomic ideas; promoted to a map of content when ≥5 cluster.
- `literature/` — processed notes on papers, repos, posts (0–5 relevance scored).
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs (hypothesis → result, config, metrics, log).
- `raw/` — immutable source captures · `docs/decisions/` — ADRs · `_meta/` — index, log, templates.

## Local use

```sh
make env    # uv sync
make lint   # knowledge-graph / experiment health check
```

Built on the [claude-system](https://github.com/eschmitt88/claude-system)
research framework (upstream attribution — this project is its own repo).
See `CLAUDE.md` for the agent-facing orientation and `~/.claude/CLAUDE.md`
for the framework's durable principles.
