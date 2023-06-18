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

win3 = tk.Tk()
win3.title("Hire Employee")

#---------adding Bg Image---------------

pic3=PhotoImage(master=win3,file='BackgroundBlurBL.png')
pic3_label=Label(win3, image= pic3).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------
#Employee ID
EmpID = tk.IntVar()
tEmpID = tk.Entry(win3,font=('arial',15), width=30, textvariable=EmpID)
tEmpID.grid(column=2, row=5,columnspan=3)

#Employee Name
lEmpName = tk.Label(win3, text="Emp. Name: ")
lEmpName.grid(column=0, row=1,columnspan=2)
lEmpName.configure(font=('Times New Roman',15), bg='white')

EmpName = tk.StringVar()
tEmpName = tk.Entry(win3,font=('arial',15), width=30, textvariable=EmpName)
tEmpName.grid(column=2, row=1,columnspan=3)

#Employee Mail ID
lEmpMail = tk.Label(win3, text="Emp. Mail ID: ") 		
lEmpMail.grid(column=0, row=2,columnspan=2)
lEmpMail.configure(font=('Times New Roman',15), bg='white')

EmpMail = tk.StringVar() 
tEmpMail = tk.Entry(win3,font=('arial',15), width=30, textvariable=EmpMail) 
tEmpMail.grid(column=2, row=2,columnspan=3)

#Employee Password
lEmpPass = tk.Label(win3, text="Emp. Password: ") 		
lEmpPass.grid(column=0, row=3,columnspan=2)
lEmpPass.configure(font=('Times New Roman',15), bg='white')

EmpPass = tk.StringVar() 
tEmpPass = tk.Entry(win3,font=('arial',15), width=30, textvariable=EmpPass) 
tEmpPass.grid(column=2, row=3,columnspan=3)

#Employee Contact No
lEmpNumber = tk.Label(win3, text="Emp. Contact No.: ") 		
lEmpNumber.grid(column=0, row=4,columnspan=2)
lEmpNumber.configure(font=('Times New Roman',15), bg='white')

EmpNumber = tk.IntVar() 
tEmpNumber = tk.Entry(win3,font=('arial',15), width=30, textvariable=EmpNumber) 
tEmpNumber.grid(column=2, row=4,columnspan=3)

#Employee Age
lAge = tk.Label(win3, text="Emp. Age: ") 		
lAge.grid(column=0, row=5,columnspan=2)
lAge.configure(font=('Times New Roman',15), bg='white')

Age = tk.IntVar() 
tAge = tk.Entry(win3,font=('arial',15), width=30, textvariable=Age) 
tAge.grid(column=2, row=5,columnspan=3)

#Employee Gender
lEmpGender = tk.Label(win3, text="Emp. Gender: ") 		
lEmpGender.grid(column=0, row=6,columnspan=2)
lEmpGender.configure(font=('Times New Roman',15), bg='white')

EmpGender = tk.StringVar() 
tEmpGender = ttk.Combobox(win3,font=('arial',15), width=29, textvariable=EmpGender,state='readonly') 
tEmpGender['values']=('M','F','O')
tEmpGender.grid(column=2, row=6,columnspan=3)

#Employee Hiring
lHireDate = tk.Label(win3, text="Date of Hiring: ") 		
lHireDate.grid(column=0, row=7,columnspan=2)
lHireDate.configure(font=('Times New Roman',15), bg='white')

HireDate = tk.StringVar() 
tHireDate = tk.Entry(win3,font=('arial',15), width=30, textvariable=HireDate) 
tHireDate.grid(column=2, row=7,columnspan=3)


#-----------Commands-----------------

#Current Date command
        
def Cdate():
    try:
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor2 = conn.cursor()
        cursor2.execute("select curdate()")
        ls = pd.DataFrame(cursor2.fetchall())
        if(len(ls.index)>0):
            HireDate.set(ls.iloc[0][0])
            
            
        else:
            mBox.showinfo('!....IIIISH....!', 'Not Found')
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


#Insert Command
def insert(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8') 
        cursor = conn.cursor()
        
        Name = EmpName.get()
        Mail = EmpMail.get() 
        Pass = EmpPass.get() 
        No = EmpNumber.get()
        Gender = EmpGender.get()
        age = Age.get()
        Hire = HireDate.get()

        cursor.execute("insert into employee( EmpName, EmpID, EmpMail, EmpPass, EmpNumber, EmpGender, Age, HireDate) values('" +str(Name)+ "', 0, '" +str(Mail)+"','" +str(Pass)+"','" +str(No)+"','" +str(Gender)+"','" +str(age)+"','" +str(Hire)+"')")

        cursor1 = conn.cursor()
        cursor1.execute("select EmpID from employee where EmpNumber = '" +str(EmpNumber.get())+ "'")
        ls = pd.DataFrame(cursor1.fetchall())
        if(len(ls.index)>0):
            EmpID.set(ls.iloc[0][0])

        if(cursor.rowcount>0): 
            mBox.showinfo('Emp. ID is: ', EmpID.get())

            
            EmpName.set('')
            EmpMail.set('')
            EmpPass.set('')
            EmpNumber.set('')
            EmpGender.set('')
            Age.set('')
            HireDate.set('')
        else: 
             mBox.showerror('Warning!', 'Not Found')
             mBox.configure(backcolor='pink')
        conn.commit()
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
         


def Emp():
    
    import Emp_menu
    win3.destroy()



#------Buttons-------------

#Insert
insert=tk.Button(win3,font=('times new roman',16), text="Insert Details" ,command=insert) 
insert.grid(column=1, row=8,columnspan=1)

#Today's Date
Cdate = tk.Button(win3,font = ('times new roman', 12), text="Today's Date", command=Cdate) 
Cdate.grid(column=4, row=7,columnspan=3)

#Back to Menu
back=tk.Button(win3,font=('times new roman',16), text="Emp. Menu",command=Emp)
back.grid(column=2, row=8,columnspan=1)









