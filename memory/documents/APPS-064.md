# APPS-064: Gate 1: defensive assignment network modularity vs volume-schedule null

- Project: Strategy app
- Date: 2026-07-12 (mtime)
- Topic: Other / unclassified
- Pre-specified: yes
- Verdict: failed_gate
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Attacker-defender assignment networks have community structure beyond volume and schedule.

## Design
2023-24 RS. attackers=257 defenders=252 possessions=196782. Compare Q_obs to Q_null.

## Result
Q_obs=0.3838; Q_null=0.4300+-0.0010 range[0.4282,0.4324]; z=-46.85 p_emp=1.000. VERDICT: KILL ? no structure beyond volume+schedule.

## Failure evidence
Observed modularity is below the volume-schedule null (z=-46.85); gate instruction is do NOT lean on topology.

## Power and reliability
n=196782 possessions, 257x252

## Related
APPS-081

## Notes
gate2_reassignment_probe.py exists but no saved result file was found in sequence_memory/output.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\gate1_assignment_structure.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\gate1_assignment_structure.py

## Related records (ids resolved to merged records)
APPS-081
