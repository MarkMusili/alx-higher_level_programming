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
    username, password, db_name, name = sys.argv[1:]
    # Establish a connection
    ul = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"

    engine = create_engine(ul, pool_pre_ping=True)

    # Create a session to query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    s_instance = session.query(State).filter(State.name == name).first()
    if s_instance is None:
        print("Not found")
    else:
        print(f"{s_instance.id}")
