# NFL Analytics Database — SQL

## Why I built this

I wanted one project that focuses less on charts and more on how an analyst would actually organize the data before the charts exist.

The database stores 2024 NFL team performance and attendance in two related tables.

That makes it possible to answer repeatable questions with SQL instead of manually filtering spreadsheets.

## Tables

### `teams`

One row per NFL team.

Fields:

- team_code
- division
- wins
- losses
- points_for
- points_against

### `attendance`

One row per NFL team.

Fields:

- team_code
- home_games
- home_attendance
- home_avg_attendance

The tables are linked through `team_code`.

## SQL concepts shown

- Primary and foreign keys
- INNER JOIN
- Common table expressions
- CASE statements
- Window functions
- RANK
- PERCENT_RANK
- Correlated subqueries
- Derived metrics
- Conference-level comparisons

## Example question

Instead of asking:

> Who had the most wins?

I can ask:

> Which teams had strong attendance even though they were not among the league's strongest teams?

That second question is much closer to the kind of analysis a sports-business department might actually use.

## Run it

The SQL is written for PostgreSQL.

```sql
CREATE DATABASE nfl_portfolio;
```

Then run:

```text
schema.sql
sample_data.sql
queries.sql
```

## Data sources

- NFL 2024 standings: https://www.nfl.com/standings/league/2024/REG
- ESPN 2024 attendance: https://www.espn.com/nfl/attendance/_/year/2024
- Pro-Football-Reference 2024 team stats: https://www.pro-football-reference.com/years/2024/

The data is public third-party information. The database structure and queries are my own.
