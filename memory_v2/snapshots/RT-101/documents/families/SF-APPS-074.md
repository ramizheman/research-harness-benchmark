# FAM:SF-APPS-074 | Study family SF-APPS-074 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-074
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-APPS-074 | Finding of SF-APPS-074: rejected
- confidence: 0.95
- derived_from: EXP:APPS-074 {family=SF-APPS-074; rule=family member}
- rules_out: HYP:SF-APPS-074 {family=SF-APPS-074; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: All 8 creators horizon=0. Jokic lag-1 ATT=+0.0282 CI[-0.043,+0.099] p=0.3779. CLEAN NULL on teammate PPP. Secondary: Antetokounmpo +0.075 distinct initiators over next 3 poss (perm p=0.0002, BH 0.003) ? structure not efficiency.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-074 | Hypothesis of SF-APPS-074
- addresses: RQC:RQC-102 {family=SF-APPS-074; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-074 {decided_by=APPS-074; family=SF-APPS-074; rule=automated adjudication stratum}
- source_record: APPS-074
- tested_by: EXP:APPS-074 {record=APPS-074; rule=family hypothesis tested by member record}
- text: After an elite creator's signature action, teammates score more on the team's next k possessions with the same lineup on the floor.
