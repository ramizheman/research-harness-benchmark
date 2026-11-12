# FAM:SF-PAP-015 | Study family SF-PAP-015 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 0.95
- confidence_level: high
- deciding_record: PAP-015
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-015 | Finding of SF-PAP-015: supported
- confidence: 0.95
- derived_from: EXP:PAP-015 {family=SF-PAP-015; rule=family member}
- statement: ON_COURT5 r_adj=0.582 (CI 0.484-0.665); INITIATED r_adj=0.509 (CI 0.407-0.608), shaper r 0.685; verdict MEANINGFULLY_WEAKER
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-015 | Hypothesis of SF-PAP-015
- addresses: RQC:RQC-161 {family=SF-PAP-015; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-015
- supported_by: FIND:SF-PAP-015 {decided_by=PAP-015; family=SF-PAP-015; rule=automated adjudication stratum}
- tested_by: EXP:PAP-015 {record=PAP-015; rule=family hypothesis tested by member record}
- text: The L-D_A correlation holds when both are computed on the same initiation-edge universe.
