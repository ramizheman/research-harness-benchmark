# APPS-056: Historical series_analysis backtest: winner and PT-rank Spearman

- Project: Strategy app
- Date: 2026-04-30 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 45
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: matched control; holdout, backtest or replay; correlation
- Limitation tags: 
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: 

## Hypothesis
Pregame predicted series winner and predicted PT-PPP ranks match realized playoff series outcomes.

## Design
45 series_analysis.md reports (51 slug folders). Winner from predictions.json vs actual. Spearman of pregame PT PPP ranks vs observed series PPP-by-PT. Canonical-10 Spearmans tabulated in Chat 6.

## Result
Winner: 27 CONFIRMED / 18 CONTRADICTED of 45 (60%). Canonical-10 team-side Spearman median ~0.536 (20 sides); series-mean median ~0.554. Example phi_bos_2526: predicted BOS (85.2% conf, PHI baseline 7.4%) CONTRADICTED (PHI 4-3); scheme-adjusted Spearman PHI 0.714, BOS 0.452. Chat 6 also cites RS holdout methodology rho=0.54, n=454, MAE 0.0922 PPP from pipeline_report_metadata.json.

## Failure evidence
Winner hit 27/45 with no CI; per-series Spearmans range from PHI_BKN -0.024 to MIN_DEN 0.905; RS 0.54 is a hand-maintained headline file.

## Power and reliability
45 series with series_analysis.md; canonical 10 for tabulated rho

## Related
APPS-003; APPS-008

## Notes
Family of repeated series backtests. Individual TEAM_vs_TEAM generated reports in reports/ and demo_reports/ were not scored as experiments. Remaining 6 series_analysis folders lack series_analysis.md.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\series_analysis\phi_bos_2526\series_analysis.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\Chats\6. cursor_spearman_correlation_for_basketb.md

## Related records (ids resolved to merged records)
APPS-003, APPS-008
