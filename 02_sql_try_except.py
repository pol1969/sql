#создает SQLite базу и таблицы
import sqlite3

#create a new database if database doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:

	#create a table
	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY',8400000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA',800000)")

	conn.commit()
except sqlite3.OperationalError:
	print("Ooops! Something went wrong.Try again..."+ str(sqlite3.OperationalError))

#close the database connection
conn.close()


