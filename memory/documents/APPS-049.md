# APPS-049: 52-series sequential adaptation: durable pivot branches and net swing

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
If-X-fails-then-Y pivot branches and PT net-swing (own PPP - opp next PPP) are durable across ~104 playoff team-offense units.

## Design
52 series, 104 units. Durable branch: median lift>0 and lift>0 in >=70% of units. Net swing per PT per unit.

## Result
durable_branches=[]. Median net swing: CUT +0.36 (neg in 9%), TRANSITION +0.26 (21%), PULL_UP +0.09 (33%), PNR +0.04 (45%), SPOT_UP +0.02 (40%), POST_UP -0.22 (77%), DRIVE -0.27 (88%). n_units: CUT 103, DRIVE/POST_UP/SPOT_UP/TRANSITION/PULL_UP 104, PUTBACK 47.

## Failure evidence
No conditional pivot branch met the durability bar (empty durable_branches). DRIVE/POST_UP negative net swing is the durable aftershock finding, recorded here as the positive half of the same run.

## Power and reliability
52 series, 104 units

## Related
APPS-050; APPS-037

## Notes
Verdict is for the pre-specified durable-branch test (null). The aftershock ranking of DRIVE/POST_UP is supported and used as the prior in the net-swing scorer.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\proof\sequential_adaptation_52series.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\sequential_adaptation_summary.json
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\NET_SWING_SCORING_PROTOTYPE.md

## Related records (ids resolved to merged records)
APPM-011, APPS-037
