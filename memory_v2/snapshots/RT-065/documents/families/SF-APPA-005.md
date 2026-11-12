# FAM:SF-APPA-005 | Study family SF-APPA-005 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-005
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPA-001 {family=SF-APPA-005; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-APPA-005; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-APPA-005 | Finding of SF-APPA-005: untestable
- confidence: 0.95
- derived_from: EXP:APPA-005 {family=SF-APPA-005; rule=family member}
- statement: Within-game change 319/523 (61.0%); cross-game change 298/440 (67.7%); 103/104 units (99.0%) and 52/52 series show a change; transition matrices near-uniform.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-005 | Hypothesis of SF-APPA-005
- addresses: RQC:RQC-064 {family=SF-APPA-005; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-005 {decided_by=APPA-005; family=SF-APPA-005; rule=automated adjudication stratum}
- source_record: APPA-005
- tested_by: EXP:APPA-005 {record=APPA-005; rule=family hypothesis tested by member record}
- text: Playoff defenses change scheme within games and between games, especially after the opponent ran a play type heavily.
