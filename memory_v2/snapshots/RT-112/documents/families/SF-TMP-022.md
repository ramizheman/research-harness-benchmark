# FAM:SF-TMP-022 | Study family SF-TMP-022 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-022
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:insufficient_exposure {family=SF-TMP-022; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-TMP-022; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF-CHT-076 {family=SF-TMP-022; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.624}
- risk_code: EXPOSURE_SPARSITY
- validation_status: no_validation_recorded

# FIND:SF-TMP-022 | Finding of SF-TMP-022: supported
- confidence: 0.95
- derived_from: EXP:TMP-022 {family=SF-TMP-022; rule=family member}
- statement: rim_pct big_tr +1.903 (SE 0.468, t=+4.1); any_fta -6.320 (t=-17.3); pts -0.020 (SE 0.011).
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-TMP-022 | Hypothesis of SF-TMP-022
- addresses: RQC:RQC-016 {family=SF-TMP-022; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: TMP-022
- supported_by: FIND:SF-TMP-022 {decided_by=TMP-022; family=SF-TMP-022; rule=automated adjudication stratum}
- tested_by: EXP:TMP-022 {record=TMP-022; rule=family hypothesis tested by member record}
- text: Offenses attack the rim when an opposing big is in foul trouble.
