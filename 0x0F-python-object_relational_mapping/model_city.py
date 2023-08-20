#!/usr/bin/python3

"""
model for class defination of a city
"""

from model_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    class inherits from Base and has id, name and states_id attriutes
    """
    __tablename__ = 'cities'
    id = Column(Integer, ptimary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)

    def__str__(self):
        return f"{self.name}"
