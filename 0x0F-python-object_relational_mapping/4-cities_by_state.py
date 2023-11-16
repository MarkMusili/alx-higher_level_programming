#!/usr/bin/python3
import sys
import MySQLdb
"""
This module uses the Module MySQLdb to interact with a database
"""


def list_city_by_state(username, password, database):
    """
    This function lists the states from a database
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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id;
    """

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

    list_city_by_state(username, password, database)
