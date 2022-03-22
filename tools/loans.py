from flask import redirect, render_template, request
import sqlite3


con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Loan:
    def __init__(self):
        pass

    def showAllLoans(self):
        pass

    def loanBook(self):
        if request.method=="POST":
            customerName=request.form.get("customerName")
            bookName=request.form.get("bookName")
            loanDate=request.form.get("loanDate")
            expectedReturn=request.form.get("expectedReturn")
            sql=(f'''INSERT INTO loans VALUES("{customerName}", "{bookName}", "{loanDate}", "{expectedReturn}")''')
            cur.execute(sql)
            con.commit()
            return render_template("/loans/loanBook.html")
        return render_template("/loans/loanBook.html")

    def returnBook(self):
        if request.method=="POST":
            customerName=request.form.get("customerName")
            bookName=request.form.get("bookName")
            returnSQL=(f'''DELETE FROM loans WHERE cusID="{int(customerName)}" and bookID="{int(bookName)}"''')
            cur.execute(returnSQL)
            con.commit()
            return render_template("/books/returnBook.html")
        return render_template("/books/returnBook.html")