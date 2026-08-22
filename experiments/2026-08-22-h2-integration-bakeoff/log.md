# Log — h2-integration-bakeoff

- 2026-08-22 03:15 scaffolded; waits for H1 collection to finish before launch (headroom verdict: slow/low → one batch at a time).
- 2026-08-22 02:58 launched run.py (84 generations Sonnet 5 (6 problems × [2 baselines + 3 seeds × 4 strategies]), 84 judgments Opus 5, parallel 5)
- 2026-08-22 03:10 crashed at 28/84 gens on an API-side [bio] safety refusal (one job); patched runner to record refusals per job + retry transient errors; resumed
- 2026-08-22 03:41 complete: 84/84 judged, 4 refusals. brief 3.29 vs naive 2.12 (13/1 p=0.002); persona≈naive; 94% home-field-default. README filled.
