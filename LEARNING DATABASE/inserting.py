import sqlite3 as sq3

# this line conncts to  db if exists or creates if it doesn't
con=sq3.connect('LEARNING DATABASE\data.db')  
# for the db we need to have a mediater whihc is cursor
cur=con.cursor() 

cur.execute(" INSERT INTO customers VALUES('Shreenandan', 'Sahu', 'shreenandansahu123@gmail.com')")
print("Data inserted successfully")

#commit the changes to the database
con.commit()
con.close
# close the connection
 