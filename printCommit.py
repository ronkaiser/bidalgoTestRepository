import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="bidalgo",
  database="mysql"
)

mycursor = mydb.cursor()

sql="SELECT * FROM commits ORDER BY row_id DESC LIMIT 1"
mycursor.execute(sql)
last_id = mycursor.fetchone()
for lastID in last_id:
    print("The last commit detalis are: "lastID)

