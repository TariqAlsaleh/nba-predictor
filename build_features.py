import pandas as pd

def build_features(team_games: pd.DataFrame) -> pd.DataFrame:

    team_games["GAME_DATE"] = pd.to_datetime(team_games["GAME_DATE"])
    team_games["REST_DAYS"] = team_games.groupby("TEAM")["GAME_DATE"].diff().dt.days
    team_games["REST_DAYS"] = team_games["REST_DAYS"].clip(upper=7)

    team_games["RECENT_AVG_PTS"] = (
        team_games.groupby("TEAM")["PTS_FOR"]
        .transform(lambda scores: scores.shift(1).rolling(5).mean())
    )

    team_games["RECENT_AVG_PTS_AGAINST"] = (
        team_games.groupby("TEAM")["PTS_AGAINST"]
        .transform(lambda scores: scores.shift(1).rolling(5).mean())
    )

    team_games["RECENT_WIN_RATE"] = (
        team_games.groupby("TEAM")["WIN"]
        .transform(lambda scores: scores.shift(1).rolling(5).mean())
    )

    team_games["HEAD_TO_HEAD_WIN_RATE"] = (
        team_games.groupby(["TEAM", "OPPONENT"])["WIN"]
        .transform(lambda scores: scores.shift(1).expanding().mean())
    )

    return team_games


def main():
    team_games = pd.read_csv("data/team_games.csv")
    team_games = build_features(team_games)
    team_games.to_csv("data/team_features.csv", index=False)
    print(f"Saved {len(team_games)} rows to data/team_features.csv")


if __name__ == "__main__":
    main()
