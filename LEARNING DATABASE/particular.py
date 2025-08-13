import sqlite3 as sq3

# this line conncts to  db if exists or creates if it doesn't
con=sq3.connect('LEARNING DATABASE\data.db')  
# for the db we need to have a mediater whihc is cursor
cur=con.cursor() 

cur.execute(" SELECT rowid,* FROM customers WHERE last_name=='Sahu'")
# print(cur.fetchall()) # gives all the data int the table
#print(cur.fetchone()) #moving pointer types as many ties called
#print(cur.fetchmany(4)) # gives that may rows from the top of table and updates pointer
for row in cur.fetchall():
    print(f"UniqueId:{row[0]} Name:{row[1]} Surname: {row[2]} and emial id: {row[3]}")  # prints first_name, last_name, email

#commit the changes to the database
con.commit()
con.close
# close the connection
  