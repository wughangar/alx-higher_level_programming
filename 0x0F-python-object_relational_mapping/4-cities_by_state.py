#!/usr/bin/python3

"""
Cities by states- script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

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
            ORDER BY cities.id ASC"

    cursor.execute(query)
    output = cursor.fetchall()

    for row in output:
        print(row)

    cursor.close()
    db.close()
