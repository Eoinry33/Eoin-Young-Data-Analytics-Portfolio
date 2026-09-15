import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).parent / "nfl_2024_team_performance_attendance.csv"
df = pd.read_csv(DATA)

# The goal is not to say attendance causes winning. This project is descriptive:
# I am checking whether the two move together and where the exceptions are.
print(df.sort_values("wins", ascending=False)[
    ["team","wins","losses","point_diff_per_game","home_avg_attendance"]
].head(10))

print("\nCorrelations:")
print(df[["wins","point_diff_per_game","home_avg_attendance"]].corr())

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(df["point_diff_per_game"], df["wins"], alpha=.8)
for _, row in df.nlargest(8, "wins").iterrows():
    ax.annotate(row["team"], (row["point_diff_per_game"], row["wins"]),
                xytext=(5,5), textcoords="offset points", fontsize=8)
ax.set_xlabel("Point differential per game")
ax.set_ylabel("Regular-season wins")
ax.set_title("2024 NFL wins vs. scoring margin")
fig.tight_layout()
fig.savefig(Path(__file__).parent / "wins_vs_point_differential.png", dpi=180)
plt.close(fig)
