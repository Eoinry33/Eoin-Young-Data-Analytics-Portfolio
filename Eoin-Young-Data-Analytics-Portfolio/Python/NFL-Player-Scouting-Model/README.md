# NFL WR Opportunity & Efficiency Model — 2024

## The idea

I did not want to make another project that says “player X had the most yards, so player X is the best.”

For a scouting or fantasy-style evaluation, I think the more interesting question is **what kind of production is being created from the opportunities a player receives?**

This project creates a simple 0–100 WR evaluation score using real 2024 NFL data.

It is not meant to replace scouting. It is a way to organize a first pass through a large group of players and identify profiles worth a closer look.

## The question

Which 2024 wide receivers combined:

- meaningful target volume,
- reliable hands,
- yards created per target,
- touchdown production,
- and consistent yardage per game?

## Data

The dataset contains 23 notable 2024 WRs and was built from publicly available season statistics.

Variables include:

- Targets
- Target share
- Receptions
- Receiving yards
- Receiving TDs
- Games
- PPR fantasy points
- PPR fantasy points per game

Derived metrics:

- Catch rate
- Yards per target
- TD rate
- Yards per game
- Standardized component scores

Sources:
- FantasyPros 2024 WR statistics: https://www.fantasypros.com/nfl/stats/wr.php?year=2024
- Pro-Football-Reference 2024 receiving: https://www.pro-football-reference.com/years/2024/receiving.htm
- NFL.com player receiving stats: https://www.nfl.com/stats/player-stats/category/receiving/2024/reg/all/receivingtarget/desc

## How the score works

I used a weighted composite instead of simply copying a fantasy ranking.

| Component | Weight |
|---|---:|
| Target share | 30% |
| Catch rate | 20% |
| Yards per target | 20% |
| TD rate | 15% |
| Yards per game | 15% |

Each component is converted to a z-score first. That keeps the different units from dominating the calculation.

The final score is centered around 50 and scaled so that higher values represent stronger overall profiles within this comparison group.

## Why target share matters

Raw targets tell you how often a player was thrown the ball. Target share puts that number into context by asking how much of the offense's passing volume the player actually owned.

That is useful for evaluation because 140 targets on a pass-heavy team are not exactly the same situation as 140 targets on a low-volume passing offense.

## Why I included efficiency

Volume is important, but I did not want the model to reward volume blindly.

A player can have a high target share while catching a lower percentage of those targets or producing less yardage per target. On the other hand, a player with fewer opportunities can show a very efficient profile.

That tension is where the model becomes more interesting than a simple leaderboard.

## What stands out

The strongest profiles tend to have a combination of volume and efficiency rather than being elite in only one category.

Ja'Marr Chase is a good example of the type of profile the model rewards: extremely high volume, strong catch rate, strong yards per target and elite touchdown output.

Jameson Williams is another interesting case. His target volume is much lower than the top target earners, but his yards per target are excellent. That creates a different player profile rather than simply a worse version of a high-volume receiver.

## Important limitation

This is a **descriptive evaluation model**, not a predictive scouting model.

It uses same-season outcomes to describe player profiles. It does not claim that the score predicts future NFL performance.

The next version I would build would use multiple seasons and out-of-sample validation to test whether these traits actually predict the following season.

## Charts

- `target_share_vs_fantasy.png`
- `top_wr_scores.png`
- `efficiency_map.png`
- `feature_relationships.png`

## Run it

```bash
pip install -r requirements.txt
python scouting_model.py
```
