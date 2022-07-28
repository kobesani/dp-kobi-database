from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    Integer,
    MetaData,
    String,
    DateTime
)

metadata = MetaData(schema="dp_kobi")
valorant_base = declarative_base(metadata=metadata)


class Maps(valorant_base):
    __tablename__ = "maps"

    map_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Agents(valorant_base):
    __tablename__ = "agents"

    agent_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    role = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Patches(valorant_base):
    __tablename__ = "patches"

    patch = Column(Integer, primary_key=True)
    release = Column(Date, nullable=False)
    size = Column(String, nullable=True)
    highlights = Column(String, nullable=True)


class Matches(valorant_base):
    __tablename__ = "valorant_matches"

    match_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    event = Column(String, nullable=True)
    stakes = Column(String, nullable=True)
    url = Column(String, nullable=True)
    map_stats = Column(Boolean, nullable=False)
    player_stats = Column(Boolean, nullable=False)


