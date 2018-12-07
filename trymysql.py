import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="testpython"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name) VALUES ('Nafisa')"

mycursor.execute(sql)

mydb.commit()
print(test)
print(mycursor.rowcount, "record inserted.")