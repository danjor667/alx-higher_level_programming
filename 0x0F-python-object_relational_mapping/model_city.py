#!/usr/bin/python3
"""
doc
"""

from sqlalchemy import Column, String, Integer ForeignKey
from sqlalchemy.ext.declarative import declative_base
from model_state import Base


class City(Base):
    """
    doc
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True, unique=True)
    state_id = Column(Integer, ForeigKey('states.id'), nullable=False)
