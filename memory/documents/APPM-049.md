# APPM-049: SCOUT D6/D7 8-game calibration batch

- Project: Strategy app
- Date: 2026-04-23 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: tool_eval_pass
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 11
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: calibration scoring
- Limitation tags: small sample
- Variable tags: play-type share / mix; three-point attempts or luck
- Paper: 

## Hypothesis
SCOUT conditional-query triggers (D6 EMPIRICAL PIVOT, D7 REGIME MIX, TRANSITION LEVER, REGIME SHIFT) fire at usable rates and respect Rule-of-Three on 8 playoff games.

## Design
8-game validation batch of ScoutQueryLayer + synthesis D6/D7 rules; then a 3-game thin re-validation of D4/D5/D8 + D7 stack (HOU/LAL, ATL/NYK, ORL/DET).

## Result
8/8 ok, 43 min. Triggers: 14 D6 EMPIRICAL PIVOT, 9 REGIME SHIFT, 1 TRANSITION LEVER, 0 REGIME MIX. Rule-of-Three respected 7/8 (POR/SAS emitted 4 bullets). Post-batch: D7 REGIME MIX threshold +/-10pp -> +/-8pp after probe showed at n>=15 only 2 non-OTHER cells reached 10pp across 16 team-sides (projected 1 REGIME MIX: MIN clutch PULL_UP +9.8%). Thin re-validation 3 ok, ~16 min.

## Failure evidence
8/8 and 3/3 reports completed; Rule-of-Three 7/8 with one documented overflow.

## Power and reliability
n=8 then n=3 games

## Related
SCOUT ORL vs DET demos

## Notes
D6+D7 merge branch (same team,PT firing both) did not occur and remains untested. Thin re-validation is n_runs extra but same product-calibration family; counted in n_runs=11 as 8+3.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PIPELINE_BACKLOG.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_thin_revalidate_three.py
