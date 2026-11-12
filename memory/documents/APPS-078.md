# APPS-078: Channel 2: possession ending state vs next 90-180s volume/points

- Project: Strategy app
- Date: 2026-06-16 (mtime)
- Topic: Other / unclassified
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); turnovers
- Paper: 

## Hypothesis
A possession's ending state changes opponent points/possessions in the next 90-180s beyond ~0.01-0.02 PPP boundary drift.

## Design
911968 possessions. Baseline end state MADE_DEAD. Same-period clock windows.

## Result
90s vs MADE_DEAD: TURNOVER_LIVE dOppPts=+0.510 dNetPts=-0.306 (dOppPPP=+0.055, dOppPoss=+0.298); MISSED_DEAD dNetPts=-0.112; PUTBACK dNetPts=+0.078. Volume (dOppPoss), not PPP, carries most of the live-TO cost.

## Failure evidence
No inferential tests in the core table; live TO raising opponent possession count is largely definitional (steal starts a break).

## Power and reliability
n=911968; MADE_DEAD n=354564

## Related
APPS-075

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\channel2_volume_analysis.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\channel2_volume.py

## Related records (ids resolved to merged records)
APPS-075
