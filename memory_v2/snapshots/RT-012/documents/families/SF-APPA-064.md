# FAM:SF-APPA-064 | Study family SF-APPA-064 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: untestable
- automated_substatus: mechanism A_unanswerable with verdict inconclusive
- confidence: 0.95
- confidence_level: high
- deciding_record: APPA-064
- decision_rule: R0 single record
- failure_mechanism: A_unanswerable
- family_kind: single_record
- knowable_before_outcome_auto: no_evidence
- limited_by: LIM:small_sample {family=SF-APPA-064; level=unclear (sample size or power, data scarcity not stated); rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: A_unanswerable=1
- members_disagree: no
- outcome_status: inconclusive
- risk_code: SAMPLE_SIZE_POWER
- validation_status: no_validation_recorded

# FIND:SF-APPA-064 | Finding of SF-APPA-064: untestable
- confidence: 0.95
- derived_from: EXP:APPA-064 {family=SF-APPA-064; rule=family member}
- statement: Final SAS 114-OKC 127. SAS CUT 9 poss 1.67 vs H2H 1.59 CORRECT; SAS PNR 22 poss 0.95 vs 0.94 MIXED (LP AVOID). OKC CUT 1 poss 2.00 vs 1.69 CORRECT but 1% mix vs plan. OKC PNR 19 poss 1.26 vs 1.11 (AVOID but above H2H). Live: both teams ~65-71% PULL_UP, CUT 1-5%.
- status: untestable
- validation_status: no_validation_recorded

# HYP:SF-APPA-064 | Hypothesis of SF-APPA-064
- addresses: RQC:RQC-048 {family=SF-APPA-064; rule=TF-IDF question clustering; similarity_threshold=0.231}
- found_untestable_by: FIND:SF-APPA-064 {decided_by=APPA-064; family=SF-APPA-064; rule=automated adjudication stratum}
- source_record: APPA-064
- tested_by: EXP:APPA-064 {record=APPA-064; rule=family hypothesis tested by member record}
- text: The LP-equilibrium opener (CUT) and AVOID (PNR) match realized efficiency in WCF Game 5 SAS @ OKC (0042500315).
