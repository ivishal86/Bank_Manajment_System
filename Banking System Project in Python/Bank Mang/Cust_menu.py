import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import *



win2 = tk.Tk()
win2.title("Customer Menu")

#---------adding Bg Image---------------

pic2=PhotoImage(master=win2,file='Bg Menu ImageBL.png')
pic2_label=Label(win2, image= pic2).grid(column=0,row=0,columnspan=5, rowspan=10)



def New():
    win2.destroy()
    import create_acc

def Search():
    win2.destroy()
    import show_acc

def Dep():
    win2.destroy()
    import deposit_login

def Wd():
    win2.destroy()
    import withdraw_login

def Delete():
    win2.destroy()
    import delete_acc
    
def Update():
    win2.destroy()
    import update_acc

def Back():
    
    import Menu
    win2.destroy()
    
#-----------adding buttons---------------

#Create Acc
new=tk.Button(win2,font=('times new roman',18), text="Create New Account",width = 17 ,command=New)
new.grid(column=1, row=4,columnspan=1)

#Search
search=tk.Button(win2,font=('times new roman',18), text="Show Account",width = 17,command=Search)
search.grid(column=3, row=4,columnspan=1)

#Deposit
dep=tk.Button(win2,font=('times new roman',18), text="Deposit",width = 17,command=Dep)
dep.grid(column=1, row=5,columnspan=1)

#Withdraw
wd=tk.Button(win2,font=('times new roman',18), text="Withdraw",width = 17,command=Wd)
wd.grid(column=3, row=5,columnspan=1)

#Update
update=tk.Button(win2,font=('times new roman',18), text="Update Account",width = 17,command=Update)
update.grid(column=1, row=6,columnspan=1)

#Delete
delete=tk.Button(win2,font=('times new roman',18), text="Drop Account",width = 17,command=Delete)
delete.grid(column=3, row=6,columnspan=1)

#Back to Menu
back=tk.Button(win2,font=('times new roman',16), text="Back to Menu",command=Back)
back.grid(column=2, row=8,columnspan=1)



