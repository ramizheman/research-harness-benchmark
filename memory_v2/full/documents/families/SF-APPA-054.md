# FAM:SF-APPA-054 | Study family SF-APPA-054 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism E_unclear
- confidence: 0.5
- confidence_level: medium
- deciding_record: APPA-054
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:insufficient_exposure {family=SF-APPA-054; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-APPA-054; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: supported
- repeated_by_later_family: FAM:SF-APPA-055 {family=SF-APPA-054; order=after; rule=lexical similarity >= repeat threshold; similarity=0.358}
- risk_code: EXPOSURE_SPARSITY
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-054 | Finding of SF-APPA-054: supported
- confidence: 0.5
- derived_from: EXP:APPA-054 {family=SF-APPA-054; rule=family member}
- statement: H1 delta -0.038 vs H2 -0.130 (22 stars, 3.4x). Q1 -0.009 vs Q4 -0.289 (11 stars; Q4 pooled n=34). PUTBACK H2 1.528 vs 1.217 (+0.311) n=8,614 vs 474,564. After opp PUTBACK offense 1.097 vs 1.210 (d=-0.113) n=15,898.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPA-054 | Hypothesis of SF-APPA-054
- addresses: RQC:RQC-010 {family=SF-APPA-054; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-054
- supported_by: FIND:SF-APPA-054 {decided_by=APPA-054; family=SF-APPA-054; rule=automated adjudication stratum}
- tested_by: EXP:APPA-054 {record=APPA-054; rule=family hypothesis tested by member record}
- text: PUTBACK suppresses the next star possession via fatigue (stronger in H2 and Q4), while PUTBACK itself remains high-value.
