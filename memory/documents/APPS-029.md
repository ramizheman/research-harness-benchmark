# APPS-029: Live Tab-2 trigger timing, 25 series 2025-26

- Project: Strategy app
- Date: 2026-05-28 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Same live-trigger rest-of-game test on 25 2025-26 playoff series.

## Design
Same Tab 2 logic as APPS-028; 228 unique triggers; AVOID_OVERRIDE rule added.

## Result
228 triggers, 100% actionable, mean remaining 21.0. Spearman rho=-0.2066, p=1e-06, n=557. MW BEST 1.263 (n=57) vs AVOID 0.783 (n=110), p=0.0. Early BEST-AVOID gap 0.701 vs late 0.415.

## Failure evidence
BEST vs AVOID ROG PPP confirmed (p=0.0) and Spearman significant; timing still 100% actionable.

## Power and reliability
557 counter obs, 228 triggers

## Related
APPS-028

## Notes
Different conclusion from the 10-series live replay; n_runs kept separate because MW went from p=0.074 to p=0.0.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\live_trigger_validation\live_trigger_report_seasons_25_26_clean.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-028

## Same study family
SF04 (repeat_runs_or_robustness): APPM-028, APPS-028, CHT-038
APPM-028 and APPS-029 share rho=-0.2066, n=557, gaps 0.701/0.415; APPS-028 (10 series) and CHT-038 (25 games) are earlier runs of the same trigger-timing design
