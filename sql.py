import pymysql
import datetime

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456100',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def insertPageIfNotExists(url):
    #如果关键词还没抓取就存进数据库
    with connection.cursor() as cur:
        sql = "SELECT * FROM pages WHERE url = %s"
        cur.execute(sql, (url))
        if cur.rowcount == 0:
            sql = "INSERT INTO pages (url) VALUES (%s)"
            cur.execute(sql, (url))
            connection.commit()
            print(cur.lastrowid)
            return cur.lastrowid
        else:
            return cur.fetchone()['id']


def insertLink(fromPageId, toPageId):
    #存入对应的来源词
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
                                                    (int(fromPageId), int(toPageId)))
        if cur.rowcount == 0:
            cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
                                                    (int(fromPageId), int(toPageId)))
            connection.commit()
