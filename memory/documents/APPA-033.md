# APPA-033: Opener recommendations vs personnel feasibility

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Rank-1 openers are within what the top-8 rotation can sustain.

## Design
8 team-games from 4 playoff games; opener target share vs personnel capacity x1.25.

## Result
8/8 rank-1 openers CUT-centered and INFEASIBLE; worst gaps +9.6 to +15.9pp; CUT target 14-18% vs ceiling 2-6%.

## Failure evidence
Optimizer ignores personnel; CUT target 3-10x stretch ceiling in every team-game.

## Power and reliability
8 team-games

## Related
APPA-018

## Notes
Explains the degenerate CUT-heavy recommendations seen in eval reports.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FEASIBILITY_VS_OPENERS.md

## Related records (ids resolved to merged records)
APPA-018

## Same study family
SF32 (duplicate_records): APPM-025
shared CUT target exceeds ceiling by +9.6 to +15.9 pp
