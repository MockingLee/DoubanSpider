import pandas as pd
import numpy as np

from DB import getConn
from dataClean import clean

conn = getConn()
cursor = conn.cursor()

def saveToDB(row):
    #print(row)
    level, movie_url, movie_name, username, user_id , img_url , type = row["rate"] , row["movie_url"] , row["movie_name"] , row["user_name"] , row["user_id"] , row["movie_img"] , row['type']
    movie_name = movie_name.replace("'" , ' ')
    #print(movie_url)
    #print(str(level), str(movie_url), str(movie_name), str(username), str(user_id) , str(img_url) , str(type))
    sql = "INSERT into user_comment ( level, movie_url ,movie_name, username, user_id , img_url , type) VALUES ( '%s', '%s', '%s', '%s', '%s' , '%s' ,'%s')" % (
            str(level), str(movie_url), str(movie_name), str(username), str(user_id) , str(img_url) , str(type))
    print(sql)
    cursor.execute(sql.encode("utf-8"))


# print(data)

def durability(file):
    data = clean(file)
    for name, group in data.groupby("user_id"):
        df = pd.DataFrame(group.drop_duplicates("movie_name"))
        df = df.loc[:, ['rate', 'movie_url', 'movie_name', 'user_name', 'user_id', 'movie_img', 'type']]
        print(df.columns)
        # print(df.columns)
        df.apply(saveToDB, axis=1)
        conn.commit()