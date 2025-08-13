import sqlite3 as sq3

con=sq3.connect('LEARNING DATABASE\data.db')

cur=con.cursor()


cur.execute("SELECT rowid,* FROM customers WHERE last_name='Kumar' AND rowid>9")

cur.execute("SELECT rowid,* FROM customers WHERE last_name='Kumar' OR rowid>9")

itemas=cur.fetchall()
for item in itemas:
    print(item)

con.commit()
con.close()     