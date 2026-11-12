# APPM-045: Playoff G1 retrospective: plan conformance vs outcome (opened RETRO files)

- Project: Strategy app
- Date: 2026-04-20 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 4
- Dataset tags: Playoff series outcomes
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: small sample
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: 

## Hypothesis
Teams running closer to the model opener portfolio perform better, and pre-game favorite/PPP direction matches the game.

## Design
4 Game 1s / 8 team-games; avg |delta| on leverage buckets vs result; headline modeled vs observed PPP and winner.

## Result
Winner direction 4/4 YES. ORL PPP 1.2364 vs 1.109 (all)/1.474 (classified), DET 1.2183 vs 0.981/1.507, ORL WP 59.0% won 112-101. PHI 1.2143 vs 0.875/1.137, BOS 1.3185 vs 1.230/1.538, PHI WP 11.1% lost 91-123. PHX 1.2254 vs 0.903/1.273, OKC 1.2758 vs 1.266/1.566, PHX WP 26.7% lost 84-119. POR 1.2248 vs 1.021/1.225, SAS 1.2591 vs 1.144/1.521, POR WP 33.5% lost 98-111. Conformance: PHX 24.0pp drift lost by 35; PHI 4.5pp closest lost by 32. 5/8 team-games closest to opener #2-#4.

## Failure evidence
Four games is not enough evidence to claim the plans work in a statistical sense (doc). Winner-picking 4/4 is a weak test (favorites were large).

## Power and reliability
n=8 team-games

## Related
APPM-024; APPM-025; Personnel feasibility of CUT openers

## Notes
Updated copy of APPM-024 after opening the four RETRO_ files. ORL favorite at 59% uses the older pooled prior (STRATEGY_V2 later flipped DET to 86%).

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PLAYOFF_RETRO_SUMMARY_2026-04-20.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RETRO_ORL_vs_DET_0042500101.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RETRO_PHI_vs_BOS_0042500111.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RETRO_PHX_vs_OKC_0042500141.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RETRO_POR_vs_SAS_0042500151.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_batch_playoff_retros.py

## Related records (ids resolved to merged records)
APPM-025
