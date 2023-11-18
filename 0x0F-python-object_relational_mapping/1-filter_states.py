#!/usr/bin/python3
"""
This module uses the Module MySQLdb to interact with a database
"""
import sys
import MySQLdb


def list_states(username, password, database):
    """
    This function lists the states from a database,
    that start with 'N'
    Args:
        mysql username: user trying to connect
        mysql password: password for the user conncecting
        database name: name of the database
    """
    # connection details
    host = 'localhost'
    port = 3306

    # establish a concetion
    connection = MySQLdb.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object to execute SQL querries
    cursor = connection.cursor()

    # Query to be executed
    query = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id'

    # Execute the querry
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    list_states(username, password, database)
