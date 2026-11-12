# APPA-004: DID-ADAPT case study NYK vs PHI 2025-26 series

- Project: Team Adaptation
- Date: 2026-05-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: difference-in-differences; case study
- Limitation tags: small sample; selection or regression to the mean
- Variable tags: PPP (points per possession); three-point attempts or luck
- Paper: 

## Hypothesis
Within-game and within-series adaptation toward engine counters coincides with better PPP in one series.

## Design
4 games x 2 teams = 8 team-game rows with three-thirds A1 method; series-level SHOULD vs DID cosine (A2).

## Result
Adapters 4/8 rows; mean dPPP adapters +0.0327 vs non-adapters -0.2987. A2 could not be computed: no SHOULD vector in correction_log.json.

## Failure evidence
n=8 team-game rows; series SHOULD vector missing.

## Power and reliability
n=8

## Related
APPA-003

## Notes
Same selection issue as APPA-003 applies.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\DID_ADAPT_NYK_vs_PHI_2526.md

## Related records (ids resolved to merged records)
APPA-003
