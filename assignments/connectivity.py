import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shirish@24",
  database="library"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
