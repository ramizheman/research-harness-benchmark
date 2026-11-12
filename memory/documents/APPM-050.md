# APPM-050: SCOUT LLM insight demos ORL vs DET G1

- Project: Strategy app
- Date: 2026-04-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: Shot-level data with expected FG; LLM or agent outputs
- Method tags: holdout, backtest or replay; LLM agent run
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
A single-shot SCOUT agent can surface one non-obvious, table-grounded insight the deterministic stack missed.

## Design
Two prompts on game 0042500101 with derived tables; groundedness check against table values. Deterministic baseline suppressed from insight space.

## Result
v1: Banchero vs T. Harris two-way edge (Banchero 12 pts ppp_in_matchup 0.341 on 35.2 partial poss; Harris 0 pts / 0.0 PPP on 32.1). v2: ORL outscored DET 31-27 in Q4 despite FT trips 2 vs 11. Retro headline (both): ORL PPP model 1.2364 vs obs 1.109 (all)/1.474 (classified); DET 1.2183 vs 0.981/1.507; ORL WP 59.0%; model correct YES.

## Failure evidence
No scoring of insight quality beyond groundedness check; two runs produced unrelated insights.

## Power and reliability
n=2 prompts on 1 game

## Related
APPM-049; APPM-012 ORL-DET leverage

## Notes
v1 PPP 0.341 on 12 points / 35.2 partial possessions is a matchup-minutes PPP, not possession PPP. Deterministic layer: no opponent-specific edge.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\SCOUT_ORL_vs_DET_0042500101.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\SCOUT_ORL_vs_DET_0042500101_v2.md

## Related records (ids resolved to merged records)
APPM-049, APPM-012
