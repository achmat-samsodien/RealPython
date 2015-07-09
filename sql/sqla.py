__author__ = 'achmat'

#Create a simple database

import sqlite3

#Create a new database if it does not exist
conn = sqlite3.connect("new.db")


#get a cursor object used to execute SQL commands
cursor = conn.cursor()

cursor.execute("""CREATE TABLE population (city TEXT,state TEXT,population INT)""")

conn.close()