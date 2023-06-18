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


win4 = tk.Tk()
win4.title("Details Window")

#---------adding Bg Image---------------

pic4=PhotoImage(master=win4,file='BackgroundBlurBL.png')
pic4_label=Label(win4, image= pic4).grid(column=0,row=0,columnspan=20, rowspan=20)

#--------Creating Frames For Diff Labels And Commands-----------------

f1 = Frame(win4)
f1.grid(column=0,row=0,columnspan=20)

f2 = ttk.LabelFrame(win4)
f2.grid(column=10, row=5)

f3 = ttk.LabelFrame(win4)
f3.grid(column=0, row=10)

f4 = Frame(win4)
f4.grid(column=0,row=2,columnspan=20)

f5 = ttk.LabelFrame(win4)
f5.grid(column=0, row=10)

f6 = Frame(win4)
f6.grid(column=0, row=15)

lshow = tk.Label(f1, text="Show : ",font=('Times New Roman',15)).grid(column=0,row=0,padx=10)
show = tk.StringVar() 
tshow = ttk.Combobox(f1,font=('arial',15), textvariable=show,state='readonly') 
tshow['values']=('Show All','Specific Acc')
tshow.grid(column=2, row=0)


#--------Column Name---------------
lcId = tk.Label(f2, text="Cust. ID : ",font=('Times New Roman',15)).grid(column=0,row=0)
lcname = tk.Label(f2, text="Cust. Name : ",font=('Times New Roman',15)).grid(column=1,row=0)
lcmail = tk.Label(f2, text="Cust. Mail Id : ",font=('Times New Roman',15)).grid(column=2,row=0)
lcNo = tk.Label(f2, text="Cust. Contact No. : ",font=('Times New Roman',15)).grid(column=3,row=0)
lcAge = tk.Label(f2, text="Cust. Age : ",font=('Times New Roman',15)).grid(column=4,row=0)
lamount = tk.Label(f2, text="Opening Amount : ",font=('Times New Roman',15)).grid(column=5,row=0)
lcgender = tk.Label(f2, text="Gender : ",font=('Times New Roman',15)).grid(column=6,row=0)
lDOC = tk.Label(f2, text="Date Of Creation : ",font=('Times New Roman',15)).grid(column=7,row=0)
#----------Table-------------------------------------
def Back():
    win4.destroy()
    import Cust_menu
    

def submit() :
   
    a = show.get()
    if a =='Show All':
        f2.destroy()

        lcId = tk.Label(f3, text="Cust. ID : ",font=('Times New Roman',15)).grid(column=0,row=0)
        lcname = tk.Label(f3, text="Cust. Name : ",font=('Times New Roman',15)).grid(column=1,row=0)
        lcmail = tk.Label(f3, text="Cust. Mail Id : ",font=('Times New Roman',15)).grid(column=2,row=0)
        lcNo = tk.Label(f3, text="Cust. Contact No. : ",font=('Times New Roman',15)).grid(column=3,row=0)
        lcAge = tk.Label(f3, text="Cust. Age : ",font=('Times New Roman',15)).grid(column=4,row=0)
        lamount = tk.Label(f3, text="Opening Amount : ",font=('Times New Roman',15)).grid(column=5,row=0)
        lcgender = tk.Label(f3, text="Gender : ",font=('Times New Roman',15)).grid(column=6,row=0)
        lDOC = tk.Label(f3, text="Date Of Creation : ",font=('Times New Roman',15)).grid(column=7,row=0)

        
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select cId,cname, cmail, cNo, cAge,amount, cgender, date_of_creation from cust_table ")
        ls = pd.DataFrame(cursor.fetchall())
  
        for i in range(1, len(ls.index)):
            for j in range(0, len(ls.columns)):
                b = tk.Entry(f3)
                b.insert(0, ls.iloc[i][j])
                b.grid(row=i, column=j,padx=10,pady=10)
                b.config(state = "readonly")
        conn.commit()

    else :
        
        f3.destroy()
        f2.destroy()
        lcId = tk.Label(f4, text="Cust. ID : ",font=('Times New Roman',15)).grid(column=0,row=3)
        cId = tk.IntVar()
        tcId = tk.Entry(f4,font=('arial',15), width=30, textvariable=cId)
        tcId.grid(column=2, row=3)
        
        lpass = tk.Label(f4, text="Cust. Pass. : ",font=('Times New Roman',15)).grid(column=4,row=3)
        cpass = tk.StringVar() 
        tcpass = tk.Entry(f4,font=('arial',15), width=30, textvariable=cpass,show='*') 
        tcpass.grid(column=6, row=3)
        

        def submit2() :

            lcId = tk.Label(f5, text="Cust. ID : ",font=('Times New Roman',15)).grid(column=0,row=0)
            lcname = tk.Label(f5, text="Cust. Name : ",font=('Times New Roman',15)).grid(column=1,row=0)
            lcmail = tk.Label(f5, text="Cust. Mail Id : ",font=('Times New Roman',15)).grid(column=2,row=0)
            lcNo = tk.Label(f5, text="Cust. Contact No. : ",font=('Times New Roman',15)).grid(column=3,row=0)
            lcAge = tk.Label(f5, text="Cust. Age : ",font=('Times New Roman',15)).grid(column=4,row=0)
            lamount = tk.Label(f5, text="Opening Amount : ",font=('Times New Roman',15)).grid(column=5,row=0)
            lcgender = tk.Label(f5, text="Gender : ",font=('Times New Roman',15)).grid(column=6,row=0)
            lDOC = tk.Label(f5, text="Date Of Creation : ",font=('Times New Roman',15)).grid(column=7,row=0)

            
            conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
            cursor = conn.cursor()
            cursor.execute("select cId,cname, cmail, cNo, cAge,amount, cgender, date_of_creation from cust_table where cId = '" +str(cId.get())+ "' and cpass='"+str(cpass.get())+"'" )
            ls = pd.DataFrame(cursor.fetchall())
  
            for i in range(0, len(ls.index)):
                for j in range(0, len(ls.columns)):
                    b = tk.Entry(f5)
                    b.insert(0, ls.iloc[i][j])
                    b.grid(row=1, column=j,padx=10,pady=10)
                    b.config(state = "readonly")

            conn.commit()
            

        sub2= tk.Button(f4, text='Submit', command=submit2)
        sub2.grid(column=7, row=3)   
    #Back to Menu
    back=tk.Button(f6,font=('Times New Roman',12), text="Back to Cust Menu",command=Back)
    back.grid(column=0, row=0,columnspan=1)

#------------------------------------------------------    
sub= tk.Button(f1,font=('Times New Roman',12) ,text='Submit', command=submit)
sub.grid(column=3, row=0)

#Back to Menu


tk.mainloop()
