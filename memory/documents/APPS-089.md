# APPS-089: Connector on/off scoring vs structural load L (quadrants)

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-26 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: 
- Limitation tags: 
- Variable tags: structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Higher structural load L predicts higher adjusted on-off scoring among connectors.

## Design
102 connectors, >=150 on and off. Adj = within-team-season association with opp/period/margin/TALENT. Quadrants at median L=0.037 and median adj=0.10.

## Result
Corr(L, raw)=+0.013; Corr(L, adj)=+0.008. Quadrants ~25 each of highL-highScore / highL-lowScore / lowL-highScore / lowL-lowScore. Negative on/off n=49; 78% mechanism NONINITIATOR_TEAM_PATH (noninit_team_lift -3.52 vs +2.44 for positives).

## Failure evidence
L is uncorrelated with scoring impact (r=+0.008). High-L connectors split evenly into help and harm.

## Power and reliability
n=102

## Related
APPS-086

## Notes
Negative-connector harm is mostly teammate-path efficiency, not mix or initiator replacement.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_player_onoff_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_negative_mechanism_report.md

## Related records (ids resolved to merged records)
APPS-086
