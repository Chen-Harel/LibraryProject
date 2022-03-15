from flask import Flask, render_template
import sqlite3

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

def initDB():
    try:
        cur.execute("CREATE TABLE books (bookName text, Author text, yearPublished int, bookType int")
    except:
        print("Table exists.")
    con.commit()
initDB()

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addCustomer")
def addCustomer():
    return render_template("addCustomer.html")

@app.route("/addBook")
def addBook():
    return render_template("addBook.html")

@app.route("/loanBook")
def loanBook():
    return render_template("loanBook.html")

@app.route("/returnBook")
def returnBook():
    return render_template("returnBook.html")

@app.route("/showAllBooks")
def showAllBooks():
    return render_template("showAllBooks.html")

@app.route("/showAllCustomers")
def showAllCustomers():
    return render_template("showAllCustomers.html")

@app.route("/showAllLoans")
def showAllLoans():
    return render_template("showAllLoans.html")

@app.route("/showAllLateLoans")
def showAllLateLoans():
    return render_template("showAllLateLoans.html")

@app.route("/findBook")
def findBook():
    return render_template("findBook.html")

@app.route("/findCustomer")
def findCustomer():
    return render_template("findCustomer.html")

@app.route("/removeBook")
def removeBook():
    return render_template("removeBook.html")

@app.route("/removeCustomer")
def removeCustomer():
    return render_template("removeCustomer.html")


if __name__=="__main__":
    app.run(debug=True)