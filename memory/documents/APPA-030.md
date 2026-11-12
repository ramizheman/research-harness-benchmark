# APPA-030: Play-type label backfill verification

- Project: Strategy app
- Date: 2026-05-24 (doc)
- Topic: Play-type labeling and data quality
- Pre-specified: yes
- Verdict: failed_gate
- Failure type: C_artifact
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: label or classification error
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Backfilled play-type labels match expected league distributions and team identities.

## Design
921,514 labelled possessions; band tests on PT shares, PNR cap, PPP sanity, temporal distribution, team identity and directional checks.

## Result
PNR 28.7% FAIL (band 20-28%); PULL_UP 7.9% FAIL; 3100 games with team PNR >33% FAIL; PNR PPP 0.948 PASS; temporal PASS; team identity FAIL; 2024-25 PULL_UP ~0-1% for many teams. Final: FAIL.

## Failure evidence
2024-25 PULL_UP shares 0.0-2.0% for many teams; 82.8% of PNR labels proxy_calibrated.

## Power and reliability
921,514 possessions

## Related


## Notes
Report says do not run adaptation analysis until resolved.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\BACKFILL_VERIFICATION.md
