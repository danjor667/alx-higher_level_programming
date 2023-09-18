#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    query = f"SELECT * FROM states;"
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for results in result:
        print(results)
    cursor.close()
    db.close()
