#!/usr/bin/python3

"""
9. Contains `a`
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    script that lists all State objects that contain the letter a
    """
    if len(sys.argv) != 4:
        print("Usage: ./{0} <{1}> <{2}> <{3}>".format(
            sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3]))
        sys.exit(1)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).filter(State.name.like /
                                           ('%a%')).order_by(State.id).all()
    for state in a_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
