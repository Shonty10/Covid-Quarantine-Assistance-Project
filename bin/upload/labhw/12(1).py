import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("select student_name from Student where age>23 order by student_name DESC")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
