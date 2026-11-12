# APPS-060: Test 1: 8x8 action transition matched ATT matrix

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: yes
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test; bootstrap interval; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Predecessor play type A changes PPP of next play type B after exact matching, surviving BH-FDR and placebo.

## Design
64 A->B cells. Exact match margin_bucket x period x season x offensive team. Cluster bootstrap 1000; perm 2000; placebo 1000; BH across 64. Min n=30.

## Result
1 of 64 survived matching+BH+placebo: CUT->PNR ATT=-0.0502*. Top unsigned ATT PUTBACK->PUTBACK +0.0615 CI[-0.060,+0.168] not sig. TRANSITION->DRIVE +0.0355 perm_p=0.0020 BH_adj_p=0.0640.

## Failure evidence
Pre-registered bar: 1/64 cells survived; no structural coaching prescription from isolated cells.

## Power and reliability
64 tested pairs; pools capped at 60000

## Related
APPS-078; APPS-068

## Notes
Directional row means: T=TRANSITION 6/8 next-pairs positive (mean ATT +0.0141); T+1=PNR 1/8 preceding positive.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\test_1_transition_matrix.md

## Related records (ids resolved to merged records)
APPS-078, APPS-068

## Also recorded as
CHT-034
