import ysql.cnector

mydb = ml.e.nt(
  host="",
  user="my",
  passwordmys",
  database="mda"
    user="myusra4e",
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#If this page was executed with no error(s), you have successfully deleted the "customers" table.
