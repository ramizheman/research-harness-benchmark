# FAM:SF-PAP-053 | Study family SF-PAP-053 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-053
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_order_unknown: FAM:SF24 {family=SF-PAP-053; order=unknown; rule=lexical similarity >= repeat threshold; similarity=0.403}
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: SAMPLE_SIZE_POWER
- validation_evidence: PAP-053: '148 spells; cross-fit deletion direction and counterfactual on random halves of p'
- validation_status: same_pipeline_validation

# FIND:SF-PAP-053 | Finding of SF-PAP-053: supported
- confidence: 1.0
- derived_from: EXP:PAP-053 {family=SF-PAP-053; rule=family member}
- statement: restoration mean +0.186 vs placebo +0.013, difference +0.173 [+0.085,+0.262]; 72% of spells R>0 vs 53% placebo; teammate response distance T 0.151 vs 0.139, diff +0.012 [-0.004,+0.030]; equal-size O excess +0.056 [+0.034,+0.080]
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-PAP-053 | Hypothesis of SF-PAP-053
- addresses: RQC:RQC-019 {family=SF-PAP-053; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-053
- supported_by: FIND:SF-PAP-053 {decided_by=PAP-053; family=SF-PAP-053; rule=automated adjudication stratum}
- tested_by: EXP:PAP-053 {record=PAP-053; rule=family hypothesis tested by member record}
- text: Teammates rebuild a detectable fraction of the deleted structural relationships relative to a no-absence placebo.
