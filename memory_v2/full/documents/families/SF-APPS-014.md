# FAM:SF-APPS-014 | Study family SF-APPS-014 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict reversed, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-014
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-014 | Finding of SF-APPS-014: rejected
- confidence: 0.95
- derived_from: EXP:APPS-014 {family=SF-APPS-014; rule=family member}
- rules_out: HYP:SF-APPS-014 {family=SF-APPS-014; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Game 1 DRIVE 0.864 (n=323) -> 0.942 (n=346), +0.078; all games 0.880 (n=1746) -> 0.973 (n=1987), +0.093.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-014 | Hypothesis of SF-APPS-014
- addresses: RQC:RQC-120 {family=SF-APPS-014; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-014 {decided_by=APPS-014; family=SF-APPS-014; rule=automated adjudication stratum}
- source_record: APPS-014
- tested_by: EXP:APPS-014 {record=APPS-014; rule=family hypothesis tested by member record}
- text: DRIVE efficiency drops within a single playoff game (defense moves first) before cross-game adaptation.
