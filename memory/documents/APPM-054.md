# APPM-054: Playoff adaptation-pair sustainability (12 pairs x 74 matchups)

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Pivoting to a listed counter after suppression sustains higher PPP than not pivoting, consistently across playoff matchups.

## Design
42,787 playoff possessions / 244 games / 74 directed matchups; 12 adaptation pairs; sustained_ppp vs non_pivot_ppp; CV<30% = CONSISTENT; |delta|>=0.10 = PIVOT_WINS/LOSES.

## Result
10/12 pairs CONSISTENT and within 0.10 of non-pivot (no PIVOT_WINS). PNR->PULL_UP sustained 1.069 vs non_pivot 1.224 (n_matchups=9) PIVOT_LOSES. DRIVE->PULL_UP 1.101 vs 1.217 (n=5) PIVOT_LOSES. Largest positive pair in the table: DRIVE->SPOT_UP 1.150 vs 1.098 (n=26). Shelf-life ~34-41 possessions.

## Failure evidence
Population deltas mostly |d|<0.10; two pairs with enough signal are PIVOT_LOSES (pivot worse than staying).

## Power and reliability
n=74 matchups; pair n_matchups 5 to 44

## Related
APPM-033 sequential premiums (abandoned); three-level sustainability

## Notes
_sustainability_all_playoffs_out.txt and _out2.txt are identical reruns (29166 bytes each). Sequential premiums were later removed from the deck as not holding up.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_sustainability_all_playoffs.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_sustainability_all_playoffs_out.txt
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_sustainability_all_playoffs_out2.txt
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_sustainability_mia_bos.py

## Related records (ids resolved to merged records)
APPM-033
