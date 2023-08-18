#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
import sys

if __name__ == '__main__':

    if len(sys.argv) != 5:
        sys.exit("Usage: python script.py <mysql_username>"
                 "<mysql_password> <database_name> <given_arg>")
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    given_arg = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    cursor = db.cursor()

    selected_list = ("SELECT *  FROM states"
                     "WHERE name LIKE '{}' "
                     "ORDER BY id ASC;".format(given_arg))

    cursor.execute(selected_list)

    output = cursor.fetchall()
    for row in output:
        print(row)

    cursor.close()
    db.close()
