import sqlite3 as sq3

# this line conncts to  db if exists or creates if it doesn't
con=sq3.connect('LEARNING DATABASE\data.db')  
# for the db we need to have a mediater whihc is cursor
cur=con.cursor() 

cur.execute(" SELECT * FROM customers")
# print(cur.fetchall()) # gives all the data int the table
#print(cur.fetchone()) #moving pointer types as many ties called
#print(cur.fetchmany(4)) # gives that may rows from the top of table and updates pointer
for row in cur.fetchall():
    print(f"Name:{row[0]} Surname: {row[1]} and emial id: {row[2]}")  # prints first_name, last_name, email

#commit the changes to the database
con.commit()
con.close
# close the connection
 