import pymysql.cursors


connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='addressbook',
                             )

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()

