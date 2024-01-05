import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypasswosrd",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql2)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
