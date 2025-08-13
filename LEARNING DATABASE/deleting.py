import sqlite3 as sq3

# this line conncts to  db if exists or creates if it doesn't
con=sq3.connect('LEARNING DATABASE\data.db')  
# for the db we need to have a mediater whihc is cursor
cur=con.cursor() 

cur.execute(" SELECT rowid,* FROM customers ")
for row in cur.fetchall():
    print(f"{row[0]}:-{row[1]} {row[2]}")  # prints first_name, last_name, email


cur.execute(" DELETE FROM customers WHERE first_name='Shreenandan'")


#commit the changes to the database
con.commit()
cur.execute(" SELECT rowid,* FROM customers")

for row in cur.fetchall():
    print(f"{row[0]}:-{row[1]} {row[2]}")  # prints first_name, last_name, email

con.close
# close the connection
  