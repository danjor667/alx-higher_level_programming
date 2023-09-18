#!/usr/bin/python3
"""
all cities in STATE
"""

import sys
import MySQLdb

if __name__ == "__main__":

    query = "SELECT cities.name\
             FROM cities INNER JOIN states\
             ON cities.state_id = states.id\
             WHERE states.name = %s"
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))
    result = cursor.fetchall()
    for res in result:
        if res != result[-1]:
            print(res[0], end=', ')
        else:
            print(res[0])
