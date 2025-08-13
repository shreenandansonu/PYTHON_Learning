import sqlite3 as sq3

con=sq3.connect('LEARNING DATABASE\data.db')

cur=con.cursor()

# cur.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")
cur.execute("SELECT rowid,* FROM customers ORDER BY last_name DESC")

itemas=cur.fetchall()
for item in itemas:
    print(item)

con.commit()
con.close()     