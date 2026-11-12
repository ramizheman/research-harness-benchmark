# APPA-059: Historical upset backtest: V2 P(overperform) on 4 known series

- Project: Strategy app
- Date: 2026-04-21 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: failed_gate
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 4
- Dataset tags: Playoff series outcomes
- Method tags: matched control; regression; holdout, backtest or replay; calibration scoring
- Limitation tags: small sample
- Variable tags: play-type share / mix; win probability / series outcome; turnovers
- Paper: 

## Hypothesis
V2 P(overperform) plus the top-feasible opener recovers the narrative lever of four known playoff upsets without future leakage.

## Design
4 series; leakage-safe RS priors (playoff games of the target year dropped); calibration off; 7-game binomial rollup. Tempo mix from pooled within-team-season regression n=9,830 team-games.

## Result
Lever fired 1/4 (DAL-OKC matchup_hunt_stack YES). MIA-MIL: V1 series 0.1% / V2 post-opener 8.7%, top TOV_AVOID not variance_push. IND-NYK: 25.6% vs 44.9%, top TOV_AVOID not tempo UP. ORL-CLE: 45.8% vs 65.2%, top TOV_AVOID not personnel_feasibility. DAL-OKC: 34.6% vs 52.1%, top TOV_FORCE; matchup_hunt_stack was #2 (P=50.5%). TEMPO UP for MIA dP -0.5pp; TEMPO DOWN +0.6pp.

## Failure evidence
n=4 selected known upsets; expected lever matched in 1/4; all top-feasible openers collapsed to four-factor TOV/OREB rather than the claimed mechanism except DAL's #2.

## Power and reliability
4 series; priors 255,099 (MIA) / 319,921 (others) possessions

## Related
APPA-033; APPA-060; APPA-066

## Notes
OREB_PUSH was top-5 for every series with realized muDelta +0.012 to +0.015 and a fixed 0.55 survival ratio. Earlier TEMPO_UP for MIA (+0.7pp) was a hand-picked mix-shift term.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HISTORICAL_UPSET_BACKTEST.md

## Related records (ids resolved to merged records)
APPA-033, APPA-060, APPA-066

## Same study family
SF10 (duplicate_records): CHT-089
shared four-series probabilities 25.6%, 45.8%, 65.2% | Verdicts differ: failed_gate vs inconclusive.
