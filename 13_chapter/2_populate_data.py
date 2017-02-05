import sqlite3

users = (
        ('Jean-Babtist Zorg', 'Human', 122),
        ('korben dallas', 'Meat Popsicle', 100),
        ('Ak,not', 'Mangalore', -5)
)

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("Create TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", users)
