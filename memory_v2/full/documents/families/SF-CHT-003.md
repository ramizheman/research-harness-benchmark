# FAM:SF-CHT-003 | Study family SF-CHT-003 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: not_a_test
- automated_substatus: descriptive
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-003
- decision_rule: R0 no member is a hypothesis test
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: descriptive
- validation_evidence: CHT-003: 'leave-one-season-out; 2025 fold brier after the full adjustment stack. raw 2'
- validation_status: same_pipeline_validation

# HYP:SF-CHT-003 | Hypothesis of SF-CHT-003
- addresses: RQC:RQC-017 {family=SF-CHT-003; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: CHT-003
- tested_by: EXP:CHT-003 {record=CHT-003; rule=family hypothesis tested by member record}
- text: The stacked men's pipeline (blend of XGB+LR+LGB+Elo, isotonic, injury, AA, seed cal, blue-blood, top-seed, differential seed cal) is well calibrated on 2025 holdout.
