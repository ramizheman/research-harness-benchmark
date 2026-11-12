# FAM:SF-PAP-062 | Study family SF-PAP-062 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict failed_gate, mechanism E_unclear
- confidence: 0.7
- confidence_level: medium
- deciding_record: PAP-062
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:multiple_testing {family=SF-PAP-062; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF26 {family=SF-PAP-062; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.405}
- risk_code: MULTIPLE_TESTING
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-062 | Finding of SF-PAP-062: uncertain
- confidence: 0.7
- derived_from: EXP:PAP-062 {family=SF-PAP-062; rule=family member}
- statement: Y1 Delta R2_oos=+0.035 CI[-0.058,+0.117] perm p=0.010 Holm p=0.030; R2 0.121->0.156; Delta rho +0.02; Y2 Delta R2=-0.016 CI[-0.124,+0.053] p=0.71
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-PAP-062 | Hypothesis of SF-PAP-062
- addresses: RQC:RQC-020 {family=SF-PAP-062; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-PAP-062 {decided_by=PAP-062; family=SF-PAP-062; rule=automated adjudication stratum}
- source_record: PAP-062
- tested_by: EXP:PAP-062 {record=PAP-062; rule=family hypothesis tested by member record}
- text: Adding L_pre to conventional features raises held-out R2 of displacement (bootstrap CI excluding 0 and perm passing Holm).
