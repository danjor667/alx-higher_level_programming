#!/usr/bin/python3
"""
printing the first state in the databases
hbtn_0e_6_usa
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    print(f"{states[0].id}: {states[0].name}")
