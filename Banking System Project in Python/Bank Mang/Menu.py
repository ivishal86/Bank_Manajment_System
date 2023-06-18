

from tkinter import *



#Menu Window
win = Tk()
win.title("Main Window")

pic= PhotoImage(master=win,file="BackgroundBL.png")
pic_label = Label(win,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)

def cust():
    win.destroy()
    import Cust_menu
    
    
    

def emp():
    win.destroy()
    import Elogin_gui
        

Cust = Button(win,font=('arial',12), text="Customer Menu", height =3, width = 13, command=cust)
Cust.grid(column=3, row=7)

Emp = Button(win,font=('arial',12), text="Employee Menu",height =3, width = 13, command=emp)
Emp.grid(column=5, row=7,columnspan=2)


