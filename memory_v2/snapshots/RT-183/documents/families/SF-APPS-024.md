# FAM:SF-APPS-024 | Study family SF-APPS-024 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-024
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:low_power_large_MDE {family=SF-APPS-024; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPS-024; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- repeat_order_unknown: FAM:SF-APPS-023 {family=SF-APPS-024; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.503}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPS-024 | Finding of SF-APPS-024: untestable
- confidence: 0.95
- derived_from: EXP:APPS-024 {family=SF-APPS-024; rule=family member}
- statement: A mean=1.178 vs B_game 1.236 (gap=-0.058, p=0.6069) vs B_fixed 1.244 (gap=-0.066, p=0.2175) vs coach default C 1.134 (gap=+0.043, p=0.3052). MDE at 80% power ~0.180 PPP (SD~0.34).
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPS-024 | Hypothesis of SF-APPS-024
- addresses: RQC:RQC-007 {family=SF-APPS-024; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPS-024 {decided_by=APPS-024; family=SF-APPS-024; rule=automated adjudication stratum}
- source_record: APPS-024
- tested_by: EXP:APPS-024 {record=APPS-024; rule=family hypothesis tested by member record}
- text: When BEST=DRIVE (counter_h2_n>=5), observed DRIVE H2 PPP beats a feasibility-constrained baseline.
