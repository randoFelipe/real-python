import sqlite3

#create database if not exists
conn = sqlite3.connect("new.db")

cursor = conn.cursor()

#create table
cursor.execute("INSERT INTO population VALUES('New York City','NY',8460000)")

# commit the changes
conn.commit()

#close the connection
conn.close
