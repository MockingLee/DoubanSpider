import pymysql

host = "tx.pkmgtdz.xyz"
user = "dbuser"
pwd = "dbuser"
db_name = "DoubanData"

def getConn():
    connection = pymysql.connect(host=host,
                                 port=3306,
                                 user=user,
                                 password=pwd,
                                 db=db_name,
                                 charset='utf8')
    return connection






