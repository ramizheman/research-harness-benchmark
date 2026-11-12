# FAM:SF-APPA-022 | Study family SF-APPA-022 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-022
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_status: no_validation_recorded

# FIND:SF-APPA-022 | Finding of SF-APPA-022: supported
- confidence: 0.95
- derived_from: EXP:APPA-022 {family=SF-APPA-022; rule=family member}
- statement: Late: blended k=30 worse on 5/5 metrics (R2 -0.1065 vs -0.0866). Early: blended better 5/5 (R2 -0.2624 vs -0.4508; win-side 55.8% vs 52.5%). k sweep recommends k~5.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPA-022 | Hypothesis of SF-APPA-022
- addresses: RQC:RQC-071 {family=SF-APPA-022; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-022
- supported_by: FIND:SF-APPA-022 {decided_by=APPA-022; family=SF-APPA-022; rule=automated adjudication stratum}
- tested_by: EXP:APPA-022 {record=APPA-022; rule=family hypothesis tested by member record}
- text: Blending prior seasons helps early season without hurting late season.
