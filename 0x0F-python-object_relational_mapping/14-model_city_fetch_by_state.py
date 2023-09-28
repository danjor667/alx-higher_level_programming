#!/usr/bin/python3
"""
doc
"""

from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True)
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(city.state_id == State.id).one()
        print(f"{state.name}: ({city.id}) {city.name}")
