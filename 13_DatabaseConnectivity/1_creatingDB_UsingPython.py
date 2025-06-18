import sqlite3

connection = sqlite3.connect("school.db")

cur = connection.cursor()

cur.execute("create table Dept(deptNo integer primary key, name text)")

connection.commit()

cur.close()

connection.close()
