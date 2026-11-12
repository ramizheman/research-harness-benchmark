# FAM:SF-APPS-034 | Study family SF-APPS-034 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: not_a_test
- automated_substatus: descriptive
- confidence: 0.65
- confidence_level: medium
- deciding_record: APPS-034
- decision_rule: R0 no member is a hypothesis test
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-APPS-034; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: descriptive
- repeat_order_unknown: FAM:SF-APPM-032 {family=SF-APPS-034; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.39}
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: APPS-034: 'rs holdout best rows n>=5 (980). ablate min_n gate and top-k rotation'
- validation_status: same_pipeline_validation

# HYP:SF-APPS-034 | Hypothesis of SF-APPS-034
- addresses: RQC:RQC-033 {family=SF-APPS-034; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-034
- tested_by: EXP:APPS-034 {record=APPS-034; rule=family hypothesis tested by member record}
- text: Routing regret (+0.137 baseline) is not an artifact of low-volume bench oracles.
