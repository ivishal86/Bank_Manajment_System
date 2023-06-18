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
win7.title("Update Employee")

#---------adding Bg Image---------------

pic7=PhotoImage(master=win7,file='BackgroundBlurBL.png')
pic7_label=Label(win7, image= pic7).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------
#Employee ID
lEmpID = tk.Label(win7, text="Emp. ID : ")
lEmpID.grid(column=0, row=0,columnspan=2)
lEmpID.configure(font=('Times New Roman',15), bg='white')

EmpID = tk.IntVar()
tEmpID = tk.Entry(win7,font=('arial',15), width=30, textvariable=EmpID)
tEmpID.grid(column=2, row=0,columnspan=3)


#Employee Name
lEmpName = tk.Label(win7, text="Emp. Name : ")
lEmpName.grid(column=0, row=1,columnspan=2)
lEmpName.configure(font=('Times New Roman',15), bg='white')

EmpName = tk.StringVar()
tEmpName = tk.Entry(win7,font=('arial',15), width=30, textvariable=EmpName)
tEmpName.grid(column=2, row=1,columnspan=3)

#Employee Mail ID
lEmpMail = tk.Label(win7, text="Emp. Mail Id : ") 		
lEmpMail.grid(column=0, row=2,columnspan=2)
lEmpMail.configure(font=('Times New Roman',15), bg='white')

EmpMail = tk.StringVar() 
tEmpMail = tk.Entry(win7,font=('arial',15), width=30, textvariable=EmpMail) 
tEmpMail.grid(column=2, row=2,columnspan=3)

#Employee Password
lEmpPass = tk.Label(win7, text="Emp. Password : ") 		
lEmpPass.grid(column=0, row=3,columnspan=2)
lEmpPass.configure(font=('Times New Roman',15), bg='white')

EmpPass = tk.StringVar() 
tEmpPass = tk.Entry(win7,font=('arial',15), width=30, textvariable=EmpPass) 
tEmpPass.grid(column=2, row=3,columnspan=3)

#Employee Contact No.
lEmpNumber = tk.Label(win7, text="Emp. Contact No. : ") 		
lEmpNumber.grid(column=0, row=4,columnspan=2)
lEmpNumber.configure(font=('Times New Roman',15), bg='white')

EmpNumber = tk.IntVar() 
tEmpNumber = tk.Entry(win7,font=('arial',15), width=30, textvariable=EmpNumber) 
tEmpNumber.grid(column=2, row=4,columnspan=3)

#Employee Age
lAge = tk.Label(win7, text="Emp. Age : ") 		
lAge.grid(column=0, row=5,columnspan=2)
lAge.configure(font=('Times New Roman',15), bg='white')

Age = tk.IntVar() 
tAge = tk.Entry(win7,font=('arial',15), width=30, textvariable=Age) 
tAge.grid(column=2, row=5,columnspan=3)

#Gender
lEmpGender = tk.Label(win7, text="Emp. Gender : ") 		
lEmpGender.grid(column=0, row=6,columnspan=2)
lEmpGender.configure(font=('Times New Roman',15), bg='white')

EmpGender = tk.StringVar() 
tEmpGender = ttk.Combobox(win7,font=('arial',15), width=29, textvariable=EmpGender,state='readonly') 
tEmpGender['values']=('M','F','O')
tEmpGender.grid(column=2, row=6,columnspan=3)


#-----------Commands-----------------

#Search Command
def search():
    try:
        
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select EmpID, EmpName, EmpMail, EmpPass, EmpNumber, Age, EmpGender from employee where EmpID = '" +str(EmpID.get())+ "'")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            EmpID.set(ls.iloc[0][0])
            EmpName.set(ls.iloc[0][1])
            EmpMail.set(ls.iloc[0][2])
            EmpPass.set(ls.iloc[0][3])
            EmpNumber.set(ls.iloc[0][4])
            Age.set(ls.iloc[0][5])
            EmpGender.set(ls.iloc[0][6])
            
            
        else:
            mBox.showerror('Error', 'Data not found. Check the details.)')
            
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")

#Update Command        
def update():
    try:
     conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
     cursor = conn.cursor()
     cursor.execute("update employee set EmpName='"+str(EmpName.get())+"', EmpMail='"+str(EmpMail.get())+"', EmpPass='"+str(EmpPass.get())+"', EmpNumber='"+str(EmpNumber.get())+"', Age='"+str(Age.get())+"', EmpGender='"+str(EmpGender.get())+"' where EmpID = '" +str(EmpID.get())+ "'")
     conn.commit()
     if(cursor.rowcount>0):
         mBox.showinfo('Done', 'Updated!')
         EmpID.set('')
         EmpName.set('')
         EmpMail.set('')
         EmpPass.set('')
         EmpNumber.set('')
         Age.set('')
         EmpGender.set('')
            
         
     else:
         print('Not Done!')
         mBox.showerror('Error!', 'Cannot update. Check the details.)')
    except Error as e :
     print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


def Emp():
    
    import Emp_menu
    win7.destroy()



#------Buttons-------------
        
#Search
search=tk.Button(win7,font=('times new roman',16), text="Search For Emp.",command=search)
search.grid(column=2, row=7,columnspan=2)

#Update
update=tk.Button(win7,font=('times new roman',16), text="Update The Emp.",command=update)
update.grid(column=1, row=7,columnspan=1)

#Back to Menu
back=tk.Button(win7,font=('times new roman',16), text="Emp. Menu",command=Emp)
back.grid(column=4, row=7,columnspan=1)













