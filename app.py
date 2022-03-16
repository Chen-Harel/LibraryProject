from flask import Flask, render_template, request
import sqlite3

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

def initDB():
    try:
        cur.execute("CREATE TABLE books (bookName text, Author text, yearPublished int, bookType int)")
    except:
        print("Table exists.")

    con.commit()
initDB()

app=Flask(__name__)

#Main page
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

#Add book page
@app.route("/books/addBook", methods=['GET', 'POST'])
def addBook():
    if request.method=='POST':
        bName = request.form.get('bookName')
        bAuthor = request.form.get('Author')
        bYear = request.form.get('yearPublished')
        bType = request.form.get('bookType')
        cur.execute(f"INSERT INTO books VALUES('{bName}', '{bAuthor}', {int(bYear)}, {int(bType)})")
        con.commit()
    return render_template("/books/addBook.html")

#Show returned books page
@app.route("/books/returnBook")
def returnBook():
    return render_template("/loans/returnBook.html")

#Show all books page
@app.route("/books/showAllBooks", methods=['GET', 'POST'])
def showAllBooks():
    if request.method=='POST':
        pass
    sqlBooks = "SELECT * FROM books"
    cur.execute(sqlBooks)
    books = cur.fetchall()
    return render_template('/books/showAllBooks.html', books=books)

#Find specific book page
@app.route("/books/findBook", methods=['GET','POST'])
def findBook():
    if request.method=='POST':
        bookName = request.form.get('bookName')
        bookAuthor=request.form.get('bookAuthor')
        sql = (f"select * from books where bookName='{bookName}' and Author='{bookAuthor}'")
        cur.execute(sql)
        books = cur.fetchall()
        return render_template("/books/findBook.html", books=books)
    return render_template("/books/findBook.html")

#Remove book from database
@app.route("/books/removeBook", methods=['GET', 'POST'])
def removeBook():
    return render_template("/books/removeBook.html")

#Add a customer page
@app.route("/customers/addCustomer")
def addCustomer():
    return render_template("/customers/addCustomer.html")

#Remove a customer page
@app.route("/customers/removeCustomer")
def removeCustomer():
    return render_template("/customers/removeCustomer.html")

#Show all customers page
@app.route("/customers/showAllCustomers")
def showAllCustomers():
    return render_template("/customers/showAllCustomers.html")

#Find specific customer page
@app.route("/customers/findCustomer")
def findCustomer():
    return render_template("/customers/findCustomer.html")

#Loan book page
@app.route("/loans/loanBook")
def loanBook():
    return render_template("loanBook.html")

#Show all loaned books
@app.route("/loans/showAllLoans")
def showAllLoans():
    return render_template("/loans/showAllLoans.html")

#Show all LATE loans
@app.route("/loans/showAllLateLoans")
def showAllLateLoans():
    return render_template("/loans/showAllLateLoans.html")

if __name__=="__main__":
    app.run(debug=True)