import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='xodls72003270', db='menuDB', charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE menuTable (menuCode int(4), menuName char(15))")

