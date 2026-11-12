# FAM:SF-TMP-006 | Study family SF-TMP-006 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-006
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-006: 'd h1-h2 difference on 1/n1+1/n2; 100 within-unit half-label permutations; strata by 3-pt share. pull_up intercept +0.0366 (tausd 0.'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-006 | Finding of SF-TMP-006: rejected
- confidence: 0.95
- derived_from: EXP:TMP-006 {family=SF-TMP-006; rule=family member}
- rules_out: HYP:SF-TMP-006 {family=SF-TMP-006; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: PULL_UP intercept +0.0366 (tauSD 0.191) vs perm mean +0.0110 [-0.0757,+0.1107]; all play types inside permutation interval.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-TMP-006 | Hypothesis of SF-TMP-006
- addresses: RQC:RQC-189 {family=SF-TMP-006; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-TMP-006 {decided_by=TMP-006; family=SF-TMP-006; rule=automated adjudication stratum}
- source_record: TMP-006
- tested_by: EXP:TMP-006 {record=TMP-006; rule=family hypothesis tested by member record}
- text: PULL_UP's large H1->H2 true-change variance is real rather than produced by heterogeneous noise.
