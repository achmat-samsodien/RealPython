__author__ = 'achmat'

import sqlite3

conn = sqlite3.connect('new.db')

cursor=conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City','NY','8200000')")

cursor.execute("INSERT INTO population VALUES('San Francisco','SF',9200000)")

conn.commit()

conn.close()

