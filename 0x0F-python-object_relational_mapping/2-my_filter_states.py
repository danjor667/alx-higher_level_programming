#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    query = f"SELECT * FROM states WHERE states.name = '{sys.argv[4]}'"
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        print(res)
