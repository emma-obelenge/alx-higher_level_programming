#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
