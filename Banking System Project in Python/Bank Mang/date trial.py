
import tkinter as tk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox as mBox

win=tk.Tk()
win.title('trial')
win.geometry('500x500')


date=tk.Label(win, text=" Date Of Creation : ")
date.grid(column=0, row=0)

D = tk.StringVar()
tD = tk.Entry(win, width=50, textvariable=D)
tD.grid(column=1, row=0)

def _fill():
    try:
     
        conn = mysql.connector.connect(host='localhost',database='A',user='root',password='start',charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select curdate()")
        ls = pd.DataFrame(cursor.fetchall())
        if(len(ls.index)>0):
            D.set(ls.iloc[0][0])
            
            
        else:
            mBox.showinfo('!....IIIISH....!', 'Not Found')
    except Error as e :
        print("Error while connecting to MySQL", e)
    finally:
        print("MySQL connection is closed")


def clickMe(): 				
    try: 
        conn = mysql.connector.connect(host='localhost',database='A',user='root',password='start',charset='utf8') 
        cursor = conn.cursor()  
        Date = D.get() 
        

        cursor.execute("insert into Dates values('"+str(Date)+"')")

        if(cursor.rowcount>0): 
             mBox.showinfo('Congrats', 'Done!')
             D.set('')
             
        else: 
             mBox.showinfo('Warning!', 'Not Found')
             mBox.configure(backcolor='pink')
        conn.commit()
    except Error as e : 
        print("Error while connecting to MySQL", e) 
    finally: 
        print("MySQL connection is closed")


Id = tk.Button(win,font=('arial',16), text="Insert Dates!", command=clickMe) 
Id.grid(column=1, row=10)
Cdate = tk.Button(win, text="Today's Date", command=_fill) 
Cdate.grid(column=2, row=0)



