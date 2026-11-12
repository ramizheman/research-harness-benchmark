# FAM:SF-PAP-073 | Study family SF-PAP-073 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-073
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:low_measurement_reliability {family=SF-PAP-073; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: MEASURE_RELIABILITY
- validation_evidence: PAP-073: 'eups >=200 poss); defense a 0.06, b 0.11, c 0.13; team-game split-half a -0.11 ci[-0.14,-0.09] detecting 10 per 100 at 2 se needs'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-073 | Finding of SF-PAP-073: rejected
- confidence: 1.0
- derived_from: EXP:PAP-073 {family=SF-PAP-073; rule=family member}
- rules_out: HYP:SF-PAP-073 {family=SF-PAP-073; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: lineup-season offense k: A 1,448 vs B 132 / C 126; corr later A: A 0.21, B -0.04, C 0.03 (304 lineups >=200 poss); defense A 0.06, B 0.11, C 0.13; team-game split-half A -0.11 CI[-0.14,-0.09]
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-073 | Hypothesis of SF-PAP-073
- addresses: RQC:RQC-174 {family=SF-PAP-073; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-073 {decided_by=PAP-073; family=SF-PAP-073; rule=automated adjudication stratum}
- source_record: PAP-073
- tested_by: EXP:PAP-073 {record=PAP-073; rule=family hypothesis tested by member record}
- text: Expected shot/possession value is more reliable than actual points and better predicts later actual points.
