# APPS-008: Engine layer ablation L1-L4 with placebos

- Project: Strategy app
- Date: 2026-05-04 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: failed_gate
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: placebo or permutation test; bootstrap interval; ablation; calibration scoring
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Each engine layer (PNR calibration, scheme fingerprint, tier correction, sequential conditioning) improves prediction of observed series PPP.

## Design
42 series; configs V0..V4, LOO A1-A4, FP/tier shuffles; 268 scheme cells / 213 PT cells; cluster bootstrap 10,000, Holm correction.

## Result
May-7 PT-level vs V0_NEUTRAL: V4 beat 0.422 [0.365,0.480], V2 0.399 [0.338,0.459], FP_SHUFFLE 0.479 [0.412,0.544]; vs V0: V2 0.526 [0.469,0.585], V4 0.451. May-4 dir_acc: V4 0.205 vs A_SHUFFLE placebo 0.511 (gap -0.306).

## Failure evidence
No forward config beats V0_NEUTRAL (all beat rates <0.5, CI excludes 0.5 above); placebo ties or beats V4 in the first version.

## Power and reliability
213 PT cells, 42 series; CI width about +/-0.06

## Related
SQ2 decision quality hit rate

## Notes
Version 1 (May 4) reported L2 lift +0.172 dir_acc but a placebo beating V4; version 2 (May 7) added a scheme-neutral baseline that no layer beats. L1 and L4 contributed ~0 in both.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\ablation_summary.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\ablation_report.md

## Also recorded as
CHT-015
