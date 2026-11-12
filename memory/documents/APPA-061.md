# APPA-061: L5 ablation: deterministic V4 vs LangGraph agent V5

- Project: Strategy app
- Date: 2026-05-05 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes; LLM or agent outputs
- Method tags: bootstrap interval; ablation; LLM agent run
- Limitation tags: small sample; multiple testing
- Variable tags: 
- Paper: 

## Hypothesis
LangGraph agents (V5) improve play-type recommendations over the deterministic engine (V4).

## Design
20 series, 40 paired (slug, side) observations; 2,000 series-cluster bootstrap; Holm-Bonferroni on Wilcoxon regret and McNemar.

## Result
Median regret V4 0.102 [0.067, 0.128] vs V5 0.067 [0.050, 0.100], Holm p=0.062. V5 beats V4 11/40 vs 4/40, McNemar p=0.118. Override 8/40 (20%); override hit rate 25.0% [0.000, 1.000]. Brittle precision 7.5%. Parse 40/40. Runtime 60.1s vs 349.6s (5.816x).

## Failure evidence
Holm p=0.062 and McNemar p=0.118 on n=40; override hit 25% on 8 overrides; 0 player-level overrides scorable.

## Power and reliability
n=40 pairs; 8 overrides

## Related
APPA-062; APPA-009

## Notes
Doc interpretation 'AGENTS DEGRADE QUALITY' is stronger than the tests (neither primary p<0.05 after Holm). Successful-override table lists only 2 rows with V5 rec='none'.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\L5_ABLATION_REPORT.md

## Related records (ids resolved to merged records)
APPA-062, APPA-009
