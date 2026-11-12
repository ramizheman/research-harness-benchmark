# APPA-062: L5 baseline comparison: V0/V2/V4/V5 team-aggregate regret

- Project: Strategy app
- Date: 2026-05-07 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes; LLM or agent outputs
- Method tags: ablation; LLM agent run
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Scheme fingerprint (V2), optimizer (V4), and agents (V5) beat a scheme-neutral team PPP baseline on |projected-observed| regret.

## Design
Same 40 (slug, side) pairs from l5_ablation_results.parquet; observed_ppp is series-level weighted-mean PPP, not per-recommendation.

## Result
Mean regret: V0_NEUTRAL 0.1072, V0_TEAM 0.1053, V2_TEAM 0.1003, V4 0.1148, V5 0.0979. V2 vs V0_NEUTRAL mean_diff -0.0069 p=0.190. V4 vs V0_NEUTRAL +0.0075 p=0.563 (V4 worse). V5 vs V4 n_diff=15 beat_rate 0.275 / cond 0.733 mean_diff -0.0169 p=0.0309. V5 vs V0_NEUTRAL -0.0093 p=0.2589.

## Failure evidence
n=40; V2 and full stack vs neutral p>0.05; V4 trends worse than neutral. Only V5 vs V4 on 15 differing pairs is p=0.031.

## Power and reliability
n=40 pairs

## Related
APPA-061

## Notes
Conflicts with APPA-061 'AGENTS DEGRADE' headline: here V5 median/mean regret is lower than V4. Target is team-aggregate PPP, not the recommended play type.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\L5_BASELINE_COMPARISON.md

## Related records (ids resolved to merged records)
APPA-061
