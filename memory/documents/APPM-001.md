# APPM-001: Play-type mix alignment vs actual PPP (matchup residual)

- Project: Strategy app
- Date: 2026-04-18 (mtime)
- Topic: Lineup and matchup effects
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix; net rating / ORtg
- Paper: 

## Hypothesis
Holdout games where a team's play-type mix is closer to the model's recommended mix score more efficiently.

## Design
908 holdout game-team rows (454 games), terciles of L1 distance actual vs recommended mix; actual PPP residualized on team offense and opponent defense means.

## Result
Raw gap aligned-deviated +5.18 ORtg; strength-controlled gap +3.27 ORtg (+0.0193 vs -0.0134 PPP residual). Model regret median +25.94 ORtg (non-negative by construction).

## Failure evidence
Strength-controlled gap +3.27 ORtg persists after team/opponent residualization.

## Power and reliability
n=908 rows; no CI stated

## Related


## Notes
Observational; doc states regret is a tautology. _new/_prior files are identical reruns (only elapsed time differs).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\MATCHUP_RESIDUAL.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\MATCHUP_RESIDUAL_new.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\MATCHUP_RESIDUAL_prior.md

## Finding status
supported in source; independent replication not recorded

## Also recorded as
CHT-088
