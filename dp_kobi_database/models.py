from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    DateTime
)

metadata = MetaData(schema="dp_valorant")
valorant_base = declarative_base(metadata=metadata)


class Maps(valorant_base):
    __tablename__ = "maps"
    __tableargs__ = {
        "comment": "Table containing the currently available maps in valorant"
    }

    map_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Agents(valorant_base):
    __tablename__ = "agents"
    __tableargs__ = {
        "comment": "Table containing the currently available agents in valorant"
    }

    agent_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    role = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Patches(valorant_base):
    __tablename__ = "patches"
    __tableargs__ = {
        "comment": "Table containing the patch updates for valorant"
    }


    patch = Column(Integer, primary_key=True)
    release = Column(Date, nullable=False)
    size = Column(String, nullable=True)
    highlights = Column(String, nullable=True)


class Matches(valorant_base):
    __tablename__ = "matches"
    __tableargs__ = {
        "comment": "Table containing matches scraped using the valorant_matches DAG in Airflow"
    }


    match_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    event = Column(String, nullable=True)
    stakes = Column(String, nullable=True)
    url = Column(String, nullable=True)
    map_stats = Column(Boolean, nullable=False)
    player_stats = Column(Boolean, nullable=False)


class TeamStats(valorant_base):
    __tablename__ = "team_stats"
    __tableargs__ = {
        "comment": "Table containing the stats for each team in each game they have played"
    }

    match_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, primary_key=True)
    result = Column(Boolean, nullable=False)
    score = Column(Integer, nullable=False)
    defense_score = Column(Integer, nullable=False)
    attack_score = Column(Integer, nullable=False)
    attack_start = Column(Boolean, nullable=False)
    map_name = Column(String, nullable=False)


class PlayerStats(valorant_base):
    __tablename__ = "player_stats"
    __tableargs__ = {
        "comment": "Table containing the stats for each player in each game they have played"
    }
 
    game_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, primary_key = True)
    acs = Column(Integer, nullable=False)
    adr = Column(Integer, nullable=False)
    kills = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    first_bloods = Column(Integer, nullable=False)
    first_deaths = Column(Integer, nullable=False)
    kast = Column(Float, nullable=False)
    hsp = Column(Float, nullable=False)
