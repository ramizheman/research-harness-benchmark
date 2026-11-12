# FAM:SF-PAP-007 | Study family SF-PAP-007 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: supported
- automated_substatus: mechanism D_positive
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-007
- decision_rule: R0 single record
- failure_mechanism: D_positive
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- limited_by: LIM:confounding {family=SF-PAP-007; level=design; rule=LIMIT_RULES on power_info, failure_evidence, notes}
- mechanism_votes: D_positive=1
- members_disagree: no
- outcome_status: supported
- risk_code: CONFOUNDING
- validation_status: no_validation_recorded

# FIND:SF-PAP-007 | Finding of SF-PAP-007: supported
- confidence: 1.0
- derived_from: EXP:PAP-007 {family=SF-PAP-007; rule=family member}
- statement: Shaper: CUT +1.353pp (sd 1.434), PNR +0.98pp, SPOT_UP -1.248pp, DRIVE -0.542pp; Organizer POST_UP +2.331pp
- status: supported
- validation_status: no_validation_recorded

# HYP:SF-PAP-007 | Hypothesis of SF-PAP-007
- addresses: RQC:RQC-140 {family=SF-PAP-007; rule=TF-IDF question clustering; similarity_threshold=0.231}
- source_record: PAP-007
- supported_by: FIND:SF-PAP-007 {decided_by=PAP-007; family=SF-PAP-007; rule=automated adjudication stratum}
- tested_by: EXP:PAP-007 {record=PAP-007; rule=family hypothesis tested by member record}
- text: Teams run more cuts/PNR and fewer spot-ups/drives when a shaper is on the floor.
