from flask import render_template, request
import sqlite3

from tools.books import Book


con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Loan:
    def __init__(self):
        pass

    def showAllLoans(self):
        if request.method=="POST":
            pass
        findAllLoans = '''SELECT * FROM loans'''
        cur.execute(findAllLoans)
        allLoans = cur.fetchall()
        return render_template("/loans/showAllLoans.html", allLoans=allLoans)

    def loanBook(self):
        if request.method=="POST":
            customerName=request.form.get("customerName")
            bookName=request.form.get("bookName")
            loanDate=request.form.get("loanDate")
            returnDate=request.form.get("returnDate")
            sql=(f'''INSERT INTO loans (cusID, bookID) SELECT customers.customerID, books.bookID FROM customers, books WHERE customers.cusName="{customerName}" and books.bookName="{bookName}"''')
            updateDate=(f'''UPDATE loans SET loanDate="{loanDate}", returnDate="{returnDate}"''')
            cur.execute(sql)
            cur.execute(updateDate)
            updateSQL=(f'''UPDATE books SET inStock="No" WHERE bookName="{bookName}"''')
            cur.execute(updateSQL)
            con.commit()
            return render_template("/loans/loanBook.html")
        return render_template("/loans/loanBook.html")

    def returnBook(self):
        if request.method=="POST":
            customerName=request.form.get("customerName")
            bookName=request.form.get("bookName")
            removeSQL=(f'''DELETE FROM loans WHERE cusID="{int(customerName)}" and bookID="{int(bookName)}"''')
            cur.execute(removeSQL)
            con.commit()
            return render_template("/books/returnBook.html")
        return render_template("/books/returnBook.html")