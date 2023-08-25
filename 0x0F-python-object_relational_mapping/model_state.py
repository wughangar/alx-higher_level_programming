#!/usr/bin/python3

"""
First state model- the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    state class that inherits from Base
    class has id and name attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")

    def __str__(self):
        return f"{self.name}"
