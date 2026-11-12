# FAM:SF-PAP-095 | Study family SF-PAP-095 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-095
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeated_by_later_family: FAM:SF-CHT-001 {family=SF-PAP-095; order=after; rule=lexical similarity >= repeat threshold; similarity=0.387}
- validation_status: no_validation_recorded

# FIND:SF-PAP-095 | Finding of SF-PAP-095: supported
- confidence: 1.0
- derived_from: EXP:PAP-095 {family=SF-PAP-095; rule=family member}
- statement: Version B OOF Brier ~0.13664 (improvement <0.002, user chose to keep); 2nd-stage isotonic 0.13776 vs 0.13664 reverted
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-095 | Hypothesis of SF-PAP-095
- addresses: RQC:RQC-015 {family=SF-PAP-095; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-095
- supported_by: FIND:SF-PAP-095 {decided_by=PAP-095; family=SF-PAP-095; rule=automated adjudication stratum}
- tested_by: EXP:PAP-095 {record=PAP-095; rule=family hypothesis tested by member record}
- text: Adding efficiency features with an XGB+LR ensemble improves women's OOF Brier enough to keep.
