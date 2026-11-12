# APPA-045: Joint vs sequential Rank-then-Route ranking

- Project: Defensive Suppression
- Date: 2026-06-22 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Picking play type and player jointly beats sequential Rank then Route enough to justify the extra step.

## Design
_joint_vs_sequential.py; n=2,779 RS triggers; blended matchup PPP, min 3 H2H poss/player.

## Result
Joint pick = sequential 80.3%; joint reroutes 19.7% (547). Mean PPP left on table +0.020 all / +0.099 reroutes only (median +0.080). Play-type gap BEST vs 2nd 0.215 mean / 0.182 median. Routing premium +0.089. Strict dominance 49.2%.

## Failure evidence
Mean +0.020 PPP left on table is small; sequential declared safe ~80% with joint tiebreak in ~20%.

## Power and reliability
n=2,779 triggers

## Related
APPA-044

## Notes
Prior weight 50 ? reroutes partly reflect talent routing, not pure matchup.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-044
