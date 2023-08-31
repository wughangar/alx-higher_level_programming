#!/usr/bin/python3

"""
10. Get a state
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    script that prints the State object with the name passed as argument
    """
    if len(sys.argv) != 5:
        print("Usage: ./{0} <{1}> <{2}> <{3}>".format(
            sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
        sys.exit(1)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    searched_state = sys.argv[4]
    result = session.query(State).filter(State.name == searched_state).first()
    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
