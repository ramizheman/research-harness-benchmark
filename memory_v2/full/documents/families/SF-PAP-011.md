# FAM:SF-PAP-011 | Study family SF-PAP-011 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-011
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- repeat_of_earlier_family: FAM:SF-PAP-013 {family=SF-PAP-011; order=before; rule=lexical similarity >= repeat threshold; similarity=0.402}
- validation_status: no_validation_recorded

# FIND:SF-PAP-011 | Finding of SF-PAP-011: rejected
- confidence: 1.0
- derived_from: EXP:PAP-011 {family=SF-PAP-011; rule=family member}
- rules_out: HYP:SF-PAP-011 {family=SF-PAP-011; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: HasShaper +0.003 pts/100, t=0.004, p=0.996, CI[-1.37,+1.48]; n_SHAPER +1.17 pts/100 t=2.25 p~0.02 (not confirmed at 0.01)
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-011 | Hypothesis of SF-PAP-011
- addresses: RQC:RQC-062 {family=SF-PAP-011; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-011 {decided_by=PAP-011; family=SF-PAP-011; rule=automated adjudication stratum}
- source_record: PAP-011
- tested_by: EXP:PAP-011 {record=PAP-011; rule=family hypothesis tested by member record}
- text: Having any shaper on the floor raises PPP net of role counts and talent.
