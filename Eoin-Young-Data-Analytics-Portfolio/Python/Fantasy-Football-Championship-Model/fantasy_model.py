import pandas as pd
from pathlib import Path
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).parent / "nfl_2024_wr_fantasy_model_data.csv"
df = pd.read_csv(DATA)

features = ["targets","catch_rate_pct","yards_per_target","receiving_tds","games"]
target = "fantasy_points_per_game"

model = Pipeline([
    ("scale", StandardScaler()),
    ("ridge", Ridge(alpha=1.0))
])

model.fit(df[features], df[target])
df["model_predicted_fppg"] = model.predict(df[features])
df["residual"] = df[target] - df["model_predicted_fppg"]

print(df[[
    "player","fantasy_points_per_game","model_predicted_fppg","residual"
]].sort_values("fantasy_points_per_game", ascending=False).to_string(index=False))

df.to_csv(Path(__file__).parent / "model_predictions.csv", index=False)
