r"""Fetch 2026-27 NBA per-game files into data_2026_27\, with a hard gate on the validation period.

  python scripts\14_fetch_2026_27.py --partition development [--max-games N]
  python scripts\14_fetch_2026_27.py --partition validation --registry runs\<exp>\claims.jsonl

Development: games dated D0 <= date < D1 (2026-10-20 to 2027-01-30), already played.
Validation: games dated D1 <= date <= D2; refused unless the claim registry verifies, is closed, and today is after D2.
The game list is requested with a date window, so results of validation-period games are never downloaded early.
Files written: data_2026_27\<partition>\game_list.json and <endpoint>_<game_id>.json. Existing files are kept.
"""
import argparse
import datetime as dt
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bench import challenges, claims, common  # noqa: E402

OUT = os.path.join(common.HB, "data_2026_27")
SEASON = "2026-27"


def window(partition, today, registry=None):
    """(date_from, date_to) inclusive for a partition, or raise PermissionError."""
    d0, d1, d2 = (dt.date.fromisoformat(x) for x in (challenges.D0, challenges.D1, challenges.D2))
    if partition == "development":
        return d0, min(d1 - dt.timedelta(days=1), today - dt.timedelta(days=1))
    if partition == "validation":
        ok, reasons = claims.release_allowed(registry or "", challenges.D2, today.isoformat())
        if not ok:
            raise PermissionError("validation period locked: " + "; ".join(reasons))
        return d1, d2
    raise ValueError(partition)


def in_window(game_date, lo, hi):
    d = dt.date.fromisoformat(str(game_date)[:10])
    return lo <= d <= hi


def fetch_list(lo, hi):
    from nba_api.stats.endpoints import LeagueGameFinder
    f = LeagueGameFinder(season_nullable=SEASON, league_id_nullable="00", season_type_nullable="Regular Season",
                         date_from_nullable=lo.strftime("%m/%d/%Y"), date_to_nullable=hi.strftime("%m/%d/%Y"), timeout=120)
    games = {}
    for _, r in f.get_data_frames()[0].iterrows():
        if not in_window(r["GAME_DATE"], lo, hi):
            continue
        g = games.setdefault(r["GAME_ID"], {"game_id": r["GAME_ID"], "date": str(r["GAME_DATE"]), "teams": []})
        g["teams"].append({"team": r["TEAM_ABBREVIATION"], "team_id": str(r["TEAM_ID"]), "pts": int(r["PTS"] or 0), "wl": r["WL"]})
    return sorted(games.values(), key=lambda g: (g["date"], g["game_id"]))


def endpoints():
    from nba_api.stats.endpoints import BoxScoreMatchupsV3, BoxScoreSummaryV2, BoxScoreTraditionalV3, GameRotation, PlayByPlayV3
    return {"pbp_v3": lambda g: PlayByPlayV3(game_id=g, timeout=60).get_dict(),
            "rotation": lambda g: GameRotation(game_id=g, timeout=60).get_dict(),
            "boxscore": lambda g: BoxScoreSummaryV2(game_id=g, timeout=60).get_dict(),
            "starters": lambda g: BoxScoreTraditionalV3(game_id=g, timeout=60).get_dict(),
            "matchups": lambda g: BoxScoreMatchupsV3(game_id=g, timeout=60).get_dict()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--partition", required=True, choices=["development", "validation"])
    ap.add_argument("--registry")
    ap.add_argument("--max-games", type=int)
    ap.add_argument("--sleep", type=float, default=1.0)
    a = ap.parse_args()
    lo, hi = window(a.partition, dt.date.today(), a.registry)
    if hi < lo:
        sys.exit("no completed games in the window yet")
    d = os.path.join(OUT, a.partition)
    os.makedirs(d, exist_ok=True)
    games = fetch_list(lo, hi)
    json.dump({"window": [lo.isoformat(), hi.isoformat()], "fetched": dt.datetime.now().isoformat(timespec="seconds"), "games": games},
              open(os.path.join(d, "game_list.json"), "w", encoding="utf-8"), indent=1)
    eps, n = endpoints(), 0
    for g in games[: a.max_games]:
        for name, fn in eps.items():
            p = os.path.join(d, f"{name}_{g['game_id']}.json")
            if os.path.exists(p):
                continue
            try:
                json.dump(fn(g["game_id"]), open(p, "w", encoding="utf-8"))
            except Exception as e:  # noqa: BLE001
                print(f"{g['game_id']} {name}: {e!r}"[:200])
            time.sleep(a.sleep)
        n += 1
    print(f"{a.partition}: {len(games)} games in {lo}..{hi}; processed {n}")


if __name__ == "__main__":
    main()
