import mysql.connector
from  datetime import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shirish@24",
  database="library"
)
mycursor = mydb.cursor()
    # selcts date of issue and return
q1 = "SELECT date_of_issue, date_of_return FROM student WHERE stud_id = %s"
studid=3
stid = (studid,)
mycursor.execute(q1, stid)
dates = mycursor.fetchone()  # fetch only one record

d1, d2 = dates
dat1 = d1.strftime("%d")
dat2 = d2.strftime("%d")
int_dat1 = int(dat1)
int_dat2 = int(dat2)
# print(int_dat1)

diff = int_dat2 - int_dat1
print(diff)