#!/usr/bin/python3
"""
This module establishes a connection to a database and
querries from it
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def query_from(username, password, name):
    """
    This function querries from a database
    """
    States = State

    # Establish a connection
    sql_url = f"mysql://{username}:{password}@localhost:3306/hbtn_0e_6_usa"

    engine = create_engine(sql_url)

    # Create a session to query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    states = session.query(States).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    query_from(username, password, name)
