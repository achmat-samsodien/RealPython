__author__ = 'achmat'

#Create a simple database

import sqlite3

#Create a new database if it does not exist
conn = sqlite3.connect("cars.db")


#get a cursor object used to execute SQL commands
cursor = conn.cursor()

cursor.execute('''CREATE TABLE cars (make TEXT,model TEXT,quantity INT)''')


conn.commit()
conn.close()