#!/usr/bin/python3
"""
selsct all from cities and city states
"""

import sys
import MySQLdb

if __name__ == "__main__":
    query = "SELECT cities.id, cities.name, states.name\
             FROM cities INNER JOIN states\
             WHERE states.id = cities.state_id\
             ORDER BY cities.id"
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        print(res)
