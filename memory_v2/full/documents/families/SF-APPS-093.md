# FAM:SF-APPS-093 | Study family SF-APPS-093 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-093
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-APPS-093 | Finding of SF-APPS-093: rejected
- confidence: 0.95
- derived_from: EXP:APPS-093 {family=SF-APPS-093; rule=family member}
- rules_out: HYP:SF-APPS-093 {family=SF-APPS-093; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Within raw_success: L p=0.433; usage p=0.952; diet x gap p=0.399; n organizers p=0.975; talent_gap p=0.0122; adj_pts100 p=3.5e-18 (mechanical, it is the success label). proto sim p=0.0554 (wrong direction: fail med +0.676 vs success +0.279).
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-093 | Hypothesis of SF-APPS-093
- addresses: RQC:RQC-054 {family=SF-APPS-093; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-093 {decided_by=APPS-093; family=SF-APPS-093; rule=automated adjudication stratum}
- source_record: APPS-093
- tested_by: EXP:APPS-093 {record=APPS-093; rule=family hypothesis tested by member record}
- text: Successful vs failing connectors share a structural signature, diet-gap match, or roster-load pattern.
