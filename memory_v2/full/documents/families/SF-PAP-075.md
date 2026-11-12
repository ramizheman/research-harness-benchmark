# FAM:SF-PAP-075 | Study family SF-PAP-075 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-075
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-PAP-072 {family=SF-PAP-075; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.391}
- validation_evidence: PAP-075: '049, 0.252] mse +0.01%; f +0.139 [0.005, 0.274] mse +0.01%; validation e/f not significant (f negative); c vs m0 ~2.1 millinats an'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-075 | Finding of SF-PAP-075: rejected
- confidence: 1.0
- derived_from: EXP:PAP-075 {family=SF-PAP-075; rule=family member}
- rules_out: HYP:SF-PAP-075 {family=SF-PAP-075; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: offense test E +0.147 millinats [0.049, 0.252] MSE +0.01%; F +0.139 [0.005, 0.274] MSE +0.01%; validation E/F not significant (F negative); C vs M0 ~2.1 millinats and ~1.0% MSE
- status: rejected
- validation_status: same_pipeline_validation

# HYP:SF-PAP-075 | Hypothesis of SF-PAP-075
- addresses: RQC:RQC-069 {family=SF-PAP-075; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-075 {decided_by=PAP-075; family=SF-PAP-075; rule=automated adjudication stratum}
- source_record: PAP-075
- tested_by: EXP:PAP-075 {record=PAP-075; rule=family hypothesis tested by member record}
- text: In-game evidence improves prediction of subsequent performance under the actual rotation (Task 1).
