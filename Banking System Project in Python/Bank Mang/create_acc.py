import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from tkinter import *


win3 = tk.Tk()
win3.title("Details Window")

#---------adding Bg Image---------------

pic3=PhotoImage(master=win3,file='BackgroundBlurBL.png')
pic3_label=Label(win3, image= pic3).grid(column=0,row=0,columnspan=5, rowspan=10)


#----------Adding Fields---------------
#Cust Id
cId = tk.IntVar()
tcId = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=cId)
tcId.grid(column=2, row=5,columnspan=3)

#Cust. Name
lcname = tk.Label(win3, text="Cust. Name : ")
lcname.grid(column=0, row=1,columnspan=2)
lcname.configure(font=('Times New Roman',15),width=20)

cname = tk.StringVar()
tcname = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=cname)
tcname.grid(column=2, row=1,columnspan=3)

#Mail Id
lcmail = tk.Label(win3, text="Cust. Mail Id : ") 		
lcmail.grid(column=0, row=2,columnspan=2)
lcmail.configure(font=('Times New Roman',16),width=20)

cmail = tk.StringVar() 
tcmail = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=cmail) 
tcmail.grid(column=2, row=2,columnspan=3)

#Pass
lcpass = tk.Label(win3, text="Cust. Password : ") 		
lcpass.grid(column=0, row=3,columnspan=2)
lcpass.configure(font=('Times New Roman',16),width=20)

cpass = tk.StringVar() 
tcpass = tk.Entry(win3,font=('arial',15), width=28, textvariable=cpass) 
tcpass.grid(column=2, row=3,columnspan=3)

#ContactNo
lcNo = tk.Label(win3, text="Cust. Contact No. : ") 		
lcNo.grid(column=0, row=4,columnspan=2)
lcNo.configure(font=('Times New Roman',16),width=20)

cNo = tk.IntVar() 
tcNo = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=cNo) 
tcNo.grid(column=2, row=4,columnspan=3)

#Cust. Age
lcAge = tk.Label(win3, text="Cust. Age : ") 		
lcAge.grid(column=0, row=5,columnspan=2)
lcAge.configure(font=('Times New Roman',16),width=20)

cAge = tk.IntVar() 
tcAge = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=cAge) 
tcAge.grid(column=2, row=5,columnspan=3)

#Amount
lamount = tk.Label(win3, text="Opening Amount : ") 		
lamount.grid(column=0, row=6,columnspan=2)
lamount.configure(font=('Times New Roman',16),width=20)

amount = tk.IntVar() 
tamount = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=amount) 
tamount.grid(column=2, row=6,columnspan=3)

#Gender
lcgender = tk.Label(win3, text="Gender : ") 		
lcgender.grid(column=0, row=7,columnspan=2)
lcgender.configure(font=('Times New Roman',16),width=20)

cgender = tk.StringVar() 
tcgender = ttk.Combobox(win3,font=('Times New Roman',15), width=29, textvariable=cgender,state='readonly') 
tcgender['values']=('M','F','O')
tcgender.grid(column=2, row=7,columnspan=3)

#Date of creation
lDOC = tk.Label(win3, text="Date Of Creation : ") 		
lDOC.grid(column=0, row=8,columnspan=2)
lDOC.configure(font=('Times New Roman',16),width=20)

DOC = tk.StringVar() 
tDOC = tk.Entry(win3,font=('Times New Roman',15), width=30, textvariable=DOC,bd=4) 
tDOC.grid(column=2, row=8,columnspan=3)


#-----------Commands-----------------

#Current Date command
        
def Cdate():
    try:
     
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='',charset='utf8')
        cursor2 = conn.cursor()
        cursor2.execute("select curdate()")
        ls = pd.DataFrame(cursor2.fetchall())
        if(len(ls.index)>0):
            DOC.set(ls.iloc[0][0])
            
            
        else:
            mBox.showinfo('!....IIIISH....!', 'Not Found')
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


#Insert Command
def insert(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='bank_mang',user='root',password='',charset='utf8') 
        cursor = conn.cursor()
        
        name = cname.get() 
        mail = cmail.get() 
        Cpass = cpass.get() 
        No = cNo.get()
        Age = cAge.get() 
        Amount = amount.get() 
        gender = cgender.get() 
        doc = DOC.get()

        if No > 999999999  :

            cursor.execute("insert into cust_table ( cname, cmail, cpass, cNo, cAge, Amount, cgender, date_of_creation) values('" +str(name)+ "','" +str(mail)+"','" +str(Cpass)+"','" +str(No)+"','" +str(Age)+"','" +str(Amount)+"','" +str(gender)+"','"+str(doc)+"')")

            cursor1 = conn.cursor()
            cursor1.execute("select cId from cust_table where cNo = '" +str(cNo.get())+ "'")
            ls = pd.DataFrame(cursor1.fetchall())
            if(len(ls.index)>0):
                cId.set(ls.iloc[0][0])
            CID= ('Your Cust. ID is :', cId.get())
            if(cursor.rowcount>0): 
                mBox.showinfo('Thank You',CID) 
                cname.set('')
                cmail.set('')
                cpass.set('')
                cNo.set('')
                cAge.set('')
                amount.set('')
                cgender.set('')
                DOC.set('')
                #win3.destroy()
                #import Cust_menu
            else: 
                 mBox.showerror('Warning!', 'Not Found')
                 mBox.configure(backcolor='pink')
            
        else:
            mBox.showerror('Warning!', 'Incorrect Phone No.')
        conn.commit()    
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")
         
def Back():
    win3.destroy()
    import Cust_menu



#------Buttons-------------

#Insert
insert=tk.Button(win3,font=('arial',16), text="Insert Details" ,command=insert) 
insert.grid(column=2, row=9,columnspan=1)

#Today's Date
Cdate = tk.Button(win3, text="Today's Date", command=Cdate) 
Cdate.grid(column=4, row=8,columnspan=3)


#Back to Menu
back=tk.Button(win3,font=('Times New Roman',12), text="Back to Cust Menu",command=Back)
back.grid(column=3, row=9,columnspan=1)








