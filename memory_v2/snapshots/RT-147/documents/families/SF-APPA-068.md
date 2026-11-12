# FAM:SF-APPA-068 | Study family SF-APPA-068 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict abandoned
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-068
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: abandoned
- validation_evidence: APPA-068: 'pending]. spearman 0.54 and mae 0.0922 are copied from the holdout rank study, not computed here. placeholder preview, not a c'
- validation_status: same_pipeline_validation

# FIND:SF-APPA-068 | Finding of SF-APPA-068: untestable
- confidence: 0.95
- derived_from: EXP:APPA-068 {family=SF-APPA-068; rule=family member}
- statement: All sections [MODELED pending] / [DELTA pending] / [OBSERVED pending]. Spearman 0.54 and MAE 0.0922 are copied from the holdout rank study, not computed here.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-APPA-068 | Hypothesis of SF-APPA-068
- addresses: RQC:RQC-061 {family=SF-APPA-068; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-068 {decided_by=APPA-068; family=SF-APPA-068; rule=automated adjudication stratum}
- source_record: APPA-068
- tested_by: EXP:APPA-068 {record=APPA-068; rule=family hypothesis tested by member record}
- text: Pre-game vs halftime vs post-game pipeline runs on OKC-PHX Game 1 can be compared to observed stats.
