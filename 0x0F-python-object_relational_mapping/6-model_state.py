#!/usr/bin/python3

"""
model base
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
            'mysql + mysqldb://{sys.argv[1]:{sys.argv[2]} /'
            '@localhost/{sys.argv[3]}',
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
