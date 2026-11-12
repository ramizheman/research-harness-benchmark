# APPS-019: PO 55-series n-gated BEST vs AVOID counter gap (leakage-corrected)

- Project: Strategy app
- Date: 2026-06-20 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: leakage
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Out-of-sample playsheet tiers (series held out) rank counters so BEST outscores AVOID after a suppression trigger.

## Design
55 playoff series, 272 games, 633 triggers, counter_h2_n>=5; row-mean PPP (canonical). Scout exclude_gids leakage fixed 2026-06-20. Robustness: CUT removed, n>=10, within-play-type, CUT share<=15% cap.

## Result
Canonical n-gated gap +0.375 (BEST 1.298 n=193 vs AVOID 0.923 n=156, p=0.0). Ungated Spearman rho=-0.2349, n=2544. Within-play-type +0.225 (p~1e-07); CUT removed +0.279; n>=10 +0.221; CUT<=15% cap gap +0.505 (2508 rows). Oracle BEST 1.578 (+0.655 vs AVOID); routing gain +0.280. Pre-fix leaky gap was ~+0.488.

## Failure evidence
Gap survives leakage fix, CUT removal, n-gate, within-type, and feasibility cap; thick H2H (>=50) gap +0.384 vs thin +0.131.

## Power and reliability
193 BEST / 156 AVOID n-gated rows; 1580/1409 possessions; 272 games

## Related
APPS-018; APPS-020; APPS-003

## Notes
COHERENT_NUMBERS.md is deprecated in favor of FINAL_NUMBERS_SHEET.md (APPA slice) but is the playsheet_validation canonical writeup. Do not cite poss-weighted BEST-AVOID +0.323 on slides; row-mean +0.375 is locked.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\COHERENT_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\h1h2_aggregate_all_graph_series\validation_report_clean.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\best_avoid_gap_defense.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cut_feasibility_cap\cut_feasibility_cap_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\slide5_tier_table.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-018, APPS-020, APPS-003

## Same study family
SF03 (repeat_runs_or_robustness): APPA-036, APPM-030, APPS-020, PAP-043, CHT-042
shared BEST-AVOID gaps +0.375 (PO) and +0.422 (RS), BEST 1.298/1.423, AVOID 0.923/1.001 | Same BEST vs AVOID counter-gap design run on playoff and regular-season samples before and after the leakage correction.
