import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bidalgo",
  database="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE commits (commit_id VARCHAR(255), commit_time VARCHAR(255), commit_message VARCHAR(255), commit_user VARCHAR(255))")
