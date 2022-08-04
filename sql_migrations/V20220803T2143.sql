CREATE TABLE `dp_valorant`.`alembic_version` (
    `version_num` STRING(32) NOT NULL
);

-- Running upgrade  -> V20220803T2143

CREATE TABLE `dp_valorant`.`agents` (
    `agent_id` INT64 NOT NULL, 
    `name` STRING NOT NULL, 
    `origin` STRING NOT NULL, 
    `role` STRING NOT NULL, 
    `release` FLOAT64
);

CREATE TABLE `dp_valorant`.`maps` (
    `map_id` INT64 NOT NULL, 
    `name` STRING NOT NULL, 
    `location` STRING NOT NULL, 
    `release` FLOAT64
);

CREATE TABLE `dp_valorant`.`patches` (
    `patch` INT64 NOT NULL, 
    `release` DATE NOT NULL, 
    `size` STRING, 
    `highlights` STRING
);

CREATE TABLE `dp_valorant`.`matches` (
    `match_id` INT64 NOT NULL, 
    `timestamp` DATETIME NOT NULL, 
    `event` STRING, 
    `stakes` STRING, 
    `url` STRING, 
    `map_stats` BOOL NOT NULL, 
    `player_stats` BOOL NOT NULL
);

ALTER TABLE `dp_valorant`.`agents` SET OPTIONS(description='Table containing the currently available agents in valorant');
ALTER TABLE `dp_valorant`.`maps` SET OPTIONS(description='Table containing the currently available maps in valorant');
ALTER TABLE `dp_valorant`.`patches` SET OPTIONS(description='Table containing the patch updates for valorant');
ALTER TABLE `dp_valorant`.`matches` SET OPTIONS(description='Table containing matches scraped using the valorant_matches DAG in Airflow');
