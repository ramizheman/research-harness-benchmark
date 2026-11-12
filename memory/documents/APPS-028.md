# APPS-028: Live Tab-2 trigger timing, 10 series (rest-of-game BEST vs AVOID)

- Project: Strategy app
- Date: 2026-05-28 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Tab 2's live trigger fires with time to act, and rest-of-game PPP is higher on BEST than AVOID counters.

## Design
Possession-by-possession replay, 10 2025-26 series. Trigger: H2 PPP drop>=0.25, n>=10 (or n>=5 with eff_n>=300). Counter PPP measured after trigger, not full H2.

## Result
101 triggers; 100% actionable (>=5 H2 poss remaining); mean remaining 23.4. Spearman tier vs ROG PPP rho=-0.0457, p=0.45616, n=268. MW BEST 1.227 (n=30) vs AVOID 1.037 (n=95), p=0.073965 (not confirmed at 0.05). Early vs late BEST ROG 1.521 vs 1.182.

## Failure evidence
Timing is actionable (100% with >=5 remaining) but BEST vs AVOID ROG PPP p=0.073965 and Spearman p=0.456.

## Power and reliability
268 counter obs, 101 triggers; BEST n=30

## Related
APPS-029

## Notes
Follow-up 25-series replay (APPS-029) confirms BEST vs AVOID.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\live_trigger_validation\live_trigger_report.md

## Related records (ids resolved to merged records)
APPS-029

## Follow-on candidate
candidate, needs curation (see Notes)

## Same study family
SF04 (repeat_runs_or_robustness): APPM-028, APPS-029, CHT-038
APPM-028 and APPS-029 share rho=-0.2066, n=557, gaps 0.701/0.415; APPS-028 (10 series) and CHT-038 (25 games) are earlier runs of the same trigger-timing design
