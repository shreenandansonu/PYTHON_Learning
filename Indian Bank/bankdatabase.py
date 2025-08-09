import sqlite3 as sq3


def create_database():
    con = sq3.connect('./Indian Bank/bankdatabase.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS bankaccounts(
                
                name TEXT NOT NULL,
                fname TEXT NOT NULL,
                dob TEXT NOT NULL,
                balance REAL NOT NULL,
                password TEXT NOT NULL
                )''')
    con.commit()
    con.close()


def change_password(name: str, password: str, npassword: str):
    con = sq3.connect("./Indian Bank/bankdatabase.db")
    cur = con.cursor()
    cur.execute(
        '''SELECT rowid,* FROM bankaccounts WHERE name=? AND password=?''', (name,password))

    if cur.fetchone():
        cur.execute('''UPDATE bankaccounts SET password=? WHERE name=?''', (npassword, name))
        con.commit()
        con.close()
        return "Password changed successfully"  
    else:
        con.close()
        return "Invalid name or password" 
    


def create_account(name, fname, dob, balance):
    con = sq3.connect('./Indian Bank/bankdatabase.db')
    cur = con.cursor()

    password = name[:3] + dob[-4:] + fname[:3]

    cur.execute('''INSERT INTO bankaccounts VALUES (?,?,?,?,?)''',
                (name, fname, dob, balance, password))

    con.commit()
    con.close()
    return password


if __name__ == "__main__":
    create_database()
