import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT Name from Graduate1 where Name like 'r%'")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
