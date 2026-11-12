# APPM-033: Sequential conditioning premiums (CUT->PULL_UP etc.)

- Project: Defensive Suppression
- Date: 2026-06-11 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: abandoned
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Specific play-type sequences carry a PPP premium (e.g. CUT->PULL_UP +0.065, PUTBACK->TRANSITION +0.084).

## Design
Sequence premium analyses (details in scripts, not read).

## Result
Premiums CUT->PULL_UP +0.065, PUTBACK->TRANSITION +0.084, Brown DRIVE->Tatum PNR +0.326 later removed: 'doesn't hold up'.

## Failure evidence
Slide notes 'Sequence premiums - Removed - doesn't hold up'; reason not stated in files read.

## Power and reliability


## Related
Superstar suppression Q5c

## Notes
Date approximated from v8 structure doc era; scripts dated 2026-05-31.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_STRUCTURE_v8.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_SLIDE_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_sequential_premium.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_sequential_premium_by_player.py
