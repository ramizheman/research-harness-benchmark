# FAM:SF-APPS-079 | Study family SF-APPS-079 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict reversed, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-079
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-079 | Finding of SF-APPS-079: rejected
- confidence: 0.95
- derived_from: EXP:APPS-079 {family=SF-APPS-079; rule=family member}
- rules_out: HYP:SF-APPS-079 {family=SF-APPS-079; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Total attributable +0.0614 AUC. outcome_persistence marginal +0.0527 (39% share) unique +0.0069; momentum +0.0494 unique 0; transition_state unique +0.0117 (53% of unique); playtype_state unique +0.0003; lineup_state unique -0.0049.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-079 | Hypothesis of SF-APPS-079
- addresses: RQC:RQC-034 {family=SF-APPS-079; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-079 {decided_by=APPS-079; family=SF-APPS-079; rule=automated adjudication stratum}
- source_record: APPS-079
- tested_by: EXP:APPS-079 {record=APPS-079; rule=family hypothesis tested by member record}
- text: Lag-1 predictive signal is process/state (pace, play type, transition) rather than outcome persistence.
