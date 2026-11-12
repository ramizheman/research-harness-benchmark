# FAM:SF-PAP-094 | Study family SF-PAP-094 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-094
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: DRIFT_NONSTATIONARITY
- validation_status: no_validation_recorded

# FIND:SF-PAP-094 | Finding of SF-PAP-094: supported
- confidence: 1.0
- derived_from: EXP:PAP-094 {family=SF-PAP-094; rule=family member}
- statement: rd2+goto_conversion method was wrong (goto Brier much worse); rd6 normalization ~0.11 combined 2025 as fallback; variable/new alpha beat pure model (log examples ~0.157 vs ~0.159; new alpha ~0.156 combined)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-094 | Hypothesis of SF-PAP-094
- addresses: RQC:RQC-044 {family=SF-PAP-094; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-094
- supported_by: FIND:SF-PAP-094 {decided_by=PAP-094; family=SF-PAP-094; rule=automated adjudication stratum}
- tested_by: EXP:PAP-094 {record=PAP-094; rule=family hypothesis tested by member record}
- text: Blending the model with betting-derived goto (2024-25) and 538 (2016-23) round-specific win probabilities beats pure model on scored (no play-in) Brier.
