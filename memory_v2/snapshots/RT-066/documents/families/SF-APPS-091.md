# FAM:SF-APPS-091 | Study family SF-APPS-091 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-091
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:implementation_bug {family=SF-APPS-091; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: IMPLEMENTATION_BUG
- validation_status: no_validation_recorded

# FIND:SF-APPS-091 | Finding of SF-APPS-091: rejected
- confidence: 0.95
- derived_from: EXP:APPS-091 {family=SF-APPS-091; rule=family member}
- rules_out: HYP:SF-APPS-091 {family=SF-APPS-091; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: Spearman(cut, adj) rho=-0.1269 p=0.204 n=102. HasHighCut=+0.59 p=0.293; HasLowCut=+1.39 p=0.117. 2x2 M1: HiCut x HiLoad -0.29 p=0.688 (portability x hub cell null/wrong-sign); HiCut x LoLoad +2.14 p=0.00248; LoCut x HiLoad +3.06 p=0.00162. Kruskal-Wallis adj p=0.191.
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-APPS-091 | Hypothesis of SF-APPS-091
- addresses: RQC:RQC-124 {family=SF-APPS-091; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-APPS-091 {decided_by=APPS-091; family=SF-APPS-091; rule=automated adjudication stratum}
- source_record: APPS-091
- tested_by: EXP:APPS-091 {record=APPS-091; rule=family hypothesis tested by member record}
- text: High-CUT portable-diet connectors have higher on/off adj PPP, especially when combined with high load.
