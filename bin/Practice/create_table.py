import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE students (id INT PRIMARY KEY, student_name VARCHAR(255), gender VARCHAR(255), age int, city varchar(50), fee int, phone int)")
mycursor.execute("Show Tables")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
