# APPS-002: Three-series adaptation review and v2 playsheet pipeline test

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: tool_eval_pass
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 16
- Dataset tags: Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: three-point attempts or luck
- Paper: 

## Hypothesis
The agent adaptation-review and v2 playsheet pipeline runs end to end on full playoff series.

## Design
16 focal games (MIA vs BOS 2023 ECF G1-7, DEN vs MIA 2023 Finals G1-5, LAL vs OKC 2025-26 G1-4), one offense each; adaptation review plus v2 playsheet per game.

## Result
16/16 runs status ok (19-25 tool calls, ~124-227 s each); MIA_BOS tiered playsheet: 5 robust, 5 fragile, 1 structural of 11 entries.

## Failure evidence
Only run status recorded; no outcome-based scoring. G3_DEN_off.md is only 1405 bytes (report appears truncated).

## Power and reliability
16 games

## Related
Overnight 10-series LLM adaptation review

## Notes
Pipeline smoke test rather than a validation of recommendations.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\three_series_test\_three_series_log.json
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\three_series_test\MIA_vs_BOS_2023_ECF\MIA_BOS_tiered_playsheet.md
