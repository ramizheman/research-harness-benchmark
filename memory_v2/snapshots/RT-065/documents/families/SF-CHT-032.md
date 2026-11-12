# FAM:SF-CHT-032 | Study family SF-CHT-032 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 1.0
- confidence_level: high
- deciding_record: CHT-032
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPA-005 {family=SF-CHT-032; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-CHT-032; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-CHT-032 | Finding of SF-CHT-032: artifact
- confidence: 1.0
- derived_from: EXP:CHT-032 {family=SF-CHT-032; rule=family member}
- rules_out: HYP:SF-CHT-032 {family=SF-CHT-032; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: League-wide including calibrated PNR: +0.022 PPP, p=0.004 (n=20,658 vs 159,623). Tatum +0.152 p=0.27. Inferrer-only DRIVE-PNR ATT=-0.006, p=0.76.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-CHT-032 | Hypothesis of SF-CHT-032
- addresses: RQC:RQC-044 {family=SF-CHT-032; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-CHT-032 {decided_by=CHT-032; family=SF-CHT-032; rule=automated adjudication stratum}
- source_record: CHT-032
- tested_by: EXP:CHT-032 {record=CHT-032; rule=family hypothesis tested by member record}
- text: Any teammate DRIVE preceding a PNR raises PNR PPP.
