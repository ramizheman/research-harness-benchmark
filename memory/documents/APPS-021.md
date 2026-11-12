# APPS-021: Cost of ignoring suppression (continue suppressed PT in H2)

- Project: Strategy app
- Date: 2026-05-29 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NCAA tournament and ratings data
- Method tags: 
- Limitation tags: small sample; low power / large MDE
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
When a suppression trigger fires and teams keep running the suppressed play type, H2 PPP on that PT is materially below H1.

## Design
735 suppression events, 271 games; Group A h2_n>=3 (n=683) vs Group B h2_n<=1 (n=31). Canonical deck uses trigger CSV H1/H2 n>=5 (633 PO / 2779 RS).

## Result
Group A: H1 1.522 -> post-trigger 0.876, cost 0.646 PPP/poss, 5.16 pts/trigger (t=48.172, p=0.0000, n=683). Pivot vs continue overall H2 1.074 vs 1.043, MW p=0.2642. Locked row-mean (n>=5): H1 1.48->H2 0.85, drop 0.63, 5.4 pts/trigger, n=633 PO / 2779 RS; full-graph drop 0.619 (n=11087).

## Failure evidence
One-sample t on (h1-h2) p=0.0000 n=683; pivoting overall-H2 advantage not significant (p=0.2642, n_B=31).

## Power and reliability
n=683 Group A; n=31 Group B underpowered for pivot vs continue

## Related
APPS-022; APPS-025

## Notes
Do not cite poss-weighted cost 0.646 on slides; locked methodology is trigger row-mean drop 0.63. Win rates 48.8% vs 48.4% are indistinguishable.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cost_of_ignoring_results.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\COHERENT_NUMBERS.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
PAP-036, APPS-025

## Same study family
SF02 (duplicate_records): APPA-040, PAP-039, CHT-040
shared 683 continued of 735 events, H1 1.522 to H2 0.876, cost 0.646; CHT-040 reports the pivot-vs-continue test from the same run (t=48.172, n=683)
