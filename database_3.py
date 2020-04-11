#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('''INSERT INTO students (name,addr,city,pin) 
	VALUES ('pajaro', 'pajaro', 'pajaro', 'pajaro');''');

conn.commit()

print("STUDENT created successfully");


conn.close()