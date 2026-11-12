# APPS-063: Test 4: foul-trouble sequencing after star 2nd Q1/Q2 foul

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Other / unclassified
- Pre-specified: yes
- Verdict: null
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: placebo or permutation test; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix; free throws / fouls
- Paper: 

## Hypothesis
Opponent PPP rises on the next 1-3 possessions after a star's 2nd personal foul in Q1/Q2.

## Design
2104 qualifying events. Exact match period x margin x season x offensive team. FT possessions excluded after first-pass artifact.

## Result
Including FT: lag-1 ATT=+0.204 CI[+0.163,+0.245] (artifact: FT share 41.8% vs 9.9%). Excluding FT: lag-1 +0.0486 [-0.0060,+0.0991] perm p=0.0655; lag-2 -0.0192; lag-3 -0.0272. No lag clears CI+perm+placebo.

## Failure evidence
Headline +0.204 was FT-possession coding; clean lag-1 +0.049 does not clear the pre-specified bars.

## Power and reliability
n_treated lag-1=2101

## Related
APPS-061

## Notes
Knowable: a 2nd foul is often a shooting foul, so lag-1 includes FT trips unless excluded. On-floor vs benched not verifiable.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\test_4_foul_trouble.md

## Related records (ids resolved to merged records)
APPS-061

## Same study family
SF15 (duplicate_records): CHT-035
shared raw lag-1 +0.204 with 41.8% FT share | Verdicts differ: null vs artifact_found.
