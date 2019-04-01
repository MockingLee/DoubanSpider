import pymysql

host = "db.pkmgtdz.xyz"
user = "dbuser"
pwd = "dbuser"
db_name = "DoubanData"
connection = pymysql.connect(host=host,
                             port=3306,
                             user=user,
                             password=pwd,
                             db=db_name,
                             charset='utf8')
