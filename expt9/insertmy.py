import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="cricketers-db"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO `cricketers` (`id`, `name`) VALUES (NULL, 'MusheerAhmed2')"
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

selectquery = "SELECT * FROM cricketers"
mycursor.execute(selectquery)
records = mycursor.fetchall()
print(records)