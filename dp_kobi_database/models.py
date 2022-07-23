from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    String,
)

valorant_base = declarative_base()


class Maps(valorant_base):
    map_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Agents(valorant_base):
    agent_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin = Column(String, nullable=False)
    role = Column(String, nullable=False)
    # if patch is null then was released in Beta
    release = Column(Float, nullable=True)


class Patches(valorant_base):
    patch = Column(Integer, primary_key=True)
    release = Column(Date, nullable=False)
    size = Column(String, nullable=True)
    highlights = Column(String, nullable=True)
