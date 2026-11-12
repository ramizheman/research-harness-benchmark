# APPS-087: Connector tangible impact: star shielding, TO, lineup lift

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-27 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 3
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Box score and traditional stats
- Method tags: regression
- Limitation tags: small sample; confounding
- Variable tags: PPP (points per possession); net rating / ORtg
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Connector presence shields stars (higher TS, lower TO) and lifts lineup ORtg beyond talent.

## Design
61 star-season pairs >=80 poss w/wo CONNECTOR. HasConn M1 regressions. Lineup lift talent-controlled and held-4 swap n=296. Wilcoxon battery n=73.

## Result
Star dTS +0.05 pp p=0.937; dTO +0.74 pp p=0.00364 (wrong sign for shielding). Star-init TO~HasConn beta=+0.34 pp p=0.439. HasConn on-off PPP BOTH_NULL (mean -0.041 p=0.939, median +0.528 p=0.731, n=73). Frequent-conn lineup ORtg lift LOO +1.559 p=0.0184 but talent-controlled beta +0.915 p=0.51 n=428. Held-4 swap dORtg +0.427 p=0.565 n=296.

## Failure evidence
PPP/TS/eFG shielding null; TO rate rises with connectors. Lineup ORtg lift is a talent confound (p=0.51 after TALENT; swap p=0.565).

## Power and reliability
n=61 star pairs; 73 team-seasons; 296 held-4 swaps; 428 lineups

## Related
APPS-086

## Notes
Wilcoxon agrees with means on the nulls (BOTH_NULL) and on TO (BOTH_SIG, higher TO with HasConn).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_tangible_impact_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_offense_median_wilcoxon_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\lineup_lift_diagnostics_report.md

## Related records (ids resolved to merged records)
APPS-086
