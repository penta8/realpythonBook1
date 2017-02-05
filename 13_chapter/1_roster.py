import sqlite3

connection = sqlite3.connect(':memory:')
c = connection.cursor()
c.execute("CREATE Table Roster(Name TEXT, Species TEXT, IQ INT)")
connection.close()
