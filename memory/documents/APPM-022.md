# APPM-022: Superstar suppression profiles (incl. Q5c sequential triggering)

- Project: Strategy app
- Date: 2026-05-05 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Specific opposing lineups, defenders, play types and preceding opponent play types suppress star efficiency.

## Design
Initiator possessions for 4 then ~30 stars (gate >=15); Q5c ranks opponent prior-PT by target PPP for 14 players; reruns 2026-05-06 and 2026-05-30.

## Result
Q5c verdict 'rank-1 suppressor varies meaningfully across players'; e.g. Jokic after opp POST_UP 1.1271 (-0.0675, SE +/-0.0500, n=480); Curry forced POST_UP -0.209.

## Failure evidence
Rank-1 deltas mostly within 1-2 SE with no multiple-comparison control; OTHER artifact flagged in doc.

## Power and reliability
SE per cell reported

## Related
Sequential premium (removed)

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\superstar_suppression_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_analyze_superstar_suppression.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_q5c_expanded.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\suppression_data.csv
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_suppression_run_log.txt
