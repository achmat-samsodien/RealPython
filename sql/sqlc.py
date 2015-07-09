__author__ = 'achmat'

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

#insert multiple records using a tuple

cities = [
          ('Boston', 'MA',9120000),
          ('Chicago','IL',3245666),
          ('Houston','TX',3200000),
          ('Denver','CL',2400000)
         ]

#insert into datatable

c.executemany('INSERT INTO population VALUES(?,?,?)',cities)