# FAM:SF-APPM-005 | Study family SF-APPM-005 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPM-005
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPA-021 {family=SF-APPM-005; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.359}
- validation_evidence: APPM-005: 'sweep k=5..5000 on 690 val / 520 holdout cells using actual usage mix; r2 raw and ols-calibrated on'
- validation_status: same_pipeline_validation

# FIND:SF-APPM-005 | Finding of SF-APPM-005: rejected
- confidence: 0.95
- derived_from: EXP:APPM-005 {family=SF-APPM-005; rule=family member}
- rules_out: HYP:SF-APPM-005 {family=SF-APPM-005; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Hypothesis REJECTED: k=5 R2 alone +0.018, k=50 +0.045, k=200 +0.058; best OLS R2 +0.0744 at k=500 (lift +0.0072 vs k=50). Actual-usage path R2 +0.045 vs equilibrium path +0.004.
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-APPM-005 | Hypothesis of SF-APPM-005
- addresses: RQC:RQC-026 {family=SF-APPM-005; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPM-005 {decided_by=APPM-005; family=SF-APPM-005; rule=automated adjudication stratum}
- source_record: APPM-005
- tested_by: EXP:APPM-005 {record=APPM-005; rule=family hypothesis tested by member record}
- text: Lowering SHRINKAGE_K in MatchupPPPModel recovers signal lost to over-shrinkage.
