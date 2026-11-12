# EXP:APPS-089 | Connector on/off scoring vs structural load L (quadrants)
- date: 2026-07-26
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 102 connectors, >=150 on and off. Adj = within-team-season association with opp/period/margin/TALENT. Quadrants at median L=0.037 and median adj=0.10.
- hypothesis: Higher structural load L predicts higher adjusted on-off scoring among connectors.
- knowable_in_advance: unclear
- measures: VAR:structural_influence_load_L {record=APPS-089; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-089 {record=APPS-089; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Negative-connector harm is mostly teammate-path efficiency, not mix or initiator replacement.
- prespecified: no
- produced: RES:APPS-089 {record=APPS-089; rule=record fields}
- project: When a Hub Sits (Paper 2)
- related_as_recorded: APPS-086
- related_to: EXP:APPS-086 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-089; rule=date-ordered record link}
- reported_in: PAPER:When_a_Hub_Sits_manuscript {record=APPS-089; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_negative_mechanism_report.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_player_onoff_report.md
- title: Connector on/off scoring vs structural load L (quadrants)

# RES:APPS-089 | Result of APPS-089
- failure_evidence: L is uncorrelated with scoring impact (r=+0.008). High-L connectors split evenly into help and harm.
- failure_type: B_powered_null
- power_info: n=102
- primary_result: Corr(L, raw)=+0.013; Corr(L, adj)=+0.008. Quadrants ~25 each of highL-highScore / highL-lowScore / lowL-highScore / lowL-lowScore. Negative on/off n=49; 78% mechanism NONINITIATOR_TEAM_PATH (noninit_team_lift -3.52 vs +2.44 for positives).
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
