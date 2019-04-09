import pandas as pd
import numpy as np

from DB import getConn
from dataClean import clean

conn = getConn()
cursor = conn.cursor()

def saveToDB(row):
    level, movie_id, movie_name, username, user_id , img_url = row["rate"] , row["movie_url"] , row["movie_name"] , row["user_name"] , row["user_id"] , row["movie_url"]
    movie_name = movie_name.replace("'" , ' ')
    sql = "INSERT into user_comment ( level, movie_id ,movie_name, username, user_id , img_url) VALUES ( '%s', '%s', '%s', '%s', '%s' , '%s')" % (
            str(level), str(movie_id), str(movie_name), str(username), str(user_id) , str(img_url))
    print(sql)
    cursor.execute(sql.encode("utf-8"))

data = clean()


for name , group in data.groupby("user_id"):
    df = pd.DataFrame(group.drop_duplicates("movie_name"))
    df = df.loc[:,['rate' , 'movie_url' , 'movie_name' , 'user_name' , 'user_id' , 'movie_url']]
    print(df.columns)
    df.apply(saveToDB ,axis = 1)
    conn.commit()