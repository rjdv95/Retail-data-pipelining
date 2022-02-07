import psycopg2


try:
    connection = psycopg2.connect("dbname='retail_dw' user='retail_user' host='34.116.128.233' password='eduhilfe'")
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM t1""")

    rows = cursor.fetchone()
except:
    print("\nrows: \n")
