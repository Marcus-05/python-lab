import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="wordpress")

cursor = conn.cursor()

selectquery = "SELECT * FROM wp_users"
cursor.execute(selectquery)

records = cursor.fetchall()
print(records)
print("Musheer is the best coder in the world and one day he")