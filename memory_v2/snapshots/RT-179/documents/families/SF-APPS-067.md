# FAM:SF-APPS-067 | Study family SF-APPS-067 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-067
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_evidence: APPS-067: 'matching primary; sensitivity match on own offense. bh-fdr+placebo+ft-clean. prev_made control. 3/64 finding cells survive bot'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-067 | Finding of SF-APPS-067: supported
- confidence: 0.95
- derived_from: EXP:APPS-067 {family=SF-APPS-067; rule=family member}
- statement: 3/64 FINDING cells survive both matchings: SPOT_UP->TRANSITION ATT=-0.085; POST_UP->TRANSITION -0.083; PNR->DRIVE -0.058 (all also survive +prev_made). PULL_UP->DRIVE dropped as defense-quality confound.
- status: supported
- validation_status: same_pipeline_validation

# HYP:SF-APPS-067 | Hypothesis of SF-APPS-067
- addresses: RQC:RQC-041 {family=SF-APPS-067; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPS-067
- supported_by: FIND:SF-APPS-067 {decided_by=APPS-067; family=SF-APPS-067; rule=automated adjudication stratum}
- tested_by: EXP:APPS-067 {record=APPS-067; rule=family hypothesis tested by member record}
- text: The opponent's previous play type changes your next-possession PPP after matching on defensive team.
