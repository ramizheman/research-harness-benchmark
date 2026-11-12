# APPM-025: Personnel feasibility of rank-1 CUT openers

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Model's rank-1 openers are executable by each team's top-8 rotation.

## Design
8 teams; personnel capacity and stretch ceiling per PT vs rank-1 opener CUT target.

## Result
All 24 openers seeded by CUT/PUTBACK/TRANSITION/PNR; CUT target exceeds stretch ceiling by +9.6 to +15.9pp for every team (e.g. PHI capacity 1.7% vs target 16.4%).

## Failure evidence
Optimizer uses league-average CUT execution and ignores personnel, so every team gets the same CUT-heavy opener.

## Power and reliability
n=8 teams

## Related
Playoff G1 retrospective

## Notes
Led to V2 risk-aware, feasibility-filtered playsheet.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PLAYOFF_RETRO_SUMMARY_2026-04-20.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PERSONNEL_FEASIBILITY_PLAYOFF_TEAMS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STRATEGY_V2_RESULTS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\RISK_AWARE_OPENERS.md

## Follow-on candidate
candidate, needs curation (see Notes)

## Same study family
SF32 (duplicate_records): APPA-033
shared CUT target exceeds ceiling by +9.6 to +15.9 pp
