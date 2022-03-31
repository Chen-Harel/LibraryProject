from flask import Flask, render_template, request
import sqlite3
import tools.books as myBooks
import tools.customers as myCustomers
import tools.loans as myLoans
from tools.addData import addData as myData
from tools.addData import deleteData as myDelete

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

def initDB():
    try:
        cur.execute("CREATE TABLE books (bookID INTEGER PRIMARY KEY AUTOINCREMENT, bookName text, Author text, yearPublished int, bookType int, inStock text)")
        cur.execute("CREATE TABLE customers (customerID INTEGER PRIMARY KEY AUTOINCREMENT, cusName text, cusCity text, cusAge int)")
        cur.execute("CREATE TABLE loans (cusID int, bookID int, loanDate int, returnDate int)")
    except:
        print("All tables loaded")
    con.commit()
initDB()

app=Flask(__name__)

#Main page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addData")
def addData():
    return myData()

@app.route("/deleteData")
def deleteData():
    return myDelete()

#Add book page
@app.route("/books/addBook", methods=['GET', 'POST'])
def addBook():
    return myBooks.Book.addBook(myBooks)
    
#Show returned books page
@app.route("/books/returnBook", methods=['GET', 'POST'])
def returnBook():
    return myLoans.Loan.returnBook(myLoans)

#Show all books page
@app.route("/books/showAllBooks", methods=['GET', 'POST'])
def showAllBooks():
    return myBooks.Book.showAllBooks(myBooks)

#Find specific book page
@app.route("/books/findBook", methods=['GET','POST'])
def findBook():
    return myBooks.Book.findBook(myBooks)

#Remove book from database
@app.route("/books/removeBook", methods=['GET', 'POST'])
def removeBook():
    return myBooks.Book.removeBook(myBooks)

#Add a customer page
@app.route("/customers/addCustomer", methods=['GET', 'POST'])
def addCustomer():
    return myCustomers.Customer.addCustomer(myCustomers)

#Remove a customer page
@app.route("/customers/removeCustomer", methods=['GET', 'POST'])
def removeCustomer():
    return myCustomers.Customer.removeCustomer(myCustomers)

#Show all customers page
@app.route("/customers/showAllCustomers", methods=['GET', 'POST'])
def showAllCustomers():
    return myCustomers.Customer.showAllCustomers(myCustomers)

#Find specific customer page
@app.route("/customers/findCustomer", methods=['GET', 'POST'])
def findCustomer():
    return myCustomers.Customer.findCustomer(myCustomers)

#Loan book page
@app.route("/loans/loanBook", methods=['GET', 'POST'])
def loanBook():
    return myLoans.Loan.loanBook(myLoans)

#Show all loaned books
@app.route("/loans/showAllLoans", methods=['GET', 'POST'])
def showAllLoans():
    return myLoans.Loan.showAllLoans(myLoans)

#Show all LATE loans
@app.route("/loans/showAllLateLoans")
def showAllLateLoans():
    return myLoans.Loan.showLateLoans(myLoans)

if __name__=="__main__":
    app.run(debug="True")