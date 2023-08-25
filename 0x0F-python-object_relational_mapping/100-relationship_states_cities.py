#!/usr/bin/python3

"""
creates the state with city database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    """
    initialize argv
    """
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_host = "localhost"
    db_port = 3306

    db_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
