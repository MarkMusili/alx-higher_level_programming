#!/usr/bin/python3
"""
This module establishes a connection to a database and
querries from it
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """
    This function querries from a database
    """
    username, password, name = sys.argv[1:4]
    # Establish a connection
    ul = f"mysql+mysqldb://{username}:{password}@localhost:3306/{name}"

    engine = create_engine(ul, pool_pre_ping=True)

    # Create a session to query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    for x in session.query(City, State)\
            .filter(City.state_id == State.id).order_by(City.id):
        print(f"{x.State.name}: ({x.City.id}) {x.City.name}")
