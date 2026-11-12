# FAM:SF-TMP-038 | Study family SF-TMP-038 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict abandoned
- confidence: 0.95
- confidence_level: high
- deciding_record: TMP-038
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_basis: earlier family (by recorded point dates) with overlapping limitation
- knowable_before_outcome_auto: yes_from_history_probable
- limitation_precedent: FAM:SF-APPS-085 {family=SF-TMP-038; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-TMP-016 {family=SF-TMP-038; rule=knowability: earlier family with overlapping limitation}
- limitation_precedent: FAM:SF-TMP-024 {family=SF-TMP-038; rule=knowability: earlier family with overlapping limitation}
- limited_by: LIM:low_measurement_reliability {family=SF-TMP-038; level=data; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: abandoned
- risk_code: DRIFT_NONSTATIONARITY
- risk_code: MEASURE_RELIABILITY
- validation_evidence: TMP-038: '0, still below ~270. g3 analog: yy=25 inferrer data dropped split-half from 0.32 to ~0.00. research_assessment (generated november'
- validation_status: same_pipeline_validation

# FIND:SF-TMP-038 | Finding of SF-TMP-038: untestable
- confidence: 0.95
- derived_from: EXP:TMP-038 {family=SF-TMP-038; rule=family member}
- statement: Neo4j/raw files: yy=20 and yy=21 have 0 games. API: 1,080 (yy=20) and 1,230 (yy=21) game IDs. gamerotation ~15% success (2/13 yy=20 games; timeouts). PBP roster proxy 11.4 players per team-game (range 9-15) on a 30-game sample. Uncalibrated 15-game play-type sample vs yy=22: PNR 17.2%/15.0% vs 21.9%; SPOT_UP 29.3%/29.1% vs 21.7%. 10-game subType PNR ~0 events both seasons. Projected spells yy=21 ~42-52, yy=20 ~33-45; yy=21+22-24 ~190-200, still below ~270. G3 analog: yy=25 inferrer data dropped split-half from 0.32 to ~0.00.
- status: untestable
- validation_status: same_pipeline_validation

# HYP:SF-TMP-038 | Hypothesis of SF-TMP-038
- addresses: RQC:RQC-197 {family=SF-TMP-038; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-TMP-038 {decided_by=TMP-038; family=SF-TMP-038; rule=automated adjudication stratum}
- source_record: TMP-038
- tested_by: EXP:TMP-038 {record=TMP-038; rule=family hypothesis tested by member record}
- text: Reconstructed 2020-21 and 2021-22 possession data can enlarge the 148-spell pool toward ~270 spells and improve restoration-predictor power without breaking play-type comparability.
