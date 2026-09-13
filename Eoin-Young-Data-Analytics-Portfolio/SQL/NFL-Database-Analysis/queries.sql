-- Team point differential
WITH results AS (
    SELECT home_team_id AS team_id, home_score AS points_for,
           away_score AS points_against FROM games
    UNION ALL
    SELECT away_team_id, away_score, home_score FROM games
)
SELECT t.team_name,
       SUM(points_for) AS points_for,
       SUM(points_against) AS points_against,
       SUM(points_for-points_against) AS point_differential
FROM results r
JOIN teams t ON t.team_id=r.team_id
GROUP BY t.team_name
ORDER BY point_differential DESC;

-- Position-adjusted player ranking
SELECT p.player_name, p.position,
       SUM(ps.fantasy_points) AS fantasy_points,
       RANK() OVER (
           PARTITION BY p.position
           ORDER BY SUM(ps.fantasy_points) DESC
       ) AS position_rank
FROM players p
JOIN player_stats ps ON ps.player_id=p.player_id
GROUP BY p.player_name,p.position
ORDER BY p.position,position_rank;

-- High-volume players
WITH totals AS (
    SELECT p.player_name,p.position,
           SUM(ps.rushing_yards+ps.receiving_yards) AS scrimmage_yards
    FROM players p
    JOIN player_stats ps ON ps.player_id=p.player_id
    GROUP BY p.player_name,p.position
)
SELECT * FROM totals
WHERE scrimmage_yards >= 1000
ORDER BY scrimmage_yards DESC;
