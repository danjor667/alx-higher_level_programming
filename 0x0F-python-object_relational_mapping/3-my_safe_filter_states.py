#!/usr/bin/python3
"""
select only STATE from states, SQL injection free
"""

import sys
import MySQLdb

if __name__ == "__main__":
    query = "SELECT * FROM states WHERE states.name = %s"
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(query, (sys.argv[4],))
    result = cursor.fetchall()
    for res in result:
        print(res)
