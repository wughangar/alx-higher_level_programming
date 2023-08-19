#!/usr/bin/python3

"""
 All cities by state- script that takes in the name of a state as an argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    statename = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            LEFT JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"

    cursor.execute(query, (statename,))
    output = cursor.fetchall()

    for row in output:
        print(row)

    cursor.close()
    db.close()
