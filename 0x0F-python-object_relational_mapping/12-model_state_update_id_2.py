#!/usr/bin/python3
"""
This module establishes a connection to a database and
querries from it
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    This function querries from a database
    """
    username, password, name = sys.argv[1:]
    # Establish a connection
    ul = f"mysql+mysqldb://{username}:{password}@localhost:3306/{name}"

    engine = create_engine(ul, pool_pre_ping=True)

    # Create a session to query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new object
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update.name = 'New Mexico'
    state_to_update.id = 2
    session.commit()
