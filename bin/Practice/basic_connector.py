import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sh@unak10"
  #database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("CREATE TABLE students (id INT PRIMARY KEY, student_name VARCHAR(255), gender VARCHAR(255), age int, city varchar(50), fee int, phone int)")

'''sql = "INSERT INTO students (id, student_name, gender, age, city, fee, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
  ('P1', 'Sameer', 'M', 34, 'Delhi', 45000, 9811076656),
  ('P2', 'Aryan', 'M', 35, 'Mumbai', 54000, 9911343989),
  ('P4', 'Ram', "M", 34, 'Chennai', 45000, 9810593578)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
mycursor.execute("select * from students")'''

#mycursor.execute("select student_name from Student where age>23 order by student_name DESC")
#join-------> "select description from dress, material where dress.mcode=material.mcode and material.type='cotton'"

'''myresult=mycursor.fetchall()
for i in myresult:
    print(i)'''
