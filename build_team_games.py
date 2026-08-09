import pandas as pd


def build_team_games(matchups: pd.DataFrame) -> pd.DataFrame:
    home_rows = pd.DataFrame({
        "GAME_ID": matchups["GAME_ID"],
        "GAME_DATE": matchups["GAME_DATE"],
        "TEAM": matchups["HOME_TEAM"],
        "OPPONENT": matchups["AWAY_TEAM"],
        "IS_HOME": True,
        "PTS_FOR": matchups["HOME_PTS"],
        "PTS_AGAINST": matchups["AWAY_PTS"],
        "WIN": matchups["HOME_WIN"],
    })

    away_rows = pd.DataFrame({
        "GAME_ID": matchups["GAME_ID"],
        "GAME_DATE": matchups["GAME_DATE"],
        "TEAM": matchups["AWAY_TEAM"],
        "OPPONENT": matchups["HOME_TEAM"],
        "IS_HOME": False,
        "PTS_FOR": matchups["AWAY_PTS"],
        "PTS_AGAINST": matchups["HOME_PTS"],
        "WIN": 1 - matchups["HOME_WIN"],
    })

    team_games = pd.concat([home_rows, away_rows])
    team_games = team_games.sort_values(["TEAM", "GAME_DATE"])
    return team_games


def main():
    matchups = pd.read_csv("data/matchups.csv")
    team_games = build_team_games(matchups)
    team_games.to_csv("data/team_games.csv", index=False)
    print(f"Saved {len(team_games)} rows to data/team_games.csv")


if __name__ == "__main__":
    main()
