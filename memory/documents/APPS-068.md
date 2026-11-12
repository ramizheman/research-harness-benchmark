# APPS-068: Possession Control Index incremental R2 over ORtg (PCI is DRtg proxy)

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Structural roles and influence
- Pre-specified: partial
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Shot-level data with expected FG; Box score and traditional stats
- Method tags: regression; holdout, backtest or replay; correlation
- Limitation tags: leakage
- Variable tags: PPP (points per possession); net rating / ORtg
- Paper: 

## Hypothesis
PCI (halfcourt PPP + second-chance - TO - transition leakage) explains Net Rating beyond ORtg, Pace, and FGA/poss.

## Design
120 team-seasons. Models A baseline / B PCI-only / C full. OOS test 2025-26. Diagnostic Net~ORtg+leakage vs +offcontrol.

## Result
A R2=0.763 OOS 0.761; C R2=0.902 OOS 0.919; dR2=+0.139. Offensive-control components add +0.005 R2 beyond ORtg. Net~ORtg+leakage R2=0.948. corr(leakage, DRtg)=+0.894. PCI univariate r=+0.863 vs ORtg +0.866.

## Failure evidence
Headline PCI gain is leakage tracking DRtg (+0.89); offensive-control dR2=+0.005. Baseline omitted defense by construction (Net=ORtg-DRtg).

## Power and reliability
n=120 team-seasons; OOS 2025-26 30 teams

## Related
APPS-059

## Notes
Knowable: Net Rating already contains DRtg, so adding a leakage term that correlates 0.89 with DRtg must lift R2.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\pci_feature_importance_summary.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\pci_validation.py

## Related records (ids resolved to merged records)
APPS-059
