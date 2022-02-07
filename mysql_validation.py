import mysql.connector as mc
from mysql.connector import errorcode as ec

user = "retail_user"
password = "eduhilfe"
host = "34.116.128.233"
db = "retail_db"

try:
    connection = mc.connect(user=user,
                          password=password,
                          host=host,
                          database=db
                         )
    orders_cursor = connection.cursor()
    query = """SELECT * FROM orders LIMIT 10"""
    orders_cursor.execute(query)
    for order in orders_cursor:
        print(order)
except mc.Error as error:
    if error.errno == ec.ER_ACCESS_DENIED_ERROR:
        print("Invalid Credentials")
    else:
        print('err')
else:
    connection.close()