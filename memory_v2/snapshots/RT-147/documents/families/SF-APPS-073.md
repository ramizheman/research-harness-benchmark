# FAM:SF-APPS-073 | Study family SF-APPS-073 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-073
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- repeat_order_unknown: FAM:SF-CHT-029 {family=SF-APPS-073; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.43}
- validation_status: no_validation_recorded

# FIND:SF-APPS-073 | Finding of SF-APPS-073: artifact
- confidence: 0.95
- derived_from: EXP:APPS-073 {family=SF-APPS-073; rule=family member}
- rules_out: HYP:SF-APPS-073 {family=SF-APPS-073; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Global horizons: DRIVE/SPOT_UP/TRANSITION=5; others 0 (PNR/CUT/POST_UP/PUTBACK). SPOT_UP lag-1 lift +0.027 ctrl_p=0.0000. Within-team: all horizons 0 except SPOT_UP horizon(all)=1; PNR lag-1 within_team_lift=-0.0218.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-APPS-073 | Hypothesis of SF-APPS-073
- addresses: RQC:RQC-033 {family=SF-APPS-073; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-073 {decided_by=APPS-073; family=SF-APPS-073; rule=automated adjudication stratum}
- source_record: APPS-073
- tested_by: EXP:APPS-073 {record=APPS-073; rule=family hypothesis tested by member record}
- text: Running play type X raises the same team's next 1-5 possession PPP vs a matched baseline (action memory).
