#создает SQLite базу и таблицы
import sqlite3

#create a new database if database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	cities =[
			('Boston','MA',600000),	
			('Chicago','IL',2700000),
			('Houston','TX',2100000),
			('Phoenix','AZ',1500000)
	        ]

	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)


