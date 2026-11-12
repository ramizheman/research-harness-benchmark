# APPS-025: Adapt vs continue matched-pair overall-offense excess (post-hoc)

- Project: Strategy app
- Date: 2026-07-26 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Teams that abandon a suppressed play type (h2_n<=1) show a smaller matched-pair overall six-PT H1->H2 excess decline than teams that continue (h2_n>=5).

## Design
Exploratory, not pre-registered. Group A continue n=11064; Group B adapt n=810 (adapt rate 6.8%). Same-game opponent control, 0.10 H1-PPP caliper, game-cluster-robust SE.

## Result
Caliper 0.10: A excess +0.076 [+0.068,+0.084] n=3421 p=0; B excess +0.014 [-0.019,+0.046] n=255 p=0.386. Gap B-A = -0.062. Caliper sweep B CIs include 0 except 0.15.

## Failure evidence
Group B caliper-0.10 CI includes 0 (p=0.386, n=255 clusters=242); Group B is a reconstructed post-hoc cohort, not a validated successful-adaptation sample.

## Power and reliability
B n=255 pairs / 242 games at primary caliper

## Related
APPS-021; APPS-026

## Notes
Not a causal test of pivoting; outcome is six-PT aggregate PPP because suppressed-PT H2 PPP is undefined for abandoners.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\adapt_vs_continue_matched_results.md

## Related records (ids resolved to merged records)
APPS-021, APPS-026

## Also recorded as
CHT-066
