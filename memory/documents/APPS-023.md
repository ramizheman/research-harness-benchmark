# APPS-023: System BEST vs constrained league mix (non-CUT matchup-specificity test)

- Project: Strategy app
- Date: 2026-05-29 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: matched control
- Limitation tags: small sample; selection or regression to the mean
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Matchup-specific (non-CUT) BEST counters beat a feasibility-weighted league mix that ignores game state.

## Design
633 triggers, 55 series. A=BEST counter; B=constrained mix (SPOT_UP 35%/PULL_UP 25%/CUT 15%/DRIVE 9%/PNR 8%/POST_UP 8%); C=naive pivot; D=AVOID. One-sided MW A>B.

## Result
All BEST vs mix: 1.481 vs 1.212, gap=+0.269, p=0.0000, n=283. Non-CUT BEST vs mix: 1.216 vs 1.206, gap=+0.010, p=0.1709, n=136. L3_MATCHUP non-CUT: gap=+0.001, p=0.3277, n=47. BEST vs AVOID gap=+0.692, p=0.0000, n=169. 147/283 BEST are CUT (51.9%).

## Failure evidence
Key non-CUT test gap=+0.010, p=0.1709, n=136; H2H L3 non-CUT gap=+0.001, p=0.3277. Headline A vs B is CUT-driven.

## Power and reliability
n=136 non-CUT; n=47 L3 non-CUT

## Related
APPS-019; APPS-024

## Notes
Knowable: CUT is both 52% of BEST and in the constrained mix at 15%, so all-BEST vs mix cannot isolate matchup intelligence. Authors reframed contribution as trigger timing, not counter-selection.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\baseline_test_results.md

## Related records (ids resolved to merged records)
APPS-019, APPS-024
