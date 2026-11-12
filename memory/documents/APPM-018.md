# APPM-018: Scoring-run microstructure

- Project: Strategy app
- Date: 2026-05-07 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Describe what initiates, sustains and breaks scoring runs.

## Design
71,383 runs (>=6 unanswered points) over 1,090,642 possessions / 5,207 games.

## Result
SPOT_UP initiates 22.9% of runs; OTHER most common sustaining type 22.8%; DRIVE most common run-breaker 20.4%.

## Failure evidence
No hypothesis test; frequencies not compared to baseline volumes.

## Power and reliability


## Related


## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\run_microstructure_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_analyze_scoring_runs.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\run_sequences.csv

## Same study family
SF16 (duplicate_records): CHT-008
shared SPOT_UP initiates 22.9%, DRIVE run-breaker 20.4%
