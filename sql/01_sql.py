import sqlite3

#create database if not exists
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)
""")

#close the connection
conn.close
