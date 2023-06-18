from tkinter import *

top= Tk()
#def test():
#    print("hello")
pic= PhotoImage(master=top,file="BackgroundBL.png")
pic_label = Label(top,image=pic).grid(column=0,row=0,columnspan=10, rowspan=10)
Name = Label(top,text="Name").grid(row=0,column=0)
e1 = Entry(top).grid(row=0,column=1)
address = Label(top,text="address").grid(row=1,column=0)
e2 = Entry(top).grid(row=1,column=1)
btn = Button(top,text="Save").grid(row=2,column=0)
top.mainloop()
