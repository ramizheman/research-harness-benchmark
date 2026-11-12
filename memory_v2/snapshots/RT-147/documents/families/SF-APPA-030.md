# FAM:SF-APPA-030 | Study family SF-APPA-030 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: uncertain
- automated_substatus: inadequately tested: verdict failed_gate, mechanism C_artifact
- confidence: 0.8
- confidence_level: high
- deciding_record: APPA-030
- decision_rule: R0 single record
- failure_mechanism: C_artifact
- family_kind: single_record
- knowable_basis: earlier family (date order certain) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history
- limitation_precedent: FAM:SF-APPA-001 {family=SF-APPA-030; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPA-005 {family=SF-APPA-030; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-APPS-058 {family=SF-APPA-030; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:label_or_classification_error {family=SF-APPA-030; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: C_artifact=1
- members_disagree: no
- outcome_status: not_supported
- risk_code: LABEL_ERROR
- validation_status: no_validation_recorded

# FIND:SF-APPA-030 | Finding of SF-APPA-030: uncertain
- confidence: 0.8
- derived_from: EXP:APPA-030 {family=SF-APPA-030; rule=family member}
- statement: PNR 28.7% FAIL (band 20-28%); PULL_UP 7.9% FAIL; 3100 games with team PNR >33% FAIL; PNR PPP 0.948 PASS; temporal PASS; team identity FAIL; 2024-25 PULL_UP ~0-1% for many teams. Final: FAIL.
- status: uncertain
- validation_status: no_validation_recorded

# HYP:SF-APPA-030 | Hypothesis of SF-APPA-030
- addresses: RQC:RQC-014 {family=SF-APPA-030; rule=TF-IDF question clustering; similarity_threshold=0.231}
- left_open_by: FIND:SF-APPA-030 {decided_by=APPA-030; family=SF-APPA-030; rule=automated adjudication stratum}
- source_record: APPA-030
- tested_by: EXP:APPA-030 {record=APPA-030; rule=family hypothesis tested by member record}
- text: Backfilled play-type labels match expected league distributions and team identities.
