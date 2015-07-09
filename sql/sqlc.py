__author__ = 'achmat'

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

#insert multiple records using a tuple

cities = [('Boston', 'MA','9120000')
          ('Chicago','IL','3245666')
          ()]

