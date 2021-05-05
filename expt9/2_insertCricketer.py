#MusheerAhmed 1910053
import mysql.connector


def insert(lhost, ldatabase, table):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    cursor = connection.cursor()
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return

    cricketers = [
        ('Mahendra Singh','Dhoni','7 July 1981', 'Ranchi', 'India'),
        ('Virat', 'kohli', '5 November 1988', 'New Delhi', 'India'),
        ('Rohit', 'Sharma', '30 April 1987', 'Nagpur', 'India'),
        ('Abraham', 'Benjamin', '17 February 1984', 'Bela-Bela', 'South Africa'),
        ('Joe', 'Root', '30 December 1990', 'Dore', 'England'),
    ]
    sqlinsert = f"INSERT INTO {table} (First_name,Last_name,Date_of_Birth,Place_of_Birth,Country) values(%s,%s,%s,%s,%s)"
    cursor.executemany(sqlinsert, cricketers)
    connection.commit()

def show(lhost, ldatabase, table):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM `{table}`")
    for x in cursor:
        print(x)


if __name__ == '__main__':
    insert("localhost", "cricketers-db", "cricketers")
    show("localhost", "cricketers-db", "cricketers")
