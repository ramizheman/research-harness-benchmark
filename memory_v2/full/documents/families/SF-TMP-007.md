# FAM:SF-TMP-007 | Study family SF-TMP-007 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: artifact
- automated_substatus: verdict artifact_found
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-007
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPA-001 {family=SF-TMP-007; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPA-005 {family=SF-TMP-007; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPS-058 {family=SF-TMP-007; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-032 {family=SF-TMP-007; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-CHT-086 {family=SF-TMP-007; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-TMP-007; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: artifact
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-TMP-007 | Finding of SF-TMP-007: artifact
- confidence: 0.95
- derived_from: EXP:TMP-007 {family=SF-TMP-007; rule=family member}
- rules_out: HYP:SF-TMP-007 {family=SF-TMP-007; rule=stratum artifact: hypothesis ruled out as specified (scope: this design and data)}
- statement: 53.7% relabelled by calibration; PNR FG% by confidence bucket 0.0 (0.35), 0.949 (0.48), 0.898 (0.58); primary defender on floor 0.7259.
- status: artifact
- validation_status: no_validation_recorded

# HYP:SF-TMP-007 | Hypothesis of SF-TMP-007
- addresses: RQC:RQC-190 {family=SF-TMP-007; rule=TF-IDF question clustering; similarity_threshold=0.231}
- invalidated_by: FIND:SF-TMP-007 {decided_by=TMP-007; family=SF-TMP-007; rule=automated adjudication stratum}
- source_record: TMP-007
- tested_by: EXP:TMP-007 {record=TMP-007; rule=family hypothesis tested by member record}
- text: Graph play-type labels are outcome-independent descriptors.
