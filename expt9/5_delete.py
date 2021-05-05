#MusheerAhmed 1910053
import mysql.connector


def delete(lhost, ldatabase, table, firstname):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return
    cursor = connection.cursor()
    sql = f"DELETE FROM `{table}` WHERE First_name = '{firstname}' "
    cursor.execute(sql)
    connection.commit()
    print("Deleted Successfully")


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
    show("localhost", "cricketers-db", "cricketers")
    delete("localhost", "cricketers-db", "cricketers", "Rohit")
    show("localhost", "cricketers-db", "cricketers")
