#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    sql_cmd = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s\
    ORDER BY cities.id"
    num_rows = cursor.execute(sql_cmd, (argv[4],))
    rows = cursor.fetchall()
    result = []
    i = 0
    for row in rows:
        result.append(row[0])
        i += 1
    joined = ", ".join(result)
    print(joined)
    cursor.close()
    db.close()
