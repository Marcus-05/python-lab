#MusheerAhmed 1910053
import mysql.connector

def create_table(lhost, ldatabase):
    connection = mysql.connector.connect(host=lhost, database=ldatabase)
    if (connection):
        print("Connection successful")
    else:
        print("Connection failed!!")
        return
    
    cursor = connection.cursor()
    createTableSql = """
     CREATE TABLE `cricketers-db`.`cricketers` ( `First_name` VARCHAR(200) NOT NULL ,
    `Last_name` VARCHAR(200) NOT NULL , 
    `Date_of_Birth` VARCHAR(200) NOT NULL , `Place_of_Birth` VARCHAR(200) NOT NULL ,
    `Country` VARCHAR(200) NOT NULL )
    """
    cursor.execute(createTableSql)


if __name__ == '__main__':
    create_table("localhost","cricketers-db")
