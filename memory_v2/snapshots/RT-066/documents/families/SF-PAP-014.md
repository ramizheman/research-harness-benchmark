# FAM:SF-PAP-014 | Study family SF-PAP-014 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-014
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- repeat_of_earlier_family: FAM:SF-APPS-088 {family=SF-PAP-014; order=before; rule=lexical similarity >= repeat threshold; similarity=0.595}
- validation_status: no_validation_recorded

# FIND:SF-PAP-014 | Finding of SF-PAP-014: supported
- confidence: 1.0
- derived_from: EXP:PAP-014 {family=SF-PAP-014; rule=family member}
- statement: Delta D_A=+0.115, t=6.35, p~7e-9, shaper larger in 81% of pairs; Delta D_pi=+0.011 p~1e-4; r(L,D_A)=+0.60 (shapers +0.79)
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-014 | Hypothesis of SF-PAP-014
- addresses: RQC:RQC-013 {family=SF-PAP-014; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-014
- supported_by: FIND:SF-PAP-014 {decided_by=PAP-014; family=SF-PAP-014; rule=automated adjudication stratum}
- tested_by: EXP:PAP-014 {record=PAP-014; rule=family hypothesis tested by member record}
- text: Real on/off absence of a shaper displaces the team fingerprint more than a usage-matched non-shaper, and LOO L(p) tracks observed D_A.
