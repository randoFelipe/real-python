import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    cities = [
    ('Sao Paulo','SP',16000000),
    ('Tapiratiba','SP',15000),
    ('Phoenix','AZ',1500000)
    ]
    c.executemany('INSERT INTO population Values(?,?,?)',cities)
