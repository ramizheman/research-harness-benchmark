# FAM:SF-CHT-026 | Study family SF-CHT-026 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-026
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-CHT-026 | Finding of SF-CHT-026: uncertain
- confidence: 0.8
- derived_from: EXP:CHT-026 {family=SF-CHT-026; rule=family member}
- statement: Zero branches passed. The BOS-MIA PNR to PULL_UP dyad was matchup-specific.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-CHT-026 | Hypothesis of SF-CHT-026
- addresses: RQC:RQC-102 {family=SF-CHT-026; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-CHT-026 {decided_by=CHT-026; family=SF-CHT-026; rule=automated adjudication stratum}
- source_record: CHT-026
- tested_by: EXP:CHT-026 {record=CHT-026; rule=family hypothesis tested by member record}
- text: If PNR fail then PULL_UP is a real league-wide counter, it should show lift>0 in >=70% of units with median lift>2pp.
