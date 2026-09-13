DROP TABLE IF EXISTS player_stats, games, players, teams CASCADE;

CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_code VARCHAR(4) UNIQUE NOT NULL,
    team_name VARCHAR(80) NOT NULL,
    conference VARCHAR(4),
    division VARCHAR(8)
);

CREATE TABLE players (
    player_id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    position VARCHAR(3) NOT NULL,
    team_id INT REFERENCES teams(team_id)
);

CREATE TABLE games (
    game_id SERIAL PRIMARY KEY,
    season INT NOT NULL,
    week INT NOT NULL,
    home_team_id INT REFERENCES teams(team_id),
    away_team_id INT REFERENCES teams(team_id),
    home_score INT NOT NULL,
    away_score INT NOT NULL
);

CREATE TABLE player_stats (
    game_id INT REFERENCES games(game_id),
    player_id INT REFERENCES players(player_id),
    passing_yards INT DEFAULT 0,
    rushing_yards INT DEFAULT 0,
    receiving_yards INT DEFAULT 0,
    touchdowns INT DEFAULT 0,
    fantasy_points NUMERIC(8,2) DEFAULT 0,
    PRIMARY KEY(game_id, player_id)
);
