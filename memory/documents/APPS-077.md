# APPS-077: Star-specific 8x8 transition matrices (30 stars)

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Structural roles and influence
- Pre-specified: yes
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Teammate DRIVE -> star PNR (inferrer-only) is a recurring setup; other star transitions are structural if they FIND in 3+ stars.

## Design
30 stars x 64 cells=1920; 883 estimated (n_t>=30). BH-within-star + placebo + FT-clean.

## Result
Pre-reg DRIVE->PNR: all NULL/WEAK (SGA ATT=-0.222 BH_p=0.433). FINDING cells: 2 (Curry CUT->DRIVE +0.460 n=66 LOW_CONFIDENCE; Leonard SPOT_UP->POST_UP -0.360 n=137). Zero transition types FIND in 3+ stars. WEAK: 36.

## Failure evidence
Pre-registered hypothesis untestable (insufficient inferrer-only n) and unreplicated; 2 isolated FINDING cells expected at ~5% of 883 tests.

## Power and reliability
883 matched cells of 1920

## Related
APPS-060; APPS-066

## Notes
Per-star .md files are the cell dumps; summary is the experiment record.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\star_matrix_summary.md

## Related records (ids resolved to merged records)
APPS-060, APPS-066

## Also recorded as
CHT-036
