#MusheerAhmed 1910053
import mysql.connector


def getFirstNameCount(lhost, ldatabase, table):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    cursor = connection.cursor()
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return
    
    sql = f"SELECT `First_name`, `Country` FROM `{table}` WHERE 1"
    cursor.execute(sql)
    for x in cursor:
        print(x)


if __name__ == '__main__':
    getFirstNameCount("localhost", "cricketers-db","cricketers")