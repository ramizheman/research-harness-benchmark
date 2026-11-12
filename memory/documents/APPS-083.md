# APPS-083: Fragility confirmatory: structural hubs distinct from usage

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-12 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 2
- Dataset tags: Box score and traditional stats
- Method tags: regression; correlation
- Limitation tags: 
- Variable tags: play-type share / mix; structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Offenses have identifiable structural hubs (F1a usage-decoupled; F1b load correlates with fragility) at full scale.

## Design
Gate PASS R2=0.399, rho=+0.829 n_players=112. Full team_seasons=120, season_players=1969.

## Result
F1a cosine R2=0.099 share=0.901 CI[0.778,0.954]; frobenius R2=0.084 share=0.916. F1b pooled rho=+0.670 p=0.0000 CI[+0.636,+0.705]; partial rho=+0.560 CI[+0.496,+0.616]. F1a=CONFIRMED F1b=CONFIRMED.

## Failure evidence
Both F1a and F1b confirmed at 120 team-seasons; hubs distinct from usage.

## Power and reliability
n=120 team-seasons; 1969 season-players

## Related
APPS-080

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\fragility_gate_result.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\fragility_full_result.txt

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-080

## Same study family
SF18 (repeat_runs_or_robustness): PAP-004, APPA-039
APPS-083 and PAP-004 share F1a R2=0.099 and F1b rho=+0.670 [0.636, 0.705]; APPA-039 is an earlier run (R2=0.094, rho=+0.685)
