# APPS-093: Connector success vs failure commonality hunt

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-27 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: matched control
- Limitation tags: 
- Variable tags: play-type share / mix; structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Successful vs failing connectors share a structural signature, diet-gap match, or roster-load pattern.

## Design
Within-team n=102 (success=53 fail=49). Features: dA, team A, diet x gap, load HHI, n organizers, prototype similarity.

## Result
Within raw_success: L p=0.433; usage p=0.952; diet x gap p=0.399; n organizers p=0.975; talent_gap p=0.0122; adj_pts100 p=3.5e-18 (mechanical, it is the success label). proto sim p=0.0554 (wrong direction: fail med +0.676 vs success +0.279).

## Failure evidence
No structural/diet/roster feature separates success from failure once the tautological adj_pts100 split is set aside; talent_gap is the only other scalar with p<0.05.

## Power and reliability
n=102 (53/49)

## Related
APPS-086; APPS-090

## Notes
Looking like the average success prototype predicted worse Q_p in the ecosystem report as well.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_success_commonality_report.md

## Related records (ids resolved to merged records)
APPS-086, APPS-090
