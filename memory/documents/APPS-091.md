# APPS-091: Cut-share x load 2x2 connector PPP (id-keyed, after collision fix)

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-27 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: correlation
- Limitation tags: implementation bug
- Variable tags: PPP (points per possession); play-type share / mix; structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
High-CUT portable-diet connectors have higher on/off adj PPP, especially when combined with high load.

## Design
150 connector-seasons; merged on/off n=102 keyed by player_id (prior abbrev-name collision duplicated rows 102->109). Possession M1 HasHighCut etc.

## Result
Spearman(cut, adj) rho=-0.1269 p=0.204 n=102. HasHighCut=+0.59 p=0.293; HasLowCut=+1.39 p=0.117. 2x2 M1: HiCut x HiLoad -0.29 p=0.688 (portability x hub cell null/wrong-sign); HiCut x LoLoad +2.14 p=0.00248; LoCut x HiLoad +3.06 p=0.00162. Kruskal-Wallis adj p=0.191.

## Failure evidence
Cut-only still null after id-key fix. The cell that would confirm portability (HiCut x HiLoad) is null; significant cells are mixed/discordant and exploratory.

## Power and reliability
n=102 id-keyed; 150 connector-seasons

## Related
APPS-084; APPS-089

## Notes
Bug fix: J. Williams name collisions. Multiple-comparison + non-exclusive presence flags; authors say not a confirmed efficiency screen.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\cutshare_connector_ppp_report.md

## Related records (ids resolved to merged records)
APPS-084, APPS-089
