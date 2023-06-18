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


win7 = tk.Tk()
win7.title("Details Window")

#---------adding Bg Image---------------

pic7=PhotoImage(master=win7,file='BackgroundBlurBL.png')
pic7_label=Label(win7, image= pic7).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------
#Cust Id
lcId = tk.Label(win7, text="Cust. ID : ",width=20)
lcId.grid(column=0, row=0,columnspan=2)
lcId.configure(font=('Times New Roman',15))

cId = tk.IntVar()
tcId = tk.Entry(win7,font=('arial',15), width=30, textvariable=cId)
tcId.grid(column=2, row=0,columnspan=3)


#Cust. Name
lcname = tk.Label(win7, text="Cust. Name : ",width=20)
lcname.grid(column=0, row=1,columnspan=2)
lcname.configure(font=('Times New Roman',15))

cname = tk.StringVar()
tcname = tk.Entry(win7,font=('arial',15), width=30, textvariable=cname)
tcname.grid(column=2, row=1,columnspan=3)

#Mail Id
lcmail = tk.Label(win7, text="Cust. Mail Id : ",width=20) 		
lcmail.grid(column=0, row=2,columnspan=2)
lcmail.configure(font=('Times New Roman',15))

cmail = tk.StringVar() 
tcmail = tk.Entry(win7,font=('arial',15), width=30, textvariable=cmail) 
tcmail.grid(column=2, row=2,columnspan=3)

#Pass
lcpass = tk.Label(win7, text="Cust. Password : ",width=20) 		
lcpass.grid(column=0, row=3,columnspan=2)
lcpass.configure(font=('Times New Roman',15))

cpass = tk.StringVar() 
tcpass = tk.Entry(win7,font=('arial',15), width=30, textvariable=cpass) 
tcpass.grid(column=2, row=3,columnspan=3)

#ContactNo
lcNo = tk.Label(win7, text="Cust. Contact No. : ",width=20) 		
lcNo.grid(column=0, row=4,columnspan=2)
lcNo.configure(font=('Times New Roman',15))

cNo = tk.IntVar() 
tcNo = tk.Entry(win7,font=('arial',15), width=30, textvariable=cNo) 
tcNo.grid(column=2, row=4,columnspan=3)

#Cust. Age
lcAge = tk.Label(win7, text="Cust. Age : ",width=20) 		
lcAge.grid(column=0, row=5,columnspan=2)
lcAge.configure(font=('Times New Roman',15))

cAge = tk.IntVar() 
tcAge = tk.Entry(win7,font=('arial',15), width=30, textvariable=cAge) 
tcAge.grid(column=2, row=5,columnspan=3)

#Gender
lcgender = tk.Label(win7, text="Gender : ",width=20) 		
lcgender.grid(column=0, row=6,columnspan=2)
lcgender.configure(font=('Times New Roman',15))

cgender = tk.StringVar() 
tcgender = ttk.Combobox(win7,font=('arial',15), width=29, textvariable=cgender,state='readonly') 
tcgender['values']=('M','F','O')
tcgender.grid(column=2, row=6,columnspan=3)


#-----------Commands-----------------

#Search Command
def search():
    try:
        
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select cId,cname, cmail, cpass, cNo, cAge, cgender from cust_table where cId = '" +str(cId.get())+ "'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            cId.set(ls.iloc[0][0])
            cname.set(ls.iloc[0][1])
            cmail.set(ls.iloc[0][2])
            cpass.set(ls.iloc[0][3])
            cNo.set(ls.iloc[0][4])
            cAge.set(ls.iloc[0][5])
            cgender.set(ls.iloc[0][6])
            
            
        else:
            mBox.showerror('Error', 'Data Not Found ; Check The Details ;)')
            
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")

#Update Command        
def update():
    try:
     conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     cursor.execute("update cust_table set cname='"+str(cname.get())+"', cmail='"+str(cmail.get())+"',cpass='"+str(cpass.get())+"', cNo='"+str(cNo.get())+"',cAge='"+str(cAge.get())+"', cgender='"+str(cgender.get())+"' where cId = '" +str(cId.get())+ "'")
     conn.commit()
     if(cursor.rowcount>0):
         mBox.showinfo('Done', 'Updated!')
         cId.set('')
         cname.set('')
         cmail.set('')
         cpass.set('')
         cNo.set('')
         cAge.set('')
         cgender.set('')
            
         
     else:
         print('Not Done!')
         mBox.showerror('Error!', 'Cannot Update ; Check The Details ;)')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")

def Back():
    win7.destroy()
    import Cust_menu


#------Buttons-------------
        
#Search
search=tk.Button(win7,font=('arial',16), text="Search For Acc",command=search)
search.grid(column=2, row=8,columnspan=2)

#Update
update=tk.Button(win7,font=('arial',16), text="Update The Acc",command=update)
update.grid(column=1, row=8,columnspan=1)


#Back to Menu
back=tk.Button(win7,font=('Times New Roman',12), text="Back to Cust Menu",command=Back)
back.grid(column=4, row=9,columnspan=1)











