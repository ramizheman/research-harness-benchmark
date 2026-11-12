# FAM:SF-APPS-013 | Study family SF-APPS-013 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism E_unclear
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-013
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-013 | Finding of SF-APPS-013: uncertain
- confidence: 0.65
- derived_from: EXP:APPS-013 {family=SF-APPS-013; rule=family member}
- statement: SWITCH 0.294 -> 0.336 (+0.0426, 62% of teams); DROP 0.399 -> 0.343 (-0.0561); HELP 0.307 -> 0.321 (+0.0135, 'No meaningful shift').
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPS-013 | Hypothesis of SF-APPS-013
- addresses: RQC:RQC-050 {family=SF-APPS-013; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPS-013 {decided_by=APPS-013; family=SF-APPS-013; rule=automated adjudication stratum}
- source_record: APPS-013
- tested_by: EXP:APPS-013 {record=APPS-013; rule=family hypothesis tested by member record}
- text: Teams shift toward HELP/SWITCH and away from DROP in the playoffs, making RS DSI priors wrong.
