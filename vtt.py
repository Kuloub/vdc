import mysql.connector

mydb = mysql.connector.connect(
  host="localllhoouu88s",
  user="myuser4",
  password="myasd",
  database="mydataase"
    user="myusernam214e",
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
