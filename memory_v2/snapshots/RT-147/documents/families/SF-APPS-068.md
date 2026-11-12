# FAM:SF-APPS-068 | Study family SF-APPS-068 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: APPS-068
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:leakage {family=SF-APPS-068; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: LEAKAGE_LOOKAHEAD
- risk_code: MECHANICAL_FLOOR
- validation_evidence: APPS-068: '120 team-seasons. models a baseline / b pci-only / c full. oos test 2025-26. diagnostic net~ortg+leakage vs +offcontrol. a'
- validation_status: same_pipeline_validation

# FIND:SF-APPS-068 | Finding of SF-APPS-068: artifact
- confidence: 0.95
- derived_from: EXP:APPS-068 {family=SF-APPS-068; rule=family member}
- rules_out: HYP:SF-APPS-068 {family=SF-APPS-068; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: A R2=0.763 OOS 0.761; C R2=0.902 OOS 0.919; dR2=+0.139. Offensive-control components add +0.005 R2 beyond ORtg. Net~ORtg+leakage R2=0.948. corr(leakage, DRtg)=+0.894. PCI univariate r=+0.863 vs ORtg +0.866.
- status: artifact
- validation_status: same_pipeline_validation

# HYP:SF-APPS-068 | Hypothesis of SF-APPS-068
- addresses: RQC:RQC-090 {family=SF-APPS-068; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-APPS-068 {decided_by=APPS-068; family=SF-APPS-068; rule=automated adjudication stratum}
- source_record: APPS-068
- tested_by: EXP:APPS-068 {record=APPS-068; rule=family hypothesis tested by member record}
- text: PCI (halfcourt PPP + second-chance - TO - transition leakage) explains Net Rating beyond ORtg, Pace, and FGA/poss.
