# FAM:SF-TMP-002 | Study family SF-TMP-002 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-002
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-002: 'ent-paired did, caliper pairs, h1 pseudo-event; within-unit permutation nulls b=1000 and within-h2 b=200; k=3..6. k=4 d1 theta=-0.0'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-002 | Finding of SF-TMP-002: rejected
- confidence: 0.95
- derived_from: EXP:TMP-002 {family=SF-TMP-002; rule=family member}
- rules_out: HYP:SF-TMP-002 {family=SF-TMP-002; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: k=4 D1 theta=-0.0098 se=0.0047, perm null mean -0.0055, one-sided p=0.8601; D2 theta=-0.0000 p=0.4615; d2cal_k4 -0.0271 p=0.6553; all k p>=0.13.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-TMP-002 | Hypothesis of SF-TMP-002
- addresses: RQC:RQC-062 {family=SF-TMP-002; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-TMP-002 {decided_by=TMP-002; family=SF-TMP-002; rule=automated adjudication stratum}
- source_record: TMP-002
- tested_by: EXP:TMP-002 {record=TMP-002; rule=family hypothesis tested by member record}
- text: After an early-H2 slump (first k H2 possessions >=0.25 PPP below H1), the offense underperforms a cross-fitted shrinkage forecast for the rest of H2 beyond a permutation null.
