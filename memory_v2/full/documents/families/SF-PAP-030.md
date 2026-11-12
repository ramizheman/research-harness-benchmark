# FAM:SF-PAP-030 | Study family SF-PAP-030 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-030
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: MECHANICAL_FLOOR
- validation_status: no_validation_recorded

# FIND:SF-PAP-030 | Finding of SF-PAP-030: rejected
- confidence: 0.95
- derived_from: EXP:PAP-030 {family=SF-PAP-030; rule=family member}
- rules_out: HYP:SF-PAP-030 {family=SF-PAP-030; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: eligible 653/882; corr(D_A, n_on) all=-0.475 vs eligible=-0.036; eligible median D_A=0.0529, median dPPP_allowed=-0.298; corr(D_A, dPPP_allowed)=+0.020; quadrants ~161-166 each
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-030 | Hypothesis of SF-PAP-030
- addresses: RQC:RQC-167 {family=SF-PAP-030; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-030 {decided_by=PAP-030; family=SF-PAP-030; rule=automated adjudication stratum}
- source_record: PAP-030
- tested_by: EXP:PAP-030 {record=PAP-030; rule=family hypothesis tested by member record}
- text: Defenders who displace the opponent's initiation fingerprint (high D_A) also suppress opponent PPP.
