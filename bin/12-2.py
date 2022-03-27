import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("select age, avg(fee) from Student group by age")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
