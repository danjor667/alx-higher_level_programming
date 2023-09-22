#!/usr/bin/python3
"""
doc
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True)
    name = "{}".format(sys.argv[4])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == name).all()
    if len(states) != 0:
        for state in states:
            if state.name == name:
                print(f"{state.id}")
    else:
        print("Not found")
