import pandas as pd
import matplotlib.pyplot as plt

games = pd.read_csv("synthetic_nfl_games.csv")
team = games.groupby(["season","team"], as_index=False).agg(
    wins=("win","sum"),
    games=("win","count"),
    points_for=("points_for","sum"),
    points_against=("points_against","sum")
)
team["win_pct"] = team["wins"]/team["games"]
team["point_diff"] = team["points_for"]-team["points_against"]

print("Correlations with win percentage:")
print(team[["win_pct","points_for","points_against","point_diff"]].corr()["win_pct"].sort_values(ascending=False))

team.to_csv("team_season_summary.csv", index=False)

latest = team[team["season"]==team["season"].max()].copy()
plt.figure(figsize=(9,6))
plt.scatter(latest["point_diff"], latest["win_pct"])
for _, r in latest.iterrows():
    plt.annotate(r["team"], (r["point_diff"], r["win_pct"]), xytext=(4,4),
                 textcoords="offset points")
plt.xlabel("Point Differential")
plt.ylabel("Win Percentage")
plt.title("Point Differential vs. Win Percentage")
plt.tight_layout()
plt.savefig("point_differential_vs_wins.png", dpi=180)
plt.close()
