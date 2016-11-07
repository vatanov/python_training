import pymysql.cursors

connecion = pymysql.connect(host="127.0.0.1", database = "addressbook", user="root", password="")

try:
    cursor = connecion.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connecion.close()