import pandas as pd
import numpy as np
from pathlib import Path

DATA = Path(__file__).parent / "nfl_2024_wr_evaluation.csv"
df = pd.read_csv(DATA)

features = [
    "target_share_pct",
    "catch_rate_pct",
    "yards_per_target",
    "td_rate_pct",
    "yards_per_game",
]

# Standardize within this 2024 comparison group.
for col in features:
    df[col + "_z"] = (df[col] - df[col].mean()) / df[col].std(ddof=0)

df["opportunity_efficiency_score"] = (
    .30 * df["target_share_pct_z"] +
    .20 * df["catch_rate_pct_z"] +
    .20 * df["yards_per_target_z"] +
    .15 * df["td_rate_pct_z"] +
    .15 * df["yards_per_game_z"]
)

df["score_0_100"] = 50 + 10 * df["opportunity_efficiency_score"]
df = df.sort_values("score_0_100", ascending=False)

df[[
    "player","team","targets","target_share_pct","catch_rate_pct",
    "yards_per_target","td_rate_pct","fantasy_points_per_game","score_0_100"
]].to_csv(Path(__file__).parent / "wr_evaluation_rankings.csv", index=False)

print(df.head(15).to_string(index=False))
