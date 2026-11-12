# APPS-075: Extended Possession Value (direct PPP + opponent T+1 suppression)

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: placebo or permutation test; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Play types and players have a real downstream (opponent next-PPP) component beyond direct PPP.

## Design
Exact match margin x period x season x focal team. Ext.Value = direct PPP + (-opp ATT). BH+placebo for downstream.

## Result
4/8 PTs downstream real: CUT Ext 1.658 (supp +0.0220), TRANSITION 1.509 (+0.0145), SPOT_UP 1.303 (+0.0124), POST_UP 1.127 (+0.0194). DRIVE downstream not real (opp ATT +0.0024). Player downstream mostly BH ns except M. McBride supp +0.1007 BH p=0.0000.

## Failure evidence
Downstream effects are small (~0.01-0.02 PPP) relative to direct PPP gaps; player list is mostly non-FINDING after BH.

## Power and reliability
PT-level n in the tens to hundreds of thousands implied by other seq files

## Related
APPS-037; APPS-049

## Notes
POST_UP has low direct PPP (1.107) but real downstream suppression, opposite of the 52-series negative net-swing ranking which uses own-PPP minus opp-next without this matching.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\epv.md

## Related records (ids resolved to merged records)
APPS-037, APPS-049
