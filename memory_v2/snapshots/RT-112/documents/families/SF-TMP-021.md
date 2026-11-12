# FAM:SF-TMP-021 | Study family SF-TMP-021 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism E_unclear, no power information
- confidence: 0.65
- confidence_level: medium
- deciding_record: TMP-021
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: PLACEBO_DEPENDENCE
- validation_evidence: TMP-021: 'with clock>2:30, game x offense x period fe; 2->3 and 4->5+ placebos. any_fta 3->4 -0.151 vs placebos -5.556/-9.655; rim_pct +0'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-021 | Finding of SF-TMP-021: uncertain
- confidence: 0.65
- derived_from: EXP:TMP-021 {family=SF-TMP-021; rule=family member}
- statement: any_fta 3->4 -0.151 vs placebos -5.556/-9.655; rim_pct +0.015 vs +1.666/+2.077; pts +0.020.
- status: uncertain
- validation_status: same_pipeline_validation

# HYP:SF-TMP-021 | Hypothesis of SF-TMP-021
- addresses: RQC:RQC-176 {family=SF-TMP-021; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-TMP-021 {decided_by=TMP-021; family=SF-TMP-021; rule=automated adjudication stratum}
- source_record: TMP-021
- tested_by: EXP:TMP-021 {record=TMP-021; rule=family hypothesis tested by member record}
- text: Behavior changes when the defense enters the penalty (3->4 team fouls).
