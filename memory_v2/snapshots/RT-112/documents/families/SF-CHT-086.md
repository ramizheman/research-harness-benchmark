# FAM:SF-CHT-086 | Study family SF-CHT-086 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: mechanism C_artifact with verdict failed_gate
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-086
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPA-005 {family=SF-CHT-086; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-032 {family=SF-CHT-086; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-CHT-086; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- risk_code: RTM_SELECTION
- validation_status: no_validation_recorded

# FIND:SF-CHT-086 | Finding of SF-CHT-086: artifact
- confidence: 0.8
- derived_from: EXP:CHT-086 {family=SF-CHT-086; rule=family member}
- rules_out: HYP:SF-CHT-086 {family=SF-CHT-086; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: Label is mostly an RTM artifact. Apparent LLM skill was leakage; what survives is small/noisy; engine misses are selection/override not missing graph facts. Margin of LLM vs engine described as literally zero after leakage removal.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-086 | Hypothesis of SF-CHT-086
- addresses: RQC:RQC-148 {family=SF-CHT-086; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-086 {decided_by=CHT-086; family=SF-CHT-086; rule=automated adjudication stratum}
- source_record: CHT-086
- tested_by: EXP:CHT-086 {record=CHT-086; rule=family hypothesis tested by member record}
- text: An LLM layer can reason about suppression context beyond the engine, or predicting suppression from H1 is a viable label.
