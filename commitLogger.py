import mysql.connector
import os

COMMIT = os.getenv('GIT_COMMIT')
# USER = os.system('git log -1 | grep Author | cut -d " " -f2')
USER = subprocess.check_output('git log -1 | grep Author | cut -d " " -f2', shell=True)

print(USER)

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
val = (COMMIT, "2", "3", USER)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
