# APPM-056: PatternQueryLayer validation audit (KEEP/MODIFY/KILL)

- Project: Strategy app
- Date: 2026-04-13 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: partial
- Verdict: tool_eval_pass
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix; turnovers
- Paper: 

## Hypothesis
Each PatternQueryLayer pattern varies across games, differs for winners vs losers in the expected direction, and is cross-context stable enough to KEEP.

## Design
~20 mixed RS/playoff games (sample includes 2025 Finals OKC-IND G5-G7); per-pattern variance, winner-minus-loser PPP, correlation with wins, KEEP/MODIFY/KILL.

## Result
9 patterns: 8 KEEP, 1 MODIFY, 0 KILL. shot_selection KEEP w-l_ppp=0.1542 corr=0.17 n=216; clutch_performance 0.2092 / 0.36 n=135; momentum_response 0.1591 / 0.305 n=230; game_state_efficiency 0.1894 / 0.349 n=348; possession_flow 0.1686 / 0.085 n=262; pace_control 0.0968 / 0.102 n=183; initiation_efficiency 0.1147 / 0.097 n=229; court_zones KEEP w-l_ppp=None corr=0.0 n=227. turnover_diagnostics MODIFY (high variance + instability) n=457 corr=0.0.

## Failure evidence
8/9 KEEP; none KILL; one MODIFY for turnover_diagnostics.

## Power and reliability
n_rows 135 to 457 per pattern; ~20 games

## Related


## Notes
court_zones kept despite corr=0.0 / w-l_ppp None; reason string still says stable signal, correct direction.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\pattern_validation_audit.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\pattern_audit_results.json
