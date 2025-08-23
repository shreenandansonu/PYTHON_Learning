from flask import Flask
import sqlite3 as sq3

def databse(i:int):
    con=sq3.connect("Indian Bank\bankdatabase.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM bankaccounts WHERE rowid=?",(i))
    res=cur.fetchall()
    return res

app=Flask(__name__)

@app.route("/<int:i>")
def namste():
    databse(i)
    return "<p>namaste</p>"

if __name__=="__main__":
    app.run(debug=True)