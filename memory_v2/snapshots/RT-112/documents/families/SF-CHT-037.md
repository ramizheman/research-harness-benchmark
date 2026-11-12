# FAM:SF-CHT-037 | Study family SF-CHT-037 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict null
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-037
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPS-073 {family=SF-CHT-037; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-029 {family=SF-CHT-037; rule=knowability: earlier family with overlapping limitation}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-CHT-029 {family=SF-CHT-037; order=before; rule=lexical similarity >= repeat threshold; similarity=0.365}
- validation_status: no_validation_recorded

# FIND:SF-CHT-037 | Finding of SF-CHT-037: artifact
- confidence: 0.8
- derived_from: EXP:CHT-037 {family=SF-CHT-037; rule=family member}
- rules_out: HYP:SF-CHT-037 {family=SF-CHT-037; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Lag-1 real, lag-2 small, lag-3+ ~0: d(1)=+0.024 AUC, d(2)=+0.004. SPOT_UP lag-1 MWU_p=0.0000 with and without controls. DRIVE lag-1 MWU_p=0.0000 but ctrl_p=0.0911. PNR naive p=0.031, controlled 0.136, within-team lift -0.021.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-037 | Hypothesis of SF-CHT-037
- addresses: RQC:RQC-013 {family=SF-CHT-037; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-037 {decided_by=CHT-037; family=SF-CHT-037; rule=automated adjudication stratum}
- source_record: CHT-037
- tested_by: EXP:CHT-037 {record=CHT-037; rule=family hypothesis tested by member record}
- text: Naive lag-1 play-type PPP effects survive period/clock/margin controls and within-team baselines.
