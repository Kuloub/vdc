import mysql.cnector

mydb = mql.er.nct(
  host="locts",
  user="mys",
  passwordmys",
  database="mda"
    user="myusra24e",
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
