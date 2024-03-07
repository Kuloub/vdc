import mysql.cnector

mydb = mql.er.nect(
  host="loctaos",
  user="mys4",
  password="mys",
  database="myda"
    user="myusra24e",
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
