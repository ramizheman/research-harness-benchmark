# APPS-076: Trigger attribution: variance of H1->H2 PPP collapse

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Shot-level data with expected FG; Box score and traditional stats
- Method tags: regression
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Observable in-game process/usage/shot-selection/lineup/context changes explain suppression triggers beyond RTM.

## Design
40963 team-game-PT rows (>=5 both halves), 5234 games. Nested OLS on ppp_change. Triggers 12617 (30.8%), mean collapse -0.612.

## Result
RTM (ppp_h1 alone) 32.9% of variance. Usage +0.0%; process+shot-zone +1.7%; lineup +0.0%; context +0.0%. Unexplained 65.4%. Total explained 34.6% (RTM=95% of explained).

## Failure evidence
Process/usage/lineup/context add ~1.7 pp; residual 65.4% is idiosyncratic noise from small per-half n.

## Power and reliability
n=40963 cells; 12617 triggers

## Related
APPS-022; APPS-070

## Notes
Consistent with distribution-shift null: collapses are mostly hot first halves cooling off.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\trigger_attribution_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\trigger_attribution.py

## Related records (ids resolved to merged records)
PAP-036, APPS-070
