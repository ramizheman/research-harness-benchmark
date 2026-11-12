# APPS-090: Connector diet x destination structural-gap match

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-27 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control; correlation
- Limitation tags: small sample
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Diet-matching to a destination's thin initiation jobs predicts better post-move outcomes than mismatch.

## Design
198 movers with complete diet+gap; taxonomy CONNECTOR n=19; travel-check n=40. match_score=cosine(diet, gap). Primary outcomes portability delta / embedded / d_mpg / d_hhi_top, not PPP.

## Result
Binary match rate 15.7%. Taxonomy CONNECTOR delta match vs mis med +0.540 vs +0.069 p=0.156 n=5/14. Travel-check delta p=0.413. All-movers delta p=0.0283 (med +0.160 vs +0.053) but Spearman(match_score, delta)=-0.034 p=0.631 n=198. Connector-only Spearmans all ns.

## Failure evidence
Connector subsets n=19/40; all-movers binary delta p=0.0283 does not replicate as a continuous Spearman and is not the licensed connector test.

## Power and reliability
n=19 taxonomy connectors; n=198 all movers

## Related
APPS-084

## Notes
Knowable: 15.7% match rate leaves n_match=5 in the taxonomy CONNECTOR cell.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_diet_gap_match_report.md

## Related records (ids resolved to merged records)
APPS-084
