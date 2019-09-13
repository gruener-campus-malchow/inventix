import sqlite3

db = sqlite3.connect("inventix.db")

c = db.cursor()

with open("setup.sql") as file:
    c.executescript(file.read())

db.commit()
db.close()