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


#Login win1dow
win1 = tk.Tk()
win1.title("Employee login")

'--------------------------------------------------------------------------------------------------------------'
#Employee Name
EmpName = tk.StringVar()
tEmpName = tk.Entry(win1,font=('times new roman',16) ,textvariable=EmpName)
tEmpName.grid(column=5, row=7)
'---------------------------------------------------------------------------------------------------------------'
#------BG Image--------------
pic= PhotoImage(master = win1,file='BackgroundBL.png')
pic_label = Label(win1,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)


#Id field
log = tk.Label(win1, text="Employee ID: ")
log.grid(column=3, row=7)
log.configure(font=('times new roman',16), bg='white')

usr = tk.StringVar()
nameEntered = tk.Entry(win1, width=20, textvariable=usr)
nameEntered.grid(column=4, row=7)


#Pass field
bLabel = tk.Label(win1, text="Password: ")
bLabel.grid(column=5, row=7)
bLabel.configure(font=('times new roman',16), bg='white')

pas = tk.StringVar()
nameEntered = tk.Entry(win1, width=20, textvariable=pas, show='*')
nameEntered.grid(column=6, row=7)


# Adding a Login function

def login():
    
    try:
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()

        Id=usr.get()
        Epass=str(pas.get())
        
        cursor.execute("select * from employee where EmpID='"+str(Id)+"' and EmpPass = '"+str(Epass)+"'")
        ls = pd.DataFrame(cursor.fetchall())
        
                
        if(cursor.rowcount>0):
            cursor1 = conn.cursor()
            cursor1.execute("select EmpName from employee where EmpID = '"+str(Id)+"' and EmpPass = '"+str(Epass)+"'")
            ls = pd.DataFrame(cursor1.fetchall())
            EmpName.set(ls.iloc[0][0])
            mBox.showinfo('Logged in ', 'Welcome '+EmpName.get()+'')
                
            win1.destroy()
            import Emp_menu

        elif(usr.get()=='' or pas.get()==''):
                mBox.showerror("Error","Wrong user ID or password")

        else: 
            mBox.showerror('Error','Wrong user ID or password')

    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


#Back def
def Back():
    win1.destroy()
    import Menu
    
'''
#Forward
def Forward():

    import Emp_menu
    win1.destroy()
'''



#-------------Buttons----------------------

# Login Button

login = tk.Button(win1,font=('times new roman',16), text="Login", command=login)
login.grid(column=4, row=8, columnspan=2)

#Back to menu

back = tk.Button(win1,font=('times new roman',16), text="Main Menu", command=Back)
back.grid(column=7, row=9, columnspan=1)

















