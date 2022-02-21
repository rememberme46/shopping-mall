import mysql.connector as mc
from tabulate import tabulate
import os
from time import sleep
clear = lambda: os.system('cls')

mycon=mc.connect(host="localhost",user="root",password="nps@123",database="project")
if mycon.is_connected():
    print("connected")
    mycursor=mycon.cursor()


def disprecco():
    try:
        query=("select * from stock")
        mycursor.execute(query)
        result=mycursor.fetchall()
        table=[["ITEM CODE","ITEM NAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
        for rec in result:
            table.append(list(rec))
        print(tabulate(table))
    except:
        print("Choice Invalid")
    input("Press any key to Continue")
    
def addstockreco():
       try:
           itemcode=int(input("Enter Item Code:"))
           itemname=input("Enter Item Name:")
           qty=int(input("Enter Quantity in Stock:"))
           price=float(input("Enter Price of Item:"))
           discount=int(input("Enter Discount % Applicable:"))
           dom=input("Enter the DOM (YYYY-MM-DD)-:")
           query="insert into stock values({},'{}',{},{},{},'{}')".format(itemcode,itemname,qty,price,discount,dom)
           mycursor.execute(query)
           print("Record Succesfully Inserted")
           mycon.commit()
       except:
              print("Error")
       input("Press any key to Continue")

def delstockreco():
    try:
        itemd=int(input("Enter Item Code to be Deleted -:"))
        query="select * from stock where itemcode="+str(itemd)
        mycursor.execute(query)
        result=mycursor.fetchone()
        deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
        if result!=None:
            deltable.append(list(result))
            print(tabulate(deltable))
            ans=input("Do you want to Delete(Y/N)?:")
            if ans=="y" or ans=="Y":
                query="delete from stock where itemcode="+str(itemd)
                print("deleted")
        mycursor.execute(query)
        mycon.commit()   
    except:
        print("Error")
    input("Press any key to Continue")    
           

def searchreco():
    try:
        n=(input("Enter Item name for searching -:"))
        query="Select * from stock where itemname='%s'"%(n)
        mycursor.execute(query)
        result=mycursor.fetchone()
        table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
        if result!=None:
            table.append(list(result))
            print(tabulate(table))
            print("Record Found And Is Available")
        else:
            print("Record not available/Enter the correct Item Code")
    except:
        if result==None:
            print("Record not available/Enter the correct Item Code")
    input("Press any key to Continue") 

def modifystockreco():
       try:
              query=("select * from stock")
              mycursor.execute(query)
              result=mycursor.fetchall()
              table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
              for rec in result:
                     table.append(list(rec))
              print(tabulate(table))
              modtable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
              find=int(input("Enter Item Code For Modifying -:"))
              query="select * from stock where itemcode="+str(find)
              mycursor.execute(query)
              result=mycursor.fetchone()
              if result!=None:
                     print("What Do you Want to Modify?")
                     print("1.Item Name")
                     print("2.Quantity")
                     print("3.Price")
                     print("4.Discount")
                     print("5.DOM")
                     ch=int(input("Enter Your Choice -:"))
                     if ch==1:
                         i1=input("Enter New Item Name -:")
                         query="update stock set itemname='{}' where itemcode={}".format(i1,find)
                     elif ch==2:
                         i2=int(input("Enter New Quantity -:"))
                         query="update stock set qty={} where itemcode={}".format(i2,find)
                     elif ch==3:
                         i3=int(input("Enter New Price -:"))
                         query="update stock set price={} where itemcode={}".format(i3,find)
                     elif ch==4:
                         i4=int(input("Enter New Discount -:"))
                         query="update stock set itemname={} where itemcode={}".format(i4,find)
                     elif ch==5:
                         i5=input("Enter New DOM (YYYY-MM-DD) -:")
                         query="update stock set dom='{}' where itemcode={}".format(i5,find)
                        
              mycursor.execute(query)
              print("Record Modified")
              query="select * from stock where itemcode="+str(find)
              mycursor.execute(query)
              result=mycursor.fetchone()
              modtable.append(list(result))
              print(tabulate(modtable))
              mycon.commit()
       except:
              if result==None:
                     print("Record Not Available")
       input("Press any key to Continue")


def disbuyreco():
    try:
       query="select * from stock"
       mycursor.execute(query)
       result=mycursor.fetchall()
       table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
       for rec in result:
              table.append(list(rec))
       print(tabulate(table))
    except:
        
        input("Press Enter To Continue")


def purchase():
       global dtot
       dtot=0
       try:
           tot=0
           p1=int(input("Enter itemcode you want to buy -:"))
           p2=int(input("Enter number of quantity you want to buy -:"))
           mycursor.execute("use project")
           query=("select stock.price,stock.discount,stock.qty,sales.amount_pay from stock,sales where stock.itemcode={} and sales.customer_name='{}'").format(p1,i1)
           mycursor.execute(query)
           result=mycursor.fetchone()
           mycon.commit()
           a,b,c,dtot=result
           if dtot==None:
               dtot=0
           elif c>=p2:
               if c!=0:
                   d=c-p2
                   tot=tot+(p2*(a))
                   dtot+=tot*((100-b)/100)
                   query=("update sales set amount_pay={} where customer_name='{}'").format(dtot,i1)
                   mycursor.execute(query)
                   mycon.commit()
                   query=("update stock set qty={} where itemcode={}").format(d,p1)
                   mycursor.execute(query)
                   mycon.commit()
                   input("ADDED TO CART,Press to continue")
               elif c==0:
                   print("OUT OF STOCK")
               input("Press Enter to continue")
           else:
               print("Quantity Entered exceeds stock amount")
               input("Press enter to continue")
                     
       except:
           '''if i1.isnumeric():
               print("we")
           else:
               print("hfhuehfuhe")'''
       input("Please use valid choice")
              

def viewbill():
    query=("select customer_name,amount_pay from sales where customer_name='{}'").format(i1)
    mycursor.execute(query)
    result=mycursor.fetchone()
    print("======BILL======")
    table=[["NAME","AMOUNT PAYABALE"]]
    table.append(list(result))
    print(tabulate(table))
    input("Press Enter To Continue")

def adddetail():
    global i1
    i1=input("Enter Customer Name:")
    i2=int(input("Enter Customer Phone Number:"))
    query="insert into sales(customer_name,phone_no) values('{}',{})".format(i1,i2)
    mycursor.execute(query)
    mycon.commit()
    input("Press Enter To Continue")

def dispsale():
    try:
        query=("select * from sales")
        mycursor.execute(query)
        result=mycursor.fetchall()
        table=[["NAME","PHONE NO.","AMOUNT RECIEVED"]]
        for rec in result:
            table.append(list(rec))
        print(tabulate(table))
    except:
        print("Invalid Input")
    input("Press Enter To Continue")


def menu1():
    while True:
        print("=========MENU=========")
        tab=[["==Select Your Choice=="],["1.VIEW INVENTORY AND BUY"],["2.View Bill"],["3.Exit"]]
        print(tabulate(tab))
        ch=input("Enter Your Choice:")
        if ch=='':
           ch=0
           print("Please enter the choice between 1 and 6")
        else:
           ch=int(ch)
        if int(ch)==1:
            disbuyreco()
            purchase()
        elif ch==2:
            viewbill()
        elif ch==3:
            break
        else:
            print("Invalid Choice")


def menu2():
    while True:
        print("=========MENU=========")
        tab=[["==Select Your Choice=="],["1.Display Stock Record"],["2.Add Stock Record"],["3.Modify Stock Record"],["4.Delete Stock Record"],["5.Search Stock Record"],["6.Display All Sales"],["7.Exit"]]
        print(tabulate(tab))
        ch=input("Enter Your Choice:")
        if ch=='':
           ch=0
           print("Please enter the choice between 1 and 7")
        else:
           ch=int(ch)
        if ch==1:

            disprecco()
        elif ch==2:

            addstockreco()
        elif ch==3:
            clear()
            modifystockreco()
        elif ch==4:

            delstockreco()
        elif ch==5:
            clear()
            searchreco()
        elif ch==6:

            dispsale()
        elif ch==7:
            break
        else:
            print("Invalid Choice")


while True:
    print("=========MENU=========")
    mn=[["---Select Your Choice---"],["1.Customer Mode"],["2.Employee Mode"],["3.Exit"]]
    print(tabulate(mn))
    ch=input("Enter Your Choice:")
    if ch=='':
        ch=0
        print("Please enter the choice between 1 and 6")
    else:
        ch=int(ch)
    if ch==1:
        adddetail()
        
        menu1()

    elif ch==2:

        menu2()

    elif ch==3:

        break
    else:
        print("Invalid Choice")

