import sqlite3
from flask import render_template

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

def addData():
    cur.execute('''INSERT INTO books VALUES(not null, "Harry Potter and the Sorcerers Stone", "JK Rowling", 1998, 1, "Yes")''')
    cur.execute('''INSERT INTO books VALUES(not null, "Harry Potter and the Chamber of Secrets", "JK Rowling", 1998, 3, "Yes")''')
    cur.execute('''INSERT INTO books VALUES(not null, "Harry Potter and the Prisoner of Azkaban", "JK Rowling", 1999, 2, "Yes")''')
    cur.execute('''INSERT INTO books VALUES(not null, "Harry Potter and the Goblet of Fire", "JK Rowling", 2001, 1, "Yes")''')
    cur.execute('''INSERT INTO books VALUES (not null, "The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 1950, 2, "Yes")''')
    cur.execute('''INSERT INTO books VALUES (not null, "Prince Caspian", "C.S. Lewis", 1951, 1, "Yes")''')
    cur.execute('''INSERT INTO books VALUES (not null, "The Last Battle", "C.S. Lewis", 1956, 3, "Yes")''')
    cur.execute('''INSERT INTO customers VALUES(not null, "Chen Harel", "Rehovot", 30)''')
    cur.execute('''INSERT INTO customers VALUES(not null, "Jackie Chan", "Hong Kong", 21)''')
    cur.execute('''INSERT INTO customers VALUES(not null, "Arnold Shwartz", "Austria", 34)''')
    cur.execute('''INSERT INTO customers VALUES(not null, "Eddie Murphy", "United States", 32)''')
    cur.execute('''INSERT INTO customers VALUES(not null, "Tom Holland", "England", 20)''')
    con.commit()
    return render_template("/index.html")
