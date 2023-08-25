#!/usr/bin/python3
"""
script that lists all state objects, and corresponding city objects
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    """
    initilaize argv
    """
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"
    db_port = 3306

    db_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(City).order_by(State.id, City.id).all()

    for state in query:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
