# College Basketball Offensive Profiles — 2023-24

## The question

College basketball has a weird relationship between pace, scoring and winning.

A team can average 85 points per game because it plays extremely fast. Another can score 78 because it is much more efficient per possession.

I wanted to separate those ideas and look at two different offensive measures:

- Points per game
- Offensive rating

Then I compared both with winning percentage.

## Data

The project uses publicly available 2023-24 Division I men's college basketball statistics.

The sample contains 25 teams selected to give the analysis a useful mix of high-scoring teams, strong teams and different offensive profiles.

Sources:

- Sports-Reference 2023-24 school statistics: https://www.sports-reference.com/cbb/seasons/men/2024-school-stats.html
- WarrenNolan 2024 points per game: https://www.warrennolan.com/basketball/2024/stats-off-points-per-game
- WarrenNolan 2024 offensive rating: https://www.warrennolan.com/basketball/2024/stats-adv-offensive-rating
- WarrenNolan 2024 win percentage: https://www.warrennolan.com/basketball/2024/stats-season-win-percent

## What I looked at

### Points per game

This is the easiest offensive metric to understand, but it is strongly affected by pace.

### Offensive rating

Offensive rating measures points scored per 100 possessions. It gives a better idea of how efficiently a team scores when pace is taken into account.

## What I found

The most interesting part is that the two metrics tell slightly different stories.

Alabama, Kentucky, Arizona and other high-scoring teams show how much offensive pace can matter. Connecticut, Purdue, Gonzaga and other strong teams show why efficiency can be more informative than raw scoring volume.

The project is not trying to prove that offense alone wins games. Basketball outcomes also depend on defense, turnovers, rebounding, opponent quality, shot profile and late-game performance.

Instead, this is a first step toward building a more complete team profile.

## Why this fits sports analytics

This is the kind of question I would want to ask before building a lineup or player evaluation model:

**What are we actually measuring?**

If a coach says a team is “high powered,” I would want to know whether that comes from pace, efficiency, shot selection, transition opportunities or something else.

## Charts

- `scoring_vs_win_pct.png`
- `offensive_rating_vs_wins.png`
- `top_scoring_teams.png`

## Run it

```r
install.packages("tidyverse")
source("basketball_analysis.R")
```
