import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vishal"
)

mycursor = mydb.cursor()
a=input("enter the name")
b=input("enter the Email address")
c=input("Enter the password")
d=input("Enter the mobile no.")
e=input("Enter gender:")

sql = "INSERT INTO bankm(name,Email address,password,mobile no.,gender) VALUES (%s, %s, %s, %s, %s)"
val = (a,b,c,d,e)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
