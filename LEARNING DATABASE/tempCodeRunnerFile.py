import sqlite3 as sq3

con=sq3.connect('data.db')

cur=con.cursor()

list_of_customers = [
    ('Shreenandan', 'Sahu', 'shrenandansahu123@gmail.com'),
    ('suraksha','jain','surakshajain06@gmail.com'),
    ('pradeepta','Kumar','pksahu123@gmial.com')
]
cur.executemany("INSERT INTO customers VALUES (?,?,?)", list_of_customers)
print("Data inserted successfully")

con.commit()
con.close()     