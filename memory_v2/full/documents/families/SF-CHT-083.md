# FAM:SF-CHT-083 | Study family SF-CHT-083 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict failed_gate
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-083
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-TMP-012 {family=SF-CHT-083; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:insufficient_exposure {family=SF-CHT-083; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: EXPOSURE_SPARSITY
- validation_status: no_validation_recorded

# FIND:SF-CHT-083 | Finding of SF-CHT-083: untestable
- confidence: 1.0
- derived_from: EXP:CHT-083 {family=SF-CHT-083; rule=family member}
- statement: Median 3 possessions per lineup pair.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-CHT-083 | Hypothesis of SF-CHT-083
- addresses: RQC:RQC-154 {family=SF-CHT-083; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-CHT-083 {decided_by=CHT-083; family=SF-CHT-083; rule=automated adjudication stratum}
- source_record: CHT-083
- tested_by: EXP:CHT-083 {record=CHT-083; rule=family hypothesis tested by member record}
- text: Specific offensive-five vs defensive-five matchups can be scored as a unit of analysis.
