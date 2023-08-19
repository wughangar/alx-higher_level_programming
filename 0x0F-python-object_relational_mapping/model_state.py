#!/usr/bin/python3

"""
First state model- the class definition of a State and an instance Base
"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


db_user = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = "localhost"
db_port = 3306

db_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
