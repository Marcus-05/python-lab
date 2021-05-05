#MusheerAhmed 1910053
import mysql.connector


def update(lhost, ldatabase, table, country):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return
    cursor = connection.cursor()
    sql = f"UPDATE `{table}` SET Country = '{country}' WHERE Last_name = 'Dhoni' "
    cursor.execute(sql)
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
    print(cursor.fetchone())


if __name__ == '__main__':
    update("localhost", "cricketers-db", "cricketers", "UAE")
    show("localhost", "cricketers-db", "cricketers")
    update("localhost", "cricketers-db", "cricketers", "India")
    show("localhost", "cricketers-db", "cricketers")
