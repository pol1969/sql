#создает SQLite базу и таблицы
import sqlite3

#create a new database if database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	for row in c.execute("SELECT firstname, lastname from employees"):
			print(row)



