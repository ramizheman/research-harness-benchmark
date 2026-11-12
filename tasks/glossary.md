# Terminology used in the research questions

This glossary is given identically in every condition. It defines terms only and reports no results. Definitions follow the published papers (Structural Influence; Detecting Defensive Suppression) where they exist.

- **Possession, PPP:** a team's continuous spell with the ball; PPP is points per possession.
- **H1, H2:** first half (periods 1 and 2) and second half (periods 3 and 4) of a game. RS and PO: regular season and playoffs.
- **Play type:** the label assigned to each possession by the project's rule-based classifier from play-by-play events. Labels include PNR (pick-and-roll ball handler), DRIVE, CUT, SPOT_UP, PULL_UP, POST_UP, PUTBACK and TRANSITION. A play-type mix is a team's share of possessions in each play type.
- **Initiator, initiation:** the offensive player whose action starts the possession's play type (for example the cutter on a cut, the ball handler on a pick-and-roll). Initiation records are possession-level rows linking initiator, play type and points.
- **Inferrer:** the classifier step that infers a play type (for example a pick-and-roll) from play-by-play text when it is not recorded directly.
- **Suppression trigger:** a team, play type and game in which the team's PPP on that play type falls sharply from H1 to H2 under fixed minimum-attempt rules; read as the defense possibly taking the action away.
- **Continuation, counter:** after a trigger, continuation means the offense keeps running the triggered play type; a counter is a different play type run instead.
- **BEST, AVOID (counter tiers):** the strategy app's matchup-ranked counter recommendations after a trigger. BEST is the top-ranked counter play type for that matchup, AVOID the lowest-ranked.
- **Structural fingerprint:** a team's standardized pattern of how play types share initiators.
- **Structural influence (load, L):** how much a team's structural fingerprint changes when one player's initiations are removed. L_pre is that quantity measured from games before an absence.
- **Usage:** a player's share of team possessions he initiates or finishes.
- **Role categories (Structural Influence paper):** by crossing usage (above or below the rotation median) with residual influence (structural influence beyond what usage predicts): Primary Organizer (high usage, positive residual), Shaper (low usage, positive residual), Terminal Scorer (high usage, residual at or below zero), Role Occupant or Specialist (low usage, residual at or below zero).
- **Connector:** a structural-role label used in later studies for players whose presence links teammates' play types; the exact rule varied between studies.
- **Hub:** a high-structural-influence player around whom a team's initiations are organized.
- **Absence spell:** a run of consecutive games a player misses (the main studies used at least 15).
- **Displacement (D_real):** how far teammates' play-type mix moves during an absence spell relative to before it (one minus the cosine similarity of the two mixes).
- **Mover, decoy:** a mover is a player who changed teams between seasons; decoys are comparison players used as placebo matches for a mover.
- **Stint:** an interval of play with the same ten players on the court.
- **Garbage time:** late-game possessions with a lopsided score, usually excluded.
