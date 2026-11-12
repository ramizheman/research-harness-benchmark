# APPS-012: Defensive PPP allowed and possession share, RS vs playoffs

- Project: Strategy app
- Date: 2026-05-08 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Playoff defenses suppress DRIVE more than RS defenses (both lower PPP allowed and lower share).

## Design
25 defensive teams, min 30 poss per cell; RS vs playoff PPP allowed and opponent possession share by PT.

## Result
DRIVE allowed 1.191 -> 0.923 (-0.268), share 21.2% -> 18.2%; PNR -0.139, share +12.1pp; PULL_UP +0.341, share -7.6pp.

## Failure evidence
No inferential test; PNR share jump of +12.1pp may reflect tagging differences.

## Power and reliability
25 teams

## Related
Regular season vs playoff PPP by play type

## Notes
The PNR share jump (5.4% to 17.6%) is suspicious given the documented PNR tagger floor; flagged, not verified.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\_def_style_rs_vs_playoff.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\def_style_rs_playoff_run.log
