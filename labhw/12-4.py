import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("select Min(age), Max(age) from Student")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
