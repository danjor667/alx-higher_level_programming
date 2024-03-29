#!/usr/bin/python3
"""
doc
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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
    states = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states:
        session.delete(state)
        session.commit()
        session.close()
