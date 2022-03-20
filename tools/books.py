from flask import Flask, render_template, request
import sqlite3

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Book:
    def __init__(self):
        pass

    def addBook(self):
        if request.method=='POST':
            bName = request.form.get('bookName')
            bAuthor = request.form.get('Author')
            bYear = request.form.get('yearPublished')
            bType = request.form.get('bookType')
            cur.execute(f'''INSERT INTO books VALUES("{bName}", "{bAuthor}", {int(bYear)}, {int(bType)})''')
            con.commit()

    def showAllBooks(self):
        global books
        if request.method=='POST':
            pass
        sqlBooks = "SELECT * FROM books"
        cur.execute(sqlBooks)
        books = cur.fetchall()
        return render_template('/books/showAllBooks.html', books=books)