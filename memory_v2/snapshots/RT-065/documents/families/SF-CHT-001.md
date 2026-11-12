# FAM:SF-CHT-001 | Study family SF-CHT-001 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict null, mechanism B_powered_null, no power information
- confidence: 0.8
- confidence_level: high
- deciding_record: CHT-001
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:leakage {family=SF-CHT-001; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- limited_by: LIM:small_sample {family=SF-CHT-001; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-PAP-095 {family=SF-CHT-001; order=before; rule=lexical similarity >= repeat threshold; similarity=0.382}
- risk_code: LEAKAGE_LOOKAHEAD
- validation_status: no_validation_recorded

# FIND:SF-CHT-001 | Finding of SF-CHT-001: uncertain
- confidence: 0.8
- derived_from: EXP:CHT-001 {family=SF-CHT-001; rule=family member}
- statement: Seed-only prior Brier 0.17614; raw LR 0.17637; isotonic 0.17280; +AA capped 0.17285; +seed cal alpha=0.4 0.17272.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-CHT-001 | Hypothesis of SF-CHT-001
- addresses: RQC:RQC-014 {family=SF-CHT-001; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-CHT-001 {decided_by=CHT-001; family=SF-CHT-001; rule=automated adjudication stratum}
- source_record: CHT-001
- tested_by: EXP:CHT-001 {record=CHT-001; rule=family hypothesis tested by member record}
- text: A 4-feature women's LR should beat a pure historical seed-prior; raw LR at ~0.176 looking worse than seed would mean the LR is a noisier seed model.
