# APPS-066: Brown DRIVE -> Tatum PNR sequential-premium placebo

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
The reported +0.326 Brown->Tatum PNR premium is Brown-specific, not any-teammate DRIVE->Tatum PNR.

## Design
99 BOS DRIVE->Tatum-PNR chains (Brown 43 / other 56). Placebo 5000 relabels; also league-wide teammate-DRIVE->PNR.

## Result
Reproduced premium +0.3262 n=43 vs Tatum PNR baseline 1.0459. Brown-other gap +0.3185, MW p=0.1702. Placebo 95% [-0.1389,+0.4192], observed inside, p=0.1136; perm p=0.2034. League teammate-DRIVE->PNR controlled beta=+0.0220 p=0.0044 n_t=20658 (tiny). Tatum any-teammate +0.1524 p=0.2546, perm inside.

## Failure evidence
Brown-specific +0.326 does not survive placebo; any teammate's DRIVE produces a comparable number. League effect is +0.02 PPP.

## Power and reliability
n=43 Brown chains; league n_t=20658

## Related
APPS-038; APPS-065

## Notes
Knowable: original n=43, t=+1.7 was already below |t|=2.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\brown_tatum_chain_placebo.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\teammate_drive_pnr.txt

## Related records (ids resolved to merged records)
APPS-038, APPS-065

## Also recorded as
CHT-031
