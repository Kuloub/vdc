import mysql.cnector

mydb = mql.oner.conect(
  host="locaos",
  user="myser4",
  password="mys",
  database="mydate"
    user="myusernam24e",
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
