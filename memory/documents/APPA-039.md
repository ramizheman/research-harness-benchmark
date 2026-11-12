# APPA-039: Fragility F1: usage-residual structural load exists and is split-half stable

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (doc)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Box score and traditional stats; NCAA tournament and ratings data
- Method tags: placebo or permutation test; split-half reliability; bootstrap interval; regression; correlation
- Limitation tags: low measurement reliability
- Variable tags: play-type share / mix; structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
On the full sample, usage explains <90% of structural load with residual share CI lower bound >0.10 (F1a), and usage-residual load is split-half stable (F1b pooled and usage-partial).

## Design
120 team-seasons, 30 franchises; fragility_full_study.py --n-null 500 --n-perm 5000 seed 17 N_BOOT=2000; franchise-clustered permutation and bootstrap. Amendment 1 (post-gate, pre-full-run) made usage-partial Spearman co-primary for F1b.

## Result
F1a cosine R2=0.094, residual-share=0.906, CI [0.768, 0.962] PASS; Frobenius R2=0.073 share=0.927 CI [0.828, 0.965]. F1b pooled-residual rho=+0.685 p=0.0000 CI [+0.649, +0.721]; usage-partial rho=+0.557 p=0.0000 CI [+0.491, +0.618].

## Failure evidence
Residual-share CI lower bound 0.768 > registered 0.10; both F1b CIs exclude 0 and p<0.01; 30 franchises above the ~20 floor.

## Power and reliability
120 team-seasons, 30 franchises; 1962 season-level players; 1965 paired players

## Related
APPA-038; APPA-007

## Notes
One allowed mid-course correction: usage-partial F1b co-primary because usage itself is split-half stable. Load is registered as not a value/points measure.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FRAGILITY_PREREGISTRATION.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
PAP-004, APPA-007

## Same study family
SF18 (repeat_runs_or_robustness): APPS-083, PAP-004
APPS-083 and PAP-004 share F1a R2=0.099 and F1b rho=+0.670 [0.636, 0.705]; APPA-039 is an earlier run (R2=0.094, rho=+0.685)
