import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("select Name from graduate1 order by Name")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
