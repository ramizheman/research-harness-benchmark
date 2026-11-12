# APPA-066: TOV_FORCE matchup decomposition on four playoff games

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Lineup and matchup effects
- Pre-specified: no
- Verdict: descriptive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 4
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: matched control
- Limitation tags: insufficient exposure
- Variable tags: turnovers
- Paper: 

## Hypothesis
TOV_FORCE as a top-3 lever can be decomposed into defender x initiator x PT channels with positive matchup lift.

## Design
4 games (ORL-DET, PHI-BOS, PHX-OKC, POR-SAS); Dean-Oliver additive lift from 1.05M recency-weighted possessions; defender cell n>=15.

## Result
Team-PT lifts are small (ORL vs DET PNR +1.2pp; POR vs SAS all PT lifts negative, e.g. PNR -4.1pp) while player-channel lifts are large on small n (Banchero on Huerter SPOT_UP +8.4pp, n_def=17 / n_off=54; Dort on Coffey SPOT_UP +12.0pp, n=25/16; Booker on Wiggins PULL_UP +14.8pp).

## Failure evidence
Player-channel n often 15-28 defensive possessions; primary_defender attribution includes helper steals; no holdout or game-outcome check.

## Power and reliability
4 games; cell n often 15-54

## Related
APPA-067; APPA-059

## Notes
POR vs SAS team-level lifts are all negative, so the top-3 TOV_FORCE lever is coming from sparse player cells, not team PT rates.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HOW_TO_FORCE_TOVS.md

## Related records (ids resolved to merged records)
APPA-067, APPA-059
