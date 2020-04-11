#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE students
         (name CHAR(50) NOT NULL,
         addr CHAR(50) NOT NULL,
         city CHAR(50),
         pin CHAR(50));''')
print("Table created successfully");

conn.execute('''INSERT INTO students (name,addr,city,pin) 
	VALUES ('alvin', 'alvin', 'alvin', '111');''');

print("STUDENT created successfully");


conn.close()