import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vishal"
)

mycursor = mydb.cursor()

mycursor.execute("select * from gwala")
result= mycursor.fetchone()

print(result)
