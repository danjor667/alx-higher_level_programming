#!/usr/bin/python3
"""
doc
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id).all()
    for state in res:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")
