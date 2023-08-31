#!/usr/bin/python3

"""
13. Delete states
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    script that deletes all State objects
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

    deleted_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in deleted_state:
        session.delete(state)
    session.commit()
    session.close()
