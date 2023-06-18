'''import tkinter as tk
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
win4.title("Employee Details")

#---------adding Bg Image---------------

pic4=PhotoImage(master=win4,file='C:/Users/L/Desktop/CODING/Project/BackgroundBlurBL.png')
pic4_label=Label(win4, image= pic4).grid(column=0,row=0,columnspan=10, rowspan=10)


#f1= tframe(win4, text='Values')
#--------Column Name---------------
lEmpName = tk.Label(win4, text="Emp. Name: ",font=('Times New Roman',15)).grid(column=0,row=0)
lEmpID = tk.Label(win4, text="Emp. ID: ",font=('Times New Roman',15)).grid(column=1,row=0)
lEmpMail = tk.Label(win4, text="Emp. Mail ID: ",font=('Times New Roman',15)).grid(column=2,row=0)
lEmpNumber = tk.Label(win4, text="Emp. No.: ",font=('Times New Roman',15)).grid(column=3,row=0)
lAge = tk.Label(win4, text="Emp. Age: ",font=('Times New Roman',15)).grid(column=4,row=0)
lEmpGender = tk.Label(win4, text="Emp. Gender: ",font=('Times New Roman',15)).grid(column=5,row=0)
lHireDate= tk.Label(win4, text="Date of Hiring: ",font=('Times New Roman',15)).grid(column=6,row=0)
#----------Table-------------------------------------

try:
    
    conn = mysql.connector.connect(host='localhost',database='project',user='root',password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select EmpName, EmpID, EmpMail, EmpNumber, Age, EmpGender, HireDate from employee")
    ls = pd.DataFrame(cursor.fetchall())
  
    for i in range(1, len(ls.index)):
        for j in range(0, len(ls.columns)):
            b = tk.Entry(win4)
            b.insert(0, ls.iloc[i][j])
            b.grid(row=i, column=j)
            b.config(state = "readonly")
    conn.commit()        
            
except Error as e :
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")



    
def Emp():
    
    import Emp_menu
    win4.destroy()

#Back to Menu
back=tk.Button(win4,font=('times new roman',16), text="Emp. Menu",command=Emp)
back.grid(column=3, row=8,columnspan=1)


tk.mainloop()

'''

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
f6.grid(column=0,row=15,columnspan=20)

lshow = tk.Label(f1, text="Show: ",font=('times new roman',15)).grid(column=0,row=0,padx=10)
show = tk.StringVar() 
tshow = ttk.Combobox(f1,font=('times new roman',15), textvariable=show,state='readonly') 
tshow['values']=('Show All','Specific Acc')
tshow.grid(column=2, row=0)


#--------Column Name---------------
lEmpID = tk.Label(f2, text="Emp. ID: ",font=('Times New Roman',15)).grid(column=0,row=0)
lEmpName = tk.Label(f2, text="Emp. Name: ",font=('Times New Roman',15)).grid(column=1,row=0)
lEmpMail = tk.Label(f2, text="Emp. Mail ID: ",font=('Times New Roman',15)).grid(column=2,row=0)
lEmpNumber = tk.Label(f2, text="Emp. Contact No.: ",font=('Times New Roman',15)).grid(column=3,row=0)
lAge = tk.Label(f2, text="Emp. Age: ",font=('Times New Roman',15)).grid(column=4,row=0)
lEmpGender = tk.Label(f2, text="Emp. Gender: ",font=('Times New Roman',15)).grid(column=5,row=0)
lHireDate = tk.Label(f2, text="Date Of Hiring: ",font=('Times New Roman',15)).grid(column=6,row=0)
#----------Table-------------------------------------
def submit() :
    a = show.get()
    if a =='Show All':
        f2.destroy()

        lEmpID = tk.Label(f3, text="Emp. ID: ",font=('Times New Roman',15)).grid(column=0,row=0)
        lEmpName = tk.Label(f3, text="Emp. Name: ",font=('Times New Roman',15)).grid(column=1,row=0)
        lEmpMail = tk.Label(f3, text="Emp. Mail ID: ",font=('Times New Roman',15)).grid(column=2,row=0)
        lEmpNumber = tk.Label(f3, text="Emp. Contact No.: ",font=('Times New Roman',15)).grid(column=3,row=0)
        lAge = tk.Label(f3, text="Emp. Age: ",font=('Times New Roman',15)).grid(column=4,row=0)
        lEmpGender = tk.Label(f3, text="Emp. Gender: ",font=('Times New Roman',15)).grid(column=5,row=0)
        lHireDate = tk.Label(f3, text="Date Of Hiring: ",font=('Times New Roman',15)).grid(column=6,row=0)

        
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select EmpID,EmpName, EmpMail, EmpNumber, Age, EmpGender, HireDate from employee")
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
        lEmpID = tk.Label(f4, text="Emp. ID: ",font=('times new roman',15)).grid(column=0,row=3)
        EmpID = tk.IntVar()
        tEmpID = tk.Entry(f4,font=('times new roman',15), width=30, textvariable=EmpID)
        tEmpID.grid(column=2, row=3)
        
        lEmpPass = tk.Label(f4, text="Emp. Pass.: ",font=('times new roman',15)).grid(column=4,row=3)
        EmpPass = tk.StringVar() 
        tEmpPass = tk.Entry(f4,font=('times new roman',15), width=30, textvariable=EmpPass) 
        tEmpPass.grid(column=6, row=3)
        

        def submit2() :

            lEmpID = tk.Label(f5, text="Emp. ID: ",font=('Times New Roman',15)).grid(column=0,row=0)
            lEmpName = tk.Label(f5, text="Emp. Name: ",font=('Times New Roman',15)).grid(column=1,row=0)
            lEmpMail = tk.Label(f5, text="Emp. Mail ID: ",font=('Times New Roman',15)).grid(column=2,row=0)
            lEmpNumber = tk.Label(f5, text="Emp. Contact No.: ",font=('Times New Roman',15)).grid(column=3,row=0)
            lAge = tk.Label(f5, text="Emp. Age: ",font=('Times New Roman',15)).grid(column=4,row=0)
            lEmpGender = tk.Label(f5, text="Emp. Gender: ",font=('Times New Roman',15)).grid(column=5,row=0)
            lHireDate = tk.Label(f5, text="Date Of Hiring: ",font=('Times New Roman',15)).grid(column=6,row=0)

            
            conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='root',charset='utf8')
            cursor = conn.cursor()
            cursor.execute("select EmpID,EmpName, EmpMail, EmpNumber, Age, EmpGender, HireDate from employee where EmpID = '" +str(EmpID.get())+ "' and EmpPass='"+str(EmpPass.get())+"'" )
            ls = pd.DataFrame(cursor.fetchall())
  
            for i in range(0, len(ls.index)):
                for j in range(0, len(ls.columns)):
                    b = tk.Entry(f5)
                    b.insert(1, ls.iloc[i][j])
                    b.grid(row=1, column=j,padx=10,pady=10)
                    b.config(state = "readonly")

            conn.commit()
            

        sub2= tk.Button(f4, font = ('times new roman', 12), text='Submit', command=submit2)
        sub2.grid(column=7, row=3)   

def Emp():
    
    import Emp_menu
    win4.destroy()

#Back to Menu
back=tk.Button(f6, font=('times new roman',16), text="Emp. Menu",command=Emp)
back.grid(column=4, row=15,columnspan=1)

#------------------------------------------------------    
sub= tk.Button(f1, font = ('times new roman', 12), text='Submit', command=submit)
sub.grid(column=3, row=0)


tk.mainloop()














