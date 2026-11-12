# APPS-024: DRIVE-as-BEST counter vs constrained mix

- Project: Strategy app
- Date: 2026-05-30 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample; low power / large MDE
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
When BEST=DRIVE (counter_h2_n>=5), observed DRIVE H2 PPP beats a feasibility-constrained baseline.

## Design
44 qualifying triggers, 39 games, 13 teams. Mix weights CUT 15%/SPOT_UP 35%/DRIVE 30%/OTHER 20%. One-sided MW A>B and A>C.

## Result
A mean=1.178 vs B_game 1.236 (gap=-0.058, p=0.6069) vs B_fixed 1.244 (gap=-0.066, p=0.2175) vs coach default C 1.134 (gap=+0.043, p=0.3052). MDE at 80% power ~0.180 PPP (SD~0.34).

## Failure evidence
Observed gap -0.066 is below MDE 0.180; n=44 cannot distinguish a true null from an effect up to 0.18 PPP.

## Power and reliability
n=44; MDE 0.180 PPP at 80% power (SD~0.34); 0.265 if SD~0.5

## Related
APPS-023

## Notes
A is left-skewed (median 1.279 > B_fixed) so MW p=0.2175 for A>B is consistent with a negative mean gap.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\drive_counter_test.md

## Related records (ids resolved to merged records)
APPS-023
