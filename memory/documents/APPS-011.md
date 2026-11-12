# APPS-011: Regular season vs playoff PPP by play type (DRIVE over-prediction)

- Project: Strategy app
- Date: 2026-05-08 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: calibration scoring
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
DRIVE PPP is materially higher in RS than playoffs, so an RS-calibrated optimizer over-recommends DRIVE.

## Design
Team-level (team, PT, context) cells, min 30 poss, up to 25 teams.

## Result
DRIVE RS 1.198 vs PO 0.912 (-0.286, 25 teams); PNR -0.173; PULL_UP +0.301; others within -0.07.

## Failure evidence
DRIVE playoff PPP 0.286 below RS across 25 teams; top-10 teams all -0.30 to -0.43.

## Power and reliability
25 teams, min 30 poss per cell; no CIs

## Related
SQ2 decision quality hit rate (DRIVE exclusion); Defensive style RS vs playoff

## Notes
Motivated the playoff DRIVE exclusion and a proposed playoff DSI offset.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_rs_vs_playoff_ppp.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\rs_vs_playoff_run.log

## Finding status
supported in source; independent replication not recorded

## Follow-on candidate
candidate, needs curation (see Notes)
