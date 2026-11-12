# APPM-057: Defense-pool diversity: ROBUST label vs duplicate regimes

- Project: Strategy app
- Date: 2026-04-17 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The N~8-12 defensive adaptations used to certify playsheet ROBUST are genuinely distinct regimes (cosine clusters at 0.90), not near-duplicate single-knob tweaks.

## Design
Reuse _build_playsheet_conditional pool; pairwise cosine on PT delta vectors; single-link clusters at 0.95/0.90/0.80/0.50. Two matchups: BOS vs OKC and OKC vs BOS.

## Result
BOS vs OKC: 12 adaptations, 11 clusters at 0.90 (D3 STAR_DENIAL ~ D12 tighten PNR cosine 0.97). Baseline PPP 1.2916; opener POST_UP-4%->CUT+4% cumulative ++0.0625. OKC vs BOS: 11 adaptations, 10 clusters at 0.90 (D3~D11 cosine 0.96). Baseline 1.2025; cumulative ++0.0911. Verdict both: GENUINELY DISTINCT - ROBUST label is fully earned. At 0.50 threshold clusters collapse to 7 and 6.

## Failure evidence
11/12 and 10/11 distinct at the registered 0.90 threshold.

## Power and reliability
n=2 matchups

## Related
CASE_STUDIES.md scheme robustness

## Notes
STAR_DENIAL is nearly collinear with PNR-tighten in both directions; still counted as distinct at 0.90 because only that pair merges.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_audit_defense_pool.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_audit_out.txt

## Finding status
supported in source; independent replication not recorded
