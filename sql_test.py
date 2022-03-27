import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sh@unak10",
  database="cqap"
)
mycursor = mydb.cursor()
sql = "INSERT INTO users (name,username,pwd,cpwd,gender,contact_no,email,age,address,pricon1_name,pricon1_email,pricon2_name,pricon2_email,pricon3_name,pricon3_email,med_disorder,bld_grp,algy,treat_speci) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)"
val = ('n1','n2','n3','n4','1','n6','n7','65','n9','1','1','1','1','1','1','1','1','1','n20')
mycursor.execute(sql, val)
mydb.commit()
