# APPS-061: Test 2: PUTBACK Q4 star-suppression IVW trend

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test; matched control
- Limitation tags: small sample; low power / large MDE
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Star PPP after conceding a putback declines monotonically Q1->Q4.

## Design
Matched ATT by quarter; IVW trend; quarter-shuffle placebo 5000x; Cochran-Armitage P(score). Treated=2481, control capped 60000.

## Result
Q1 ATT=+0.0671 to Q4 -0.1394. IVW slope=-0.0649/qtr (z=-2.98, one-sided p=0.0014). Placebo p=0.0028. RS Q4 -0.1262 [-0.2240,-0.0284] n_t=465; close -0.1949; playoffs Q4 CI[-0.444,+0.138] n_t=55 underpowered. CA p=0.0378.

## Failure evidence
Trend clears IVW, placebo, and Q4 CI excludes 0 in RS/close. Mechanism unresolved (Test 3 null) and playoff subset underpowered.

## Power and reliability
n_t Q1=705 Q4=520; playoffs n_t=55

## Related
APPS-041; APPS-062

## Notes
Console verdict said WEAK SIGNAL; header said FINDING (qualified). Recorded as supported-with-qualifications; Test 3 shows load is not the mechanism.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\test_2_putback_trend.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-041, APPS-062
