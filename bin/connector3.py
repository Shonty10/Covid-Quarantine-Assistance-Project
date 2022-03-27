import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT Name, Average FROM Graduate1 WHERE Average= (SELECT Max(Average) FROM Graduate1) or Average=(SELECT Min(average) from Graduate1)")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
