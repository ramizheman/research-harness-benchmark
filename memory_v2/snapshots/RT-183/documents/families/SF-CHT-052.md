# FAM:SF-CHT-052 | Study family SF-CHT-052 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-052
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPA-005 {family=SF-CHT-052; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-032 {family=SF-CHT-052; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-086 {family=SF-CHT-052; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-CHT-052; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-CHT-052 | Finding of SF-CHT-052: uncertain
- confidence: 0.8
- derived_from: EXP:CHT-052 {family=SF-CHT-052; rule=family member}
- statement: mean sim ABSORBED +0.863 vs CASCADE +0.848; Spearman(sim, -gap)=-0.19 (wrong-signed). Embiid 23-24 cascades with Reed sim 0.94.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-CHT-052 | Hypothesis of SF-CHT-052
- addresses: RQC:RQC-127 {family=SF-CHT-052; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-CHT-052 {decided_by=CHT-052; family=SF-CHT-052; rule=automated adjudication stratum}
- source_record: CHT-052
- tested_by: EXP:CHT-052 {record=CHT-052; rule=family hypothesis tested by member record}
- text: Having a similar-profile teammate separates absorption from cascade when a player sits.
