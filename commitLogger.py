import mysql.connector
import os
import subprocess

COMMIT = os.getenv('GIT_COMMIT')
TIME = subprocess.check_output('git show -s --format=%ci', shell=True)
MESSAGE = subprocess.check_output('git log --format=%B -n 1', shell=True)
USER = subprocess.check_output('git log -1 | grep Author | cut -d " " -f2', shell=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bidalgo",
  database="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS commits (
			row_id int NOT NULL AUTO_INCREMENT,
			commit_id VARCHAR(255), 
			commit_time VARCHAR(255), 
			commit_message VARCHAR(255), 
			commit_user VARCHAR(255),
			PRIMARY KEY(row_id))""")

sql = "INSERT INTO commits (commit_id, commit_time, commit_message, commit_user) VALUES (%s, %s, %s, %s)"
val = (COMMIT, TIME, MESSAGE, USER)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
