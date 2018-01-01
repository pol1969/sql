#создает SQLite базу и таблицы
import sqlite3

#create a new database if database doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("INSERT INTO population VALUES('New York City', 'NY',8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA',800000)")

conn.commit()

#close the database connection
conn.close()


