# NFL Team Performance & Attendance — 2024

## Why I built this

I wanted to start with a simple front-office question: **does the scoreboard tell the same story as the standings, and does team performance line up with how many people show up?**

A 12-5 team and a 12-5 team are not necessarily built the same way. Point differential gives a little more context than wins alone, while attendance adds a completely different angle: fan engagement and market demand.

This project combines those ideas instead of treating the standings as the whole story.

## Questions

1. How strongly does scoring margin relate to wins?
2. Which teams were the biggest outliers?
3. Does home attendance move with winning percentage?
4. Which teams drew strong crowds despite mediocre records?
5. Where would a sports-business or front-office analyst want to dig deeper?

## Data

The team performance file contains all 32 NFL teams from the 2024 regular season.

- Wins, losses, points for and points against: NFL.com / Pro-Football-Reference
- Home attendance: ESPN's 2024 NFL attendance table
- Home average is calculated as home attendance divided by home games.

The project uses the 2024 regular season only so the comparisons are consistent.

## Approach

I calculated:

- Winning percentage
- Point differential
- Point differential per game
- Home average attendance
- Correlations between wins, scoring margin and attendance

The scatterplot is intentionally simple. The goal is to make the relationship obvious before adding more complicated modeling.

## What I found

The strongest teams generally separated themselves through scoring margin. Detroit, Kansas City, Baltimore and Philadelphia were among the teams near the top of the standings, while teams with large negative margins clustered near the bottom.

Attendance is more complicated. A strong record helps, but it is clearly not the only driver. Market size, stadium capacity, travel, opponent mix and stadium-specific reporting all matter. That is why I would treat attendance as an engagement metric rather than a direct measure of team quality.

One useful example is Chicago: the Bears finished 5-12 with a -60 point differential, but still recorded more than 527,000 home attendees across nine home games. That is the kind of gap between on-field results and fan demand that could be interesting for a sports business team.

## Charts

- `wins_vs_point_differential.png` — relationship between wins and scoring margin
- `top_10_scoring_margins.png` — teams with the strongest scoring margins
- `correlation_matrix.png` — simple correlation view

## Reproduce it

```bash
pip install -r requirements.txt
python nfl_team_analysis.py
```

## Data notes

This is real 2024 NFL data, not synthetic data. Third-party data remains subject to the original source's terms. I calculated the derived metrics myself.

Sources:
- NFL standings: https://www.nfl.com/standings/league/2024/REG
- PFR team stats: https://www.pro-football-reference.com/years/2024/
- ESPN attendance: https://www.espn.com/nfl/attendance/_/year/2024
- nflverse: https://github.com/nflverse/nflverse-data
