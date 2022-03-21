from flask import render_template, request
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
            cur.execute(f'''INSERT INTO books VALUES(not null,"{bName}", "{bAuthor}", {int(bYear)}, {int(bType)})''')
            con.commit()
        return render_template("/books/addBook.html")

    def showAllBooks(self):
        if request.method=='POST':
            pass
        sqlBooks = "SELECT * FROM books"
        cur.execute(sqlBooks)
        books = cur.fetchall()
        return render_template("/books/showAllBooks.html", books=books)

    def findBook(self):
        if request.method=='POST':
            bookName = request.form.get('bookName')
            bookAuthor=request.form.get('bookAuthor')
            sql = (f'''select * from books where bookName like "%{bookName}%" and Author like "%{bookAuthor}%"''')
            cur.execute(sql)
            books = cur.fetchall()
            return render_template("/books/findBook.html", books=books)
        return render_template("/books/findBook.html")

    def removeBook(self):
        if request.method=='POST':
            bName=request.form.get('bName')
            bAuthor=request.form.get('bAuthor')
            bYear=request.form.get('bYear')
            sql=(f'''DELETE FROM books where bookName="{bName}" and Author="{bAuthor}" and yearPublished="{int(bYear)}"''')
            cur.execute(sql)
            con.commit()
            bRem="Book removed!"
            goToBookDatabase="Click here"
            goBack="to go back."   
            return render_template("/books/removeBook.html", bRem=bRem, goToBookDatabase=goToBookDatabase, goBack=goBack)
        return render_template("/books/removeBook.html")