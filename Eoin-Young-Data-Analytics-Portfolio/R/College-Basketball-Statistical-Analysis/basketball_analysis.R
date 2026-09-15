library(tidyverse)

df <- read_csv("college_basketball_2023_24_profiles.csv", show_col_types = FALSE)

df <- df %>%
  mutate(
    win_pct = wins / (wins + losses),
    scoring_margin_proxy = points_per_game - 70
  )

print(summary(df))

cor_scoring <- cor(df$points_per_game, df$win_pct)
cor_ortg <- cor(df$offensive_rating, df$win_pct)

cat("Correlation: points per game vs win percentage =", round(cor_scoring, 3), "\n")
cat("Correlation: offensive rating vs win percentage =", round(cor_ortg, 3), "\n")

ggplot(df, aes(x = points_per_game, y = win_pct)) +
  geom_point() +
  geom_smooth(method = "lm", se = TRUE) +
  labs(
    title = "Scoring vs winning percentage",
    x = "Points per game",
    y = "Win percentage"
  ) +
  theme_minimal()

ggplot(df, aes(x = offensive_rating, y = win_pct)) +
  geom_point() +
  geom_smooth(method = "lm", se = TRUE) +
  labs(
    title = "Offensive rating vs winning percentage",
    x = "Offensive rating",
    y = "Win percentage"
  ) +
  theme_minimal()
