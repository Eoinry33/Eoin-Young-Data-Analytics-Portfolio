CREATE TABLE teams (
    team_code VARCHAR(3) PRIMARY KEY,
    division VARCHAR(20) NOT NULL,
    wins INTEGER NOT NULL,
    losses INTEGER NOT NULL,
    points_for INTEGER NOT NULL,
    points_against INTEGER NOT NULL
);

CREATE TABLE attendance (
    team_code VARCHAR(3) PRIMARY KEY REFERENCES teams(team_code),
    home_games INTEGER NOT NULL,
    home_attendance INTEGER NOT NULL,
    home_avg_attendance NUMERIC(10,2) NOT NULL
);
