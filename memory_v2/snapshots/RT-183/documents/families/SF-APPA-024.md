# FAM:SF-APPA-024 | Study family SF-APPA-024 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict null
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-024
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPA-004 {family=SF-APPA-024; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPM-020 {family=SF-APPA-024; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:small_sample {family=SF-APPA-024; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- repeat_order_unknown: FAM:SF-APPM-020 {family=SF-APPA-024; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.385}
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPA-024: 'ootstrap ci, ols with mix-shift control; provisional tuning/holdout split. pearson r -0.032, ci [-0.283, +0.209]; spearman -0.0'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-024 | Finding of SF-APPA-024: untestable
- confidence: 0.95
- derived_from: EXP:APPA-024 {family=SF-APPA-024; rule=family member}
- statement: Pearson r -0.032, CI [-0.283, +0.209]; Spearman -0.067; OLS beta -5.33 (SE 19.64); clean subset r -0.079 (n=54); tuning fold +0.135, holdout -0.125.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPA-024 | Hypothesis of SF-APPA-024
- addresses: RQC:RQC-002 {family=SF-APPA-024; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-024 {decided_by=APPA-024; family=SF-APPA-024; rule=automated adjudication stratum}
- source_record: APPA-024
- tested_by: EXP:APPA-024 {record=APPA-024; rule=family hypothesis tested by member record}
- text: Teams whose playoff mix shifted toward the engine's recommended PT have higher series ORtg residuals.
