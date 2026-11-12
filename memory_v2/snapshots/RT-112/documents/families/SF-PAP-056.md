# FAM:SF-PAP-056 | Study family SF-PAP-056 (single_record)
- adjudication_type: automated (rule-based); not independent human adjudication
- automated_stratum: rejected
- automated_substatus: verdict null, powered null with power information
- confidence: 1.0
- confidence_level: high
- deciding_record: PAP-056
- decision_rule: R0 single record
- failure_mechanism: B_powered_null
- family_kind: single_record
- knowable_before_outcome_auto: not_applicable
- mechanism_votes: B_powered_null=1
- members_disagree: no
- outcome_status: not_supported
- validation_status: no_validation_recorded

# FIND:SF-PAP-056 | Finding of SF-PAP-056: rejected
- confidence: 1.0
- derived_from: EXP:PAP-056 {family=SF-PAP-056; rule=family member}
- rules_out: HYP:SF-PAP-056 {family=SF-PAP-056; rule=stratum rejected: hypothesis ruled out as specified (scope: this design and data)}
- statement: profile match 19% (chance 14%); most minutes 3%; most initiations 5%; same position+minutes 7%; 0/6 high-load cases; 2/11 cases (both low-disruption); minutes-gainer during spell matches initiation gainer 66%
- status: rejected
- validation_status: no_validation_recorded

# HYP:SF-PAP-056 | Hypothesis of SF-PAP-056
- addresses: RQC:RQC-060 {family=SF-PAP-056; rule=TF-IDF question clustering; similarity_threshold=0.231}
- contradicted_by: FIND:SF-PAP-056 {decided_by=PAP-056; family=SF-PAP-056; rule=automated adjudication stratum}
- source_record: PAP-056
- tested_by: EXP:PAP-056 {record=PAP-056; rule=family hypothesis tested by member record}
- text: The teammate with the closest pre-absence initiation profile (or most minutes / initiations / same-position minutes) is the largest gainer in the absent player's primary types.
