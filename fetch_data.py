"""
Downloads NBA game logs for a set of seasons and saves them to data/games.csv.

Run once to build the raw dataset. Re-run any time you want to refresh it
(e.g. to add a newly finished season).
"""

import time

import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

SEASONS = ["2021-22", "2022-23", "2023-24", "2024-25"]


def fetch_season(season: str) -> pd.DataFrame:
    print(f"Fetching {season}...")
    log = leaguegamelog.LeagueGameLog(season=season)
    return log.get_data_frames()[0]


def main():
    season_frames = []
    for season in SEASONS:
        season_frames.append(fetch_season(season))
        time.sleep(1)  # be polite to the API between calls

    all_games = pd.concat(season_frames, ignore_index=True)
    print(f"Total rows: {len(all_games)}")

    all_games.to_csv("data/games.csv", index=False)
    print("Saved to data/games.csv")


if __name__ == "__main__":
    main()
