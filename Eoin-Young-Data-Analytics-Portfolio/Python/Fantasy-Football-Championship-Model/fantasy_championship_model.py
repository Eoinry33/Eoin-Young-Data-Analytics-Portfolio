import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

df = pd.read_csv("synthetic_fantasy_teams.csv")

features = [
    "top8_points", "avg_weekly_points", "weekly_std",
    "top8_peak", "depth_score"
]
X = df[features]
y = df["championship_contender"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=.25, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=400, random_state=42, class_weight="balanced"
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:,1]

print(f"Holdout accuracy: {accuracy_score(y_test, pred):.3f}")
print(f"Holdout ROC-AUC: {roc_auc_score(y_test, prob):.3f}")
print(classification_report(y_test, pred))

df["contender_score"] = model.predict_proba(X)[:,1]
rankings = df.sort_values("contender_score", ascending=False)
rankings.to_csv("contender_rankings.csv", index=False)

importance = pd.Series(model.feature_importances_, index=features).sort_values()
plt.figure(figsize=(9,5))
importance.plot(kind="barh")
plt.title("Fantasy Championship Model — Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=180)
plt.close()

top = rankings.head(12).sort_values("contender_score")
plt.figure(figsize=(9,6))
plt.barh(top["team_id"].astype(str), top["contender_score"])
plt.xlabel("Contender Score")
plt.title("Top Fantasy Team Profiles")
plt.tight_layout()
plt.savefig("contender_scores.png", dpi=180)
plt.close()

print("\nTop 10 contender profiles:")
print(rankings[["team_id","season","contender_score"]].head(10).to_string(index=False))
