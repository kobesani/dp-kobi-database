-- Running upgrade V20220803T2143 -> V20220809T2156

CREATE TABLE `dp_valorant`.`player_stats` (
    `game_id` INT64 NOT NULL, 
    `team_id` INT64 NOT NULL, 
    `player_id` INT64 NOT NULL, 
    `acs` INT64 NOT NULL, 
    `adr` INT64 NOT NULL, 
    `kills` INT64 NOT NULL, 
    `deaths` INT64 NOT NULL, 
    `assists` INT64 NOT NULL, 
    `first_bloods` INT64 NOT NULL, 
    `first_deaths` INT64 NOT NULL, 
    `kast` FLOAT64 NOT NULL, 
    `hsp` FLOAT64 NOT NULL
);

CREATE TABLE `dp_valorant`.`team_stats` (
    `match_id` INT64 NOT NULL, 
    `game_id` INT64 NOT NULL, 
    `team_id` INT64 NOT NULL, 
    `result` BOOL NOT NULL, 
    `score` INT64 NOT NULL, 
    `defense_score` INT64 NOT NULL, 
    `attack_score` INT64 NOT NULL, 
    `attack_start` BOOL NOT NULL, 
    `map_name` STRING NOT NULL
);

ALTER TABLE `dp_valorant`.`team_stats`
    SET OPTIONS(description='Table containing the stats for each team in each game they have played');

ALTER TABLE `dp_valorant`.`maps`
    SET OPTIONS(description='Table containing the stats for each player in each game they have played');

-- UPDATE `alembic_version` SET `version_num`='V20220809T2156' WHERE `alembic_version`.`version_num` = 'V20220803T2143';
