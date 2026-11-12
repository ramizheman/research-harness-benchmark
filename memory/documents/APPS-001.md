# APPS-001: Overnight 10-series LLM adaptation review (adapters win series)

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 10
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The team that adapted better within games (per LLM adaptation review) wins the playoff series.

## Design
LLM agent adaptation reviews of H1 vs H2 play-type PPP for both offenses in 52 games across 10 playoff series (104 reports, all status ok), aggregated into series and master summaries.

## Result
Team judged to have adapted better won 9 of 10 series; exception RECENT3_DEN_vs_MIN_26. SPOT_UP and DRIVE stifled in 10/10 series; offenses failed to counter in 9/10.

## Failure evidence
Post-hoc LLM narrative judgment of 'adapted better' with knowledge of winners; several winners described as adapting better 'enough (or opponent failed more)'.

## Power and reliability
10 series, 104 team-game reports; per-half play-type samples often n<10 possessions

## Related
three_series_test pipeline run

## Notes
No quantitative test; adaptation judgments made by the LLM after outcomes were known, so the 9/10 relationship is not an independent evaluation. Several per-game reports are very short (~1-2 KB), possibly truncated.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\batch_adaptation_overnight\MASTER_SUMMARY.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\batch_adaptation_overnight\_run_log.json
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\batch_adaptation_20260524_003952\_manifest.json
