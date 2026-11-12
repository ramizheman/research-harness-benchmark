# FAM:SF-APPA-055 | Study family SF-APPA-055 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: APPA-055
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_of_earlier_family: FAM:SF-APPA-054 {family=SF-APPA-055; order=before; rule=lexical similarity >= repeat threshold; similarity=0.358}
- risk_code: MECHANICAL_FLOOR
- validation_status: no_validation_recorded

# FIND:SF-APPA-055 | Finding of SF-APPA-055: supported
- confidence: 1.0
- derived_from: EXP:APPA-055 {family=SF-APPA-055; rule=family member}
- statement: PUTBACK Q1 d=-0.001 to Q4 d=-0.233, Q1->Q4 -0.232 (Q1 poss 722 / Q4 531). Other PTs suppress in Q1 already; largest other gradient DRIVE -0.060. CUT reverses +0.020. TRANSITION -0.053.
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-APPA-055 | Hypothesis of SF-APPA-055
- addresses: RQC:RQC-010 {family=SF-APPA-055; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: APPA-055
- supported_by: FIND:SF-APPA-055 {decided_by=APPA-055; family=SF-APPA-055; rule=automated adjudication stratum}
- tested_by: EXP:APPA-055 {record=APPA-055; rule=family hypothesis tested by member record}
- text: Only PUTBACK shows a fatigue signature (near-zero Q1 suppression compounding to Q4) across the full 30-star panel.
