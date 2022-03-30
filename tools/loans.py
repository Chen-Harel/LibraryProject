from asyncio.windows_events import NULL
from flask import render_template, request
import sqlite3
import datetime
from consts import bookType

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
            #Does customer exist?
            cur.execute(f'''SELECT customerID FROM customers WHERE cusName="{customerName}"''')
            try:
                customerID=cur.fetchone()[0]
            except:
                #If not, display a message
                customerMessage="Customer not in database!"
                return render_template("/loans/loanBook.html", customerMessage=customerMessage)
            #Check if book exists
            cur.execute(f'''SELECT bookID FROM books WHERE bookName="{bookName}"''')
            try:
                foundBookID=cur.fetchone()[0]
            except:
                #If book isn't found
                bookMessage="Book not in database!"
                return render_template("/loans/loanBook.html", bookMessage=bookMessage)
            cur.execute('''SELECT bookID FROM loans WHERE bookID=? and returnDate=?''', (foundBookID, NULL))
            allLoans=cur.fetchall()
            print(len(allLoans))
            if len(allLoans)==0:
                longToday = datetime.datetime.now()
                #delete the pound sign in line 48 to get todays exact date.
                #shortToday=longToday.strftime("%d-%m-%Y")
                #test date below 
                shortToday = "10-03-2022"
                cur.execute('''INSERT INTO loans VALUES (?,?,?,?)''',(customerID, foundBookID, shortToday, NULL))
                cur.execute(f'''UPDATE books SET inStock="No" WHERE bookID="{foundBookID}"''')
                con.commit()
            else:
                bookIsLoaned="The book you want is currently unavailable. You may loan a different book if you want."
                return render_template("/loans/loanBook.html", bookIsLoaned=bookIsLoaned)
        return render_template("/loans/loanBook.html")

    def returnBook(self):
        if request.method=="POST":
            customerName=request.form.get("customerName")
            bookName=request.form.get("bookName")
            cur.execute(f'''SELECT bookID FROM books WHERE bookName="{bookName}"''')
            foundBookID=cur.fetchone()[0]
            cur.execute(f'''SELECT customerID FROM customers WHERE cusName="{customerName}"''')
            foundCustomerID=cur.fetchone()[0]
            longToday=datetime.datetime.now()
            shortToday=longToday.strftime("%d-%m-%Y")
            cur.execute(f'''UPDATE loans SET returnDate="{shortToday}" WHERE cusID="{foundCustomerID}" and bookID="{foundBookID}"''')
            cur.execute(f'''UPDATE books SET inStock="Yes" WHERE bookName="{bookName}"''')
            con.commit()
            returnMsg="Book returned successfully!"
            return render_template("/books/returnBook.html", returnMsg=returnMsg)
        return render_template("/books/returnBook.html")

    def showLateLoans(self):
        SQL='''SELECT books.bookType, books.bookName, customers.cusName, loanDate, returnDate
        FROM loans
        INNER JOIN books ON books.bookID=loans.bookID
        INNER JOIN customers ON customers.customerID=loans.cusID
        WHERE returnDate=0'''
        cur.execute(SQL)
        lateLoans=cur.fetchall()
        print(lateLoans)
        lateList=[]       
        for latebook in lateLoans:
            today = datetime.datetime.now()
            print(f"{today} -TODAY")
            whenLoaned = datetime.datetime.strptime(f'{latebook[3]}', '%d-%m-%Y')
            print(f"{whenLoaned} -WHEN BOOK WAS LOANED")
            print(f"{latebook[3]} - LATE BOOK 3")
            timeDiff = today - whenLoaned
            print(f"{timeDiff} -amount of time book is loaned")
            print(f"{latebook[0]} - booktype" )
            #if book type is 1, loan is for 10 days max
            if latebook[0] == 1:
                if timeDiff.days > 10:
                    lateList.append(latebook)
                    print("You are late on your 10 day loan")
            #if book type is 2, loan is for 5 days max
            elif latebook[0] == 2:
                if timeDiff.days > 5:
                    lateList.append(latebook)
                    print("You are late on your 5 day loan")
            #if book type is 3, loan is for 2 days max
            elif latebook[0] == 3:
                if timeDiff.days > 2:
                    lateList.append(latebook)
                    print("You are late on your 2 day loan")
        return render_template("/loans/showAllLateLoans.html", lateList=lateList)