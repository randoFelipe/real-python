import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("SELECT * FROM population")
    try:
        rows = c.fetchall()
        for row in rows:
            print(row[0],row[1])
    except Exception as e:
        print(e)
