import mysql.connector
import os

COMMIT = os.getenv('GIT_COMMIT')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bidalgo",
  database="mysql"
)

mycursor = mydb.cursor()

sql = "INSERT INTO commits (commit_id, commit_time, commit_message, commit_user) VALUES (%s, %s, %s, %s)"
val = (COMMIT, "2", "3", "4")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
