import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("synthetic_player_stats.csv")

def score(group):
    cols=["points_per_game","games","peak_week"]
    for c in cols:
        s=group[c].std()
        group[c+"_z"]=(group[c]-group[c].mean())/(s if s else 1)
    group["consistency"] = group["points_per_game"]/(group["weekly_std"]+1)
    s=group["consistency"].std()
    group["consistency_z"]=(group["consistency"]-group["consistency"].mean())/(s if s else 1)
    group["scouting_score"] = (
        .40*group["points_per_game_z"] +
        .25*group["consistency_z"] +
        .20*group["games_z"] +
        .15*group["peak_week_z"]
    )
    return group

df=df.groupby("position", group_keys=False).apply(score)
df=df.sort_values("scouting_score", ascending=False)
df.to_csv("player_rankings.csv", index=False)

for pos in ["QB","RB","WR","TE"]:
    top=df[df.position==pos].head(10).sort_values("scouting_score")
    plt.figure(figsize=(9,5))
    plt.barh(top.player_name, top.scouting_score)
    plt.xlabel("Position-Adjusted Scouting Score")
    plt.title(f"Top {pos} Quantitative Profiles")
    plt.tight_layout()
    plt.savefig(f"top_{pos.lower()}_profiles.png", dpi=180)
    plt.close()

print(df[["player_name","position","scouting_score"]].head(15).to_string(index=False))
