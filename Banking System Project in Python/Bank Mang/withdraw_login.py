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


win6 = tk.Tk()
win6.title("Details Window")


#---------adding Bg Image---------------

pic6=PhotoImage(master=win6,file='BackgroundBlurBL.png')
pic6_label=Label(win6, image= pic6).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------

cb = tk.IntVar()
tcb = tk.Entry(win6,font=('arial',15), width=30, textvariable=cb)
tcb.grid(column=2, row=1,columnspan=3)

#Cust. Name
lcname = tk.Label(win6, text="Cust. Name : ")
lcname.grid(column=0, row=1,columnspan=3)
lcname.configure(font=('Times New Roman',15),width=25,bg='white')

cname = tk.StringVar()
tcname = tk.Entry(win6,font=('arial',15), width=30, textvariable=cname)
tcname.grid(column=2, row=1,columnspan=3)

#Amount
lamount = tk.Label(win6, text="Current Balance : ") 		
lamount.grid(column=0, row=4,columnspan=3)
lamount.configure(font=('Times New Roman',15),width=25,bg='white')

amount = tk.IntVar() 
tamount = tk.Entry(win6,font=('arial',15), width=30, textvariable=amount) 
tamount.grid(column=2, row=4,columnspan=3)

#Deposit
lwdrw = tk.Label(win6, text="Withdraw Amount : ") 		
lwdrw.grid(column=0, row=6,columnspan=3)
lwdrw.configure(font=('Times New Roman',15),width=25,bg='white')

wdrw = tk.IntVar() 
twdrw = tk.Entry(win6,font=('arial',15), width=30, textvariable=wdrw) 
twdrw.grid(column=2, row=6,columnspan=3)


f1= Frame(win6)
f1.grid(column=0, row=0,columnspan=5, rowspan=10)

pic10=PhotoImage(master=f1,file='C:/Users/tetra/Desktop/Bank Mang/BackgroundBlurBL.png')
pic10_label=Label(f1, image= pic10).grid(column=0,row=0,columnspan=5, rowspan=10)

#Cust Id
lcId = tk.Label(f1, text="Cust. ID : ")
lcId.grid(column=1, row=7)
lcId.configure(font=('Times New Roman',20))

cId = tk.IntVar()
tcId = tk.Entry(f1,font=('arial',15), width=30, textvariable=cId)
tcId.grid(column=2, row=7)

#Pass
lcpass = tk.Label(f1, text="Cust. Password : ") 		
lcpass.grid(column=3, row=7)
lcpass.configure(font=('Times New Roman',20))

cpass = tk.StringVar() 
tcpass = tk.Entry(f1,font=('arial',15), width=30, textvariable=cpass,show='*') 
tcpass.grid(column=4, row=7)

#-----------Commands-----------------

#Search Command
def search():
    try:
        
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select cname, amount from cust_table where cId = '" +str(cId.get())+ "' and cpass='"+str(cpass.get())+"'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            cname.set(ls.iloc[0][0])
            amount.set(ls.iloc[0][1])
            f1.destroy()
            login.destroy()
            
            
            
        else:
            mBox.showerror('Error', 'Data Not Found ; Check The Details ;)')
            
    except Error as e :
        print("Error while connecting to MySQL", e)

#Update Command        
def update():
    try:
     conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     cursor.execute("update cust_table set amount = '"+str(amount.get())+"' - '"+str(wdrw.get())+"' where cId = '" +str(cId.get())+ "'")
     conn.commit()

     cursor2 = conn.cursor()
     cursor2.execute("select amount from cust_table where cId = '" +str(cId.get())+"'" )
     ls = pd.DataFrame(cursor2.fetchall())
     if(len(ls.index)>0):
         cb.set(ls.iloc[0][0])
         
     if(cursor.rowcount>0):
         mBox.showinfo('Done:',"Your New Balance Is : '"+str(cb.get())+"'")
         win6.destroy()
         import Cust_menu
         
            
         
     else:
         print('Not Done!')
         mBox.showerror('Error!', 'Cannot Update ; Check The Details ;)')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")        

# Adding Login Button

update= tk.Button(win6,font=('Times New Roman',20) ,text='Withdraw Amount', command = update)
update.grid(column=2,row=9)

login = tk.Button(win6,font=('Times New Roman',20),width=15, text="Login!", command=search)
login.grid(column=1, row=9,columnspan=3)
