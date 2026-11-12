# FAM:SF-PAP-072 | Study family SF-PAP-072 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict failed_gate, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-072
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-PAP-075 {family=SF-PAP-072; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.391}
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: PAP-072: 'd test +0.104 millinats [-0.012, 0.219] with opposite-sign validation; task 2 mse changes -0.14% to +0.01% vs 1% threshold feasib'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-072 | Finding of SF-PAP-072: rejected
- confidence: 1.0
- derived_from: EXP:PAP-072 {family=SF-PAP-072; rule=family member}
- rules_out: HYP:SF-PAP-072 {family=SF-PAP-072; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: NO-GO; no Task 2 99% lower bound >0; closest offense D test +0.104 millinats [-0.012, 0.219] with opposite-sign validation; Task 2 MSE changes -0.14% to +0.01% vs 1% threshold
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-072 | Hypothesis of SF-PAP-072
- addresses: RQC:RQC-069 {family=SF-PAP-072; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-072 {decided_by=PAP-072; family=SF-PAP-072; rule=automated adjudication stratum}
- source_record: PAP-072
- tested_by: EXP:PAP-072 {record=PAP-072; rule=family hypothesis tested by member record}
- text: Models D/E/F (actual-points, process, or all in-game evidence) beat model C on Task 2 weighted test (99% CI>0 and >=1% MSE drop).
