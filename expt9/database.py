from mysql_op import mysql


if __name__ == '__main__':
    myobj = mysql("localhost","cricketers-db","cricketers")
    myobj.print_details()
