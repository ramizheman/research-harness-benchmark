# APPA-037: Suppression is not regression to mean: matched-control excess

- Project: Defensive Suppression
- Date: 2026-05-29 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: matched control; regression
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
The H1-to-H2 PPP drop after a trigger exceeds the drop of a matched control, beyond what RTM predicts.

## Design
Playoff 55-series: 633 triggers, opponent same-PT same-game control (534 pairs) plus EB shrinkage. Full graph then H1-PPP-balanced caliper match, cluster-robust by game, blowout filter; Z1 OT exclusion and Z2 c_h2_n>=5 applied 2026-07-11.

## Result
PO C: excess +0.680 [0.619, 0.740], n=534, t=22.11; RTM pred 0.097 of 0.626 drop (15.5%), excess 0.529. Full graph unconstrained +0.628 n=9,900 then Z1+Z2 +0.625 n=9,111. H1-balanced caliper 0.10 +0.408 [0.378, 0.438], 1,136 pairs / 848 clusters, perm p<0.0002; blowout |margin|<=20 +0.412 [0.380, 0.443] n=997. Caliper 0.05/0.15/0.20/0.30 excess 0.403/0.397/0.398/0.412.

## Failure evidence
Excess drops from +0.625 unconstrained to +0.408 when balanced on H1 PPP, but the cluster CI excludes 0; Z1+Z2 moved excess only +0.004 vs pre-fix +0.404.

## Power and reliability
848 game clusters, eff. n ~1,088; PO 534 pairs

## Related
APPA-036

## Notes
Deck slide 3 still cites legacy +0.628 / n=9,900. Code audit Z1 (OT in H2, 4,674 poss) and Z2 (control c_h2_n unconstrained) were HIGH severity and then corrected in the paper-locked numbers. Shrinkage excess +0.495 (80%) recommended off the slide.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-036

## Same study family
SF01 (repeat_runs_or_robustness): PAP-036, PAP-037, PAP-038
shared estimates 0.408 [0.378, 0.438], N=1,136 pairs; PAP-037 and PAP-038 rerun the same DiD with caliper and blowout filters | Paper 1 suppression DiD. TMP-001 and TMP-012 are later audits with a different method and stay separate.
