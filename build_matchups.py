"""
Reshapes data/games.csv (one row per team per game) into data/matchups.csv
(one row per game, with the home and away team's stats side by side).

Games with no clear home team (neutral-site games, e.g. NBA Cup finals,
international games) are dropped.
"""

import pandas as pd


def build_matchups(games: pd.DataFrame) -> pd.DataFrame:
    games = games.copy()
    games["IS_HOME"] = games["MATCHUP"].str.contains("vs.")

    home_counts = games.groupby("GAME_ID")["IS_HOME"].sum()
    valid_game_ids = home_counts[home_counts == 1].index
    games = games[games["GAME_ID"].isin(valid_game_ids)]

    home = games[games["IS_HOME"]]
    away = games[~games["IS_HOME"]]

    matchups = home.merge(
        away,
        on="GAME_ID",
        suffixes=("_HOME", "_AWAY"),
    )

    matchups = matchups.rename(columns={
        "GAME_DATE_HOME": "GAME_DATE",
        "SEASON_ID_HOME": "SEASON_ID",
        "TEAM_ABBREVIATION_HOME": "HOME_TEAM",
        "TEAM_ABBREVIATION_AWAY": "AWAY_TEAM",
        "PTS_HOME": "HOME_PTS",
        "PTS_AWAY": "AWAY_PTS",
    })

    matchups["HOME_WIN"] = (matchups["WL_HOME"] == "W").astype(int)

    matchups = matchups[[
        "GAME_ID", "GAME_DATE", "SEASON_ID",
        "HOME_TEAM", "AWAY_TEAM", "HOME_PTS", "AWAY_PTS", "HOME_WIN",
    ]]

    return matchups.sort_values("GAME_DATE").reset_index(drop=True)


def main():
    games = pd.read_csv("data/games.csv")
    matchups = build_matchups(games)
    print(f"Built {len(matchups)} matchups (dropped {games['GAME_ID'].nunique() - len(matchups)} neutral-site games)")
    matchups.to_csv("data/matchups.csv", index=False)
    print("Saved to data/matchups.csv")


if __name__ == "__main__":
    main()
