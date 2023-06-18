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


#Login Window
win2 = tk.Tk()
win2.title("Employee Menu")

#---------adding Bg Image---------------

pic2=PhotoImage(master=win2,file='Bg Menu ImageBL.png')
pic2_label=Label(win2, image= pic2).grid(column=0,row=0,columnspan=5, rowspan=10)



def New():
    win2.destroy()
    import new_emp

def Search():
    win2.destroy()
    import show_emp

def Delete():
    win2.destroy()
    import delete_emp
    
def Update():
    win2.destroy()
    import update_emp

def Back():
    
    import Menu
    win2.destroy()
    
#-----------adding buttons---------------

#Create Acc
new=tk.Button(win2,font=('times new roman',18), text="Hire Employee",width = 17 ,command=New)
new.grid(column=1, row=5,columnspan=1)

#Search
search=tk.Button(win2,font=('times new roman',18), text="Employee Details",width = 17,command=Search)
search.grid(column=3, row=5,columnspan=1)

#Update
update=tk.Button(win2,font=('times new roman',18), text="Update Employee",width = 17,command=Update)
update.grid(column=1, row=6,columnspan=1)

#Delete
delete=tk.Button(win2,font=('times new roman',18), text="Fire Employee",width = 17,command=Delete)
delete.grid(column=3, row=6,columnspan=1)

#Back to Menu
back=tk.Button(win2,font=('times new roman',16), text="Back to Menu",command=Back)
back.grid(column=2, row=8,columnspan=1)



