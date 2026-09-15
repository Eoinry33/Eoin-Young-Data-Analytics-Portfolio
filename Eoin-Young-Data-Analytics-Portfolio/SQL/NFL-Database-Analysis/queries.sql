-- 1. Build a single team performance view
SELECT
    t.team_code,
    t.division,
    t.wins,
    t.losses,
    ROUND(t.wins::numeric / (t.wins + t.losses), 3) AS win_pct,
    t.points_for - t.points_against AS point_diff,
    ROUND((t.points_for - t.points_against) / 17.0, 2) AS point_diff_per_game,
    a.home_avg_attendance
FROM teams t
JOIN attendance a USING (team_code)
ORDER BY wins DESC, point_diff DESC;

-- 2. Rank teams within each conference by point differential
WITH ranked AS (
    SELECT
        team_code,
        division,
        points_for - points_against AS point_diff,
        RANK() OVER (
            PARTITION BY CASE
                WHEN division LIKE 'AFC%' THEN 'AFC'
                ELSE 'NFC'
            END
            ORDER BY points_for - points_against DESC
        ) AS conference_rank
    FROM teams
)
SELECT *
FROM ranked
ORDER BY conference_rank, team_code;

-- 3. Teams that outdrew a better-performing team in the same conference
SELECT
    a.team_code,
    t.wins,
    ROUND(a.home_avg_attendance, 0) AS home_avg_attendance
FROM teams t
JOIN attendance a USING(team_code)
WHERE a.home_avg_attendance >
      (SELECT AVG(a2.home_avg_attendance)
       FROM attendance a2
       JOIN teams t2 USING(team_code)
       WHERE CASE WHEN t2.division LIKE 'AFC%' THEN 'AFC' ELSE 'NFC' END =
             CASE WHEN t.division LIKE 'AFC%' THEN 'AFC' ELSE 'NFC' END)
ORDER BY home_avg_attendance DESC;

-- 4. Simple performance tiers
SELECT
    team_code,
    wins,
    points_for - points_against AS point_diff,
    CASE
        WHEN wins >= 13 THEN 'Elite'
        WHEN wins >= 10 THEN 'Contender'
        WHEN wins >= 7 THEN 'Middle'
        ELSE 'Rebuild'
    END AS performance_tier
FROM teams
ORDER BY wins DESC;

-- 5. Attendance vs. wins
SELECT
    t.team_code,
    t.wins,
    a.home_avg_attendance,
    ROUND(
        100.0 * PERCENT_RANK() OVER (ORDER BY a.home_avg_attendance),
        1
    ) AS attendance_percentile
FROM teams t
JOIN attendance a USING(team_code)
ORDER BY attendance_percentile DESC;
