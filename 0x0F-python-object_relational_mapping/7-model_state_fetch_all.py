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
    ul = f"mysql+mysqldb://{username}:{password}@localhost:3306/hbtn_0e_6_usa"

    engine = create_engine(ul, pool_pre_ping=True)

    # Create a session to query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
