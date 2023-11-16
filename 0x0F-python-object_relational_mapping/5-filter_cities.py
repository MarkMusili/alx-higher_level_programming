#!/usr/bin/python3
import sys
import MySQLdb
"""
This module uses the Module MySQLdb to interact with a database
"""


def list_cities_by_state(username, password, database, state_name):
    """
    This function lists the states from a database,
    that start with 'N'
    Args:
        mysql username: user trying to connect
        mysql password: password for the user conncecting
        database name: name of the database
        state_name: name to be searched
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
        SELECT cities.name FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
        """

    # Execute the querry
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == '__main__':
    username, password, database, state_name = sys.argv[1:5]

    list_cities_by_state(username, password, database, state_name)
