import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    try:
        row = c.fetchall()
        for row in c.execute("SELECT * FROM population"):
            print(row)
    except Exception as e:
        print(e)
