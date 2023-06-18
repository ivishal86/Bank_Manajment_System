import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import *
import mysql.connector
from mysql.connector import Error


win8 = tk.Tk()
win8.title("Details Window")

#---------adding Bg Image---------------

pic8=PhotoImage(master=win8,file='BackgroundBlurBL.png')
pic8_label=Label(win8, image= pic8).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------
#Cust Id
lcId = tk.Label(win8, text="Cust. ID : ",width=20)
lcId.grid(column=0, row=0,columnspan=2)
lcId.configure(font=('Times New Roman',15))

cId = tk.IntVar()
tcId = tk.Entry(win8,font=('arial',15), width=30, textvariable=cId)
tcId.grid(column=2, row=0,columnspan=3)


#Cust. Name
lcname = tk.Label(win8, text="Cust. Name : ",width=20)
lcname.grid(column=0, row=1,columnspan=2)
lcname.configure(font=('Times New Roman',15))

cname = tk.StringVar()
tcname = tk.Entry(win8,font=('arial',15), width=30, textvariable=cname,state = "readonly")
tcname.grid(column=2, row=1,columnspan=3)

#Mail Id
lcmail = tk.Label(win8, text="Cust. Mail Id : ",width=20) 		
lcmail.grid(column=0, row=2,columnspan=2)
lcmail.configure(font=('Times New Roman',15))

cmail = tk.StringVar() 
tcmail = tk.Entry(win8,font=('arial',15), width=30, textvariable=cmail,state = "readonly") 
tcmail.grid(column=2, row=2,columnspan=3)

#Pass
lcpass = tk.Label(win8, text="Cust. Password : ",width=20) 		
lcpass.grid(column=0, row=3,columnspan=2)
lcpass.configure(font=('Times New Roman',15))

cpass = tk.StringVar() 
tcpass = tk.Entry(win8,font=('arial',15), width=30, textvariable=cpass,state = "readonly") 
tcpass.grid(column=2, row=3,columnspan=3)

#ContactNo
lcNo = tk.Label(win8, text="Cust. Contact No. : ",width=20) 		
lcNo.grid(column=0, row=4,columnspan=2)
lcNo.configure(font=('Times New Roman',15))

cNo = tk.IntVar() 
tcNo = tk.Entry(win8,font=('arial',15), width=30, textvariable=cNo,state = "readonly") 
tcNo.grid(column=2, row=4,columnspan=3)

#Cust. Age
lcAge = tk.Label(win8, text="Cust. Age : ",width=20) 		
lcAge.grid(column=0, row=5,columnspan=2)
lcAge.configure(font=('Times New Roman',15))

cAge = tk.IntVar() 
tcAge = tk.Entry(win8,font=('arial',15), width=30, textvariable=cAge,state = "readonly") 
tcAge.grid(column=2, row=5,columnspan=3)

#Amount
lamount = tk.Label(win8, text="Amount In The Acc : ",width=20) 		
lamount.grid(column=0, row=6,columnspan=2)
lamount.configure(font=('Times New Roman',15))

amount = tk.IntVar() 
tamount = tk.Entry(win8,font=('arial',15), width=30, textvariable=amount,state = "readonly") 
tamount.grid(column=2, row=6,columnspan=3)


#Gender
lcgender = tk.Label(win8, text="Gender : ",width=20) 		
lcgender.grid(column=0, row=7,columnspan=2)
lcgender.configure(font=('Times New Roman',15))

cgender = tk.StringVar() 
tcgender = tk.Entry(win8,font=('arial',15), width=30, textvariable=cgender,state='readonly') 
tcgender.grid(column=2, row=7,columnspan=3)

#Date of creation
lDOC = tk.Label(win8, text="Date Of Creation : ",width=20) 		
lDOC.grid(column=0, row=8,columnspan=2)
lDOC.configure(font=('Times New Roman',15))

DOC = tk.StringVar() 
tDOC = tk.Entry(win8,font=('arial',15), width=30,bd=3, textvariable=DOC,state = "readonly") 
tDOC.grid(column=2, row=8,columnspan=3)


#-----------Commands-----------------

#Search Command
def search():
    try:
        
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select cId,cname, cmail, cpass, cNo, cAge, amount, cgender, date_of_creation from cust_table where cId = '" +str(cId.get())+ "'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            cId.set(ls.iloc[0][0])
            cname.set(ls.iloc[0][1])
            cmail.set(ls.iloc[0][2])
            cpass.set(ls.iloc[0][3])
            cNo.set(ls.iloc[0][4])
            cAge.set(ls.iloc[0][5])
            amount.set(ls.iloc[0][6])
            cgender.set(ls.iloc[0][7])
            DOC.set(ls.iloc[0][8])
            
            
        else:
            mBox.showerror('Error', 'Data Not Found ; Check The Details ;)')
            
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


#Delete Command
def delete():
    try:
     conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     row = cursor.execute("delete from cust_table where cId='"+str(cId.get())+"' ")
     if(cursor.rowcount>0):
         mBox.showinfo('Done', 'Deleted!')
         cId.set('')
         cname.set('')
         cmail.set('')
         cpass.set('')
         cNo.set('')
         cAge.set('')
         amount.set('')
         cgender.set('')
         DOC.set('')
         #win8.destroy()
         #import Cust_menu
         
     else:
         mBox.showerror('Error','Cannot Delete')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")
        conn.commit()

def Back():
    win8.destroy()
    import Cust_menu




#------Buttons-------------
        
#Search
search=tk.Button(win8,font=('arial',16), text="Search For Acc",command=search)
search.grid(column=4, row=3,columnspan=3)

#Delete
Delete=tk.Button(win8,font=('arial',16), text="Delete The Acc",command=delete)
Delete.grid(column=4, row=5,columnspan=3)

#Back to Menu
back=tk.Button(win8,font=('Times New Roman',12), text="Back to Cust Menu",command=Back)
back.grid(column=4, row=9,columnspan=3)




        
