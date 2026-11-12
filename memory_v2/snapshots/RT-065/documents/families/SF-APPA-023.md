# FAM:SF-APPA-023 | Study family SF-APPA-023 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-023
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:insufficient_exposure {family=SF-APPA-023; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: EXPOSURE_SPARSITY
- validation_evidence: APPA-023: '870 train cells (386,675 poss); shrinkage k sweep 25-1000; holdout r2. best k=500 r2_hol +0.1192 vs +0.1150 baseline; lift +0.'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-023 | Finding of SF-APPA-023: rejected
- confidence: 0.95
- derived_from: EXP:APPA-023 {family=SF-APPA-023; rule=family member}
- rules_out: HYP:SF-APPA-023 {family=SF-APPA-023; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Best k=500 R2_hol +0.1192 vs +0.1150 baseline; lift +0.0042; w_pt negative (-1.4014).
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPA-023 | Hypothesis of SF-APPA-023
- addresses: RQC:RQC-072 {family=SF-APPA-023; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPA-023 {decided_by=APPA-023; family=SF-APPA-023; rule=automated adjudication stratum}
- source_record: APPA-023
- tested_by: EXP:APPA-023 {record=APPA-023; rule=family hypothesis tested by member record}
- text: Per-PT team-pair interaction deltas add R2 over the 8-feature baseline (ship if lift > +0.005).
