import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    try:
        cars = [
        ('Ford','Ka',12),
        ('Honda','Civic',5)
        ]
        c.executemany("INSERT INTO inventory VALUES(?,?,?)",cars)
        rows = c.execute("SELECT * FROM inventory")
        for row in rows:
            print (row[0],row[1],row[2])
    except Exception as e:
        print(e)
