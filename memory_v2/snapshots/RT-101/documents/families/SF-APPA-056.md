# FAM:SF-APPA-056 | Study family SF-APPA-056 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-056
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: RTM_SELECTION
- validation_status: no_validation_recorded

# FIND:SF-APPA-056 | Finding of SF-APPA-056: untestable
- confidence: 1.0
- derived_from: EXP:APPA-056 {family=SF-APPA-056; rule=family member}
- statement: TRANSITION Q1 d=-0.221 (n=352) to Q4 d=-0.146 (n=262), gradient +0.075. PUTBACK compounds -0.067; POST_UP compounds -0.098. T. Young exception Q1 -0.023 to Q4 -0.240.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-056 | Hypothesis of SF-APPA-056
- addresses: RQC:RQC-059 {family=SF-APPA-056; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-056 {decided_by=APPA-056; family=SF-APPA-056; rule=automated adjudication stratum}
- source_record: APPA-056
- tested_by: EXP:APPA-056 {record=APPA-056; rule=family hypothesis tested by member record}
- text: For stars whose #1 sequential suppressor is TRANSITION (Tatum, Morant, Young, Haliburton), TRANSITION hits hardest in Q1 then adapts by Q4, unlike PUTBACK.
