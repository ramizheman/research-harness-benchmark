# APPA-040: Cost of ignoring suppression: continue rate and points lost

- Project: Defensive Suppression
- Date: 2026-05-29 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: label or classification error
- Variable tags: 
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
After a suppression trigger, teams keep running the suppressed play at near-H1 volume and lose several points per event.

## Design
55-series graph; Group A h2_n>=3 vs Group B h2_n<=1; within-game H1 vs H2 on suppressed PT; points decomposition via _points_not_ppp.py. RS confirm _rs_continue_rate.py.

## Result
PO: 735 events; Group A 683 (93%) H1 1.522 to H2 0.876, cost/poss 0.646, ~8.2 H2 poss, ~97% H1 volume, ~5.4 pts/trigger; real actionable ~6.1 pts (5.3 keep-calling + 0.8 AVOID vs BEST). RS continue 93.1% (2,949/3,169); no-floor 94.1%.

## Failure evidence
93% continue at ~97% of H1 volume; blowout-filtering continue rate is a volume-threshold artifact (78.8% at |margin|<=20) so the paper cites unfiltered 93%/94.9%.

## Power and reliability
683 Group A PO triggers; 3,169 RS events

## Related
APPA-036; APPA-037

## Notes
H1 PPP floor=1.0 in cost/continue scripts but not in the trigger table; removing it changes continue 94.9% to 94.1%. Oracle ceiling 11.1 pts is labeled projection.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-036, APPA-037

## Same study family
SF02 (duplicate_records): APPS-021, PAP-039, CHT-040
shared 683 continued of 735 events, H1 1.522 to H2 0.876, cost 0.646; CHT-040 reports the pivot-vs-continue test from the same run (t=48.172, n=683)
