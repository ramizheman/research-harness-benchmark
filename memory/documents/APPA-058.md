# APPA-058: Season stability of top suppressors and negative teammate pairs

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: 
- Limitation tags: small sample
- Variable tags: 
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Each star's top sequential suppressor is stable across seasons, and some teammate X->Y sequences have large negative premiums.

## Design
30 stars x 4 seasons; min n=20 per player-season-opp_play cell. Negative pairs: premium < -0.10, n>=30.

## Result
2/30 (7%) stable (>=75% same top suppressor): D. Mitchell PUTBACK 75%, L. James POST_UP 75%. Negative: J. Tatum->K. Porzingis DRIVE->SPOT_UP -0.444 n=31; Giannis->Lillard DRIVE->PNR -0.263 n=31; J. Brown->J. Tatum SPOT_UP->DRIVE -0.186 n=37.

## Failure evidence
Only 2/30 stars meet the 75% same-top-suppressor stability rule.

## Power and reliability
30 stars x 4 seasons; min n=20/cell

## Related
APPA-050; APPA-053

## Notes
Positive counterpart Brown DRIVE -> Tatum PNR +0.326 n=43; sequence type matters more than pairing.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-050, APPA-053
