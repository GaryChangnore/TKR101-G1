import pymysql


host = 'localhost'
port = 3306
user = 'root'
passwd = 'Gary1234!'
db = 'TESTDB'
charset = 'utf8mb4'


def get_conn():
    return pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

