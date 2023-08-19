#!/usr/bin/python3

"""
list all state objects
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./{sys.argv[0]} <{sys.argv[1]> <{sys.argv[2]}> ,{sys.argv[3].")
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                               sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}").format(state.id, state.name)
    session.close()
