library(tidyverse)

df <- read_csv("synthetic_college_basketball.csv", show_col_types = FALSE)

print(summary(df))

model <- lm(wins ~ points_per_game + opponent_points_per_game, data=df)
print(summary(model))

p <- ggplot(df, aes(points_per_game, wins)) +
  geom_point() +
  geom_smooth(method="lm", se=FALSE) +
  labs(
    title="Scoring vs. Wins in a Synthetic College Basketball Dataset",
    x="Points per Game",
    y="Wins"
  ) +
  theme_minimal()

ggsave("scoring_vs_wins.png", p, width=8, height=5, dpi=180)
