# APPM-021: Within-game tactical adaptation (halftime, crunch, post-run)

- Project: Strategy app
- Date: 2026-05-05 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: low measurement reliability; label or classification error
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Describe how play-type mix shifts by halftime margin, crunch time and after runs.

## Design
1,086,514 possessions / 5,187 games; H1 vs H2 by margin bucket; Q4 last 5 min |margin|<=5; post-run opponent PT.

## Result
OTHER +2.26 to +2.48pp in H2 in every bucket; crunch OTHER +6.08pp, PULL_UP +1.20pp at -0.045 PPP; post-run DRIVE +3.75pp, OTHER -6.72pp.

## Failure evidence
No inferential tests; OTHER label known to be noisy (PT audit).

## Power and reliability


## Related
Play-type label audit

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\within_game_adaptation_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_analyze_within_game_adaptation.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\adaptation_data.csv
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_adaptation_run_log.txt

## Also recorded as
CHT-010
