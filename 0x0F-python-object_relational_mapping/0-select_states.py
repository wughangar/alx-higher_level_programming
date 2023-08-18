#!/usr/bin/python3

if __name__ = '__main__':
    import MySQLdb
    import sys
    """
    script that lists all the states from the database hbtn_0e_0_usa
    """

    if len(sys.argv != 4:
            sys.exit()

    # get the required parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )
    cursor = db.cursor()

    # send and execute the request
    selected_list = "SELECT *  FROM states ORDER BY id ASC;"

    cursor.execute(selected_list)

    # get the feedback and display it
    output = cursor.fetchall()
    for row in output:
        print(row)

    # close the connection and cursor
    cursor.close()
    db.close()
