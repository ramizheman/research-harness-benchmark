# APPS-070: H1 usage as predictor of H2 suppression (distribution shift)

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Box score and traditional stats
- Method tags: matched control
- Limitation tags: selection or regression to the mean
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
First-half reliance on a play type predicts second-half suppression after controlling for H1 PPP / mean reversion.

## Design
8873 team-games, 37067 cells (>=4 poss both halves). Test A slope; Test B matched HIGH vs LOW H1 usage; Test C multinomial which-type-suppressed.

## Result
Test B: all BH-adjusted null/WEAK (PNR ATT=+0.0313 BH_p=0.0658 WEAK; others NULL). Test C top-1 acc=0.550 vs mean-reversion baseline 0.511 (+0.039) vs most-used 0.239. Test A PULL_UP slope -0.0581 p=0.0030; CUT -0.0917 p=0.0410; PNR +0.0562 p=0.0005 (wrong sign for suppression).

## Failure evidence
Matched ATT does not survive BH; predictive lift over mean reversion is only +0.039 (0.550 vs 0.511). Bulk of H2 suppression is RTM.

## Power and reliability
n=8873 team-games; Test C test n=1008

## Related
APPS-077; APPS-010

## Notes
Headline: no robust evidence H1 reliance predicts H2 suppression.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\distribution_shift.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\distribution_shift.py

## Related records (ids resolved to merged records)
APPS-077, APPS-010
