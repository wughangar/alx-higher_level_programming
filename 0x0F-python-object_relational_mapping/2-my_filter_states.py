#!/usr/bin/python3
"""
import sys for argv and mysqldb
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    script that lists all the states from the database hbtn_0e_0_usa
    """

    if len(sys.argv) != 5:
        sys.exit("Usage: python script.py <mysql_username>"
                 "<mysql_password> <database_name>")
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
                     "WHERE name LIKE %s ORDER BY id ASC;")

    cursor.execute(selected_list, (f"{given_arg}%",))

    output = cursor.fetchall()
    for row in output:
        print(row)

    cursor.close()
    db.close()
