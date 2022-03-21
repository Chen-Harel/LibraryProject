from flask import redirect, render_template, request
import sqlite3


con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Customer:
    def __init__(self):
        pass

    def showAllCustomers(self):
        if request.method=='POST':
            pass
        sqlCustomers = '''SELECT * FROM customers'''
        cur.execute(sqlCustomers)
        customers = cur.fetchall()
        return render_template("/customers/showAllCustomers.html", customers=customers)

    def addCustomer(self):
        if request.method=='POST':
            custName = request.form.get('custName')
            custCity = request.form.get('custCity')
            custAge = request.form.get('custAge')
            cur.execute(f'''INSERT INTO customers VALUES(not null, "{custName}", "{custCity}", {int(custAge)})''')
            con.commit()
        return render_template("/customers/addCustomer.html")
    
    def removeCustomer(self):
        if request.method=='POST':
            cName = request.form.get('custName')
            cCity = request.form.get('custCity')
            cAge = request.form.get('custAge')
            sqlRem = (f'''DELETE FROM customers where cusName="{cName}" and cusCity="{cCity}" and cusAge={int(cAge)}''')
            cur.execute(sqlRem)
            con.commit()
            cRem="Customer removed!"
            goToBookDatabase="Click here"
            goBack="to go back."
            return redirect("/customers/removeCustomer.html", cRem=cRem, goToBookDatabase=goToBookDatabase, goBack=goBack)
        return render_template("/customers/removeCustomer.html")
    
    def findCustomer(self):
        if request.method=="POST":
            custName=request.form.get("custName")
            custCity=request.form.get("custCity")
            findCust = (f'''SELECT * FROM customers where cusName like "%{custName}%" and cusCity like "%{custCity}%"''')
            cur.execute(findCust)
            cust = cur.fetchall()
            return render_template("/customers/findCustomer.html", cust=cust)
        return render_template("/customers/findCustomer.html")
