# APPS-032: CUT depletion / decay hypothesis (feasibility, not efficiency)

- Project: Strategy app
- Date: 2026-05-28 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: correlation
- Limitation tags: label or classification error
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
CUT PPP decays across successive H2 runs, so the playsheet should rotate off CUT to SPOT_UP.

## Design
311 playoff games, 12361 H2 CUT/SPOT_UP/DRIVE possessions. Decay curve, switch-point vs SPOT_UP, depletion-adjusted Spearman, DP policy vs static.

## Result
CUT PPP stable 1.60-1.71 for runs 1-5 (all n>=14); runs 6+ n=4/2/0. 62.0% of team-halves never crossed below SPOT_UP (n=405). Depletion-adjusted rho -0.0415 vs baseline -0.2737 (degraded 0.2322). DP -6.7 pts/100 vs static ? invalidated.

## Failure evidence
No efficiency cliff; constraint is opportunity (~3-5 CUT per half). DP was built on fabricated decay.

## Power and reliability
311 games; CUT runs 6+ essentially unobserved

## Related
APPS-023

## Notes
Actionable output was constrained mix tables replacing single-label BEST:CUT.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cut_depletion_analysis\CUT_DEPLETION_FINDINGS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cut_depletion_analysis\dp_policy_validation.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cut_depletion_analysis\depletion_validation.md

## Related records (ids resolved to merged records)
APPS-023
