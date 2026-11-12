# FAM:SF-PAP-028 | Study family SF-PAP-028 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism E_unclear
- confidence: 0.5
- confidence_level: medium
- deciding_record: PAP-028
- decision_rule: R0 single record
- failure_mechanism: E_unclear
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:small_sample {family=SF-PAP-028; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: E_unclear=1
- members_disagree: no
- outcome_status: supported
- repeat_of_earlier_family: FAM:SF-APPS-088 {family=SF-PAP-028; order=before; rule=lexical similarity >= repeat threshold; similarity=0.427}
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-PAP-028 | Finding of SF-PAP-028: supported
- confidence: 0.5
- derived_from: EXP:PAP-028 {family=SF-PAP-028; rule=family member}
- statement: Delta=+0.078, p~0.026
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-028 | Hypothesis of SF-PAP-028
- addresses: RQC:RQC-044 {family=SF-PAP-028; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-028
- supported_by: FIND:SF-PAP-028 {decided_by=PAP-028; family=SF-PAP-028; rule=automated adjudication stratum}
- tested_by: EXP:PAP-028 {record=PAP-028; rule=family hypothesis tested by member record}
- text: Connectors show larger on/off D_A than usage-matched terminal scorers.
