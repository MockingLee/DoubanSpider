from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import sys

proxies = { }

cookies = {"cookie" : 'll="108258"; bid=tLImqHU5tQw; _vwo_uuid_v2=DEA5F3ABC87B65A439B48A1380043F167|6cdef9469bc47f0af8df22af2dc87cee; __yadk_uid=3IKOiAMzeDwMbrcVfqzp4OlTyHYhvAPx; push_noty_num=0; push_doumail_num=0; __utmz=223695111.1553918932.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmz=30149280.1553921039.1.1.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject/25986662/comments; __utmv=30149280.19417; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553930608%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.2085295896.1553921039.1553926060.1553930608.3; __utmc=30149280; __utma=223695111.1660141469.1553147220.1553926060.1553930608.6; __utmb=223695111.0.10.1553930608; __utmc=223695111; ps=y; dbcl2="194172670:ZQnVJtVeP6Q"; ck=CDt6; __utmt=1; __utmb=30149280.7.10.1553930608; _pk_id.100001.4cf6=a3efd3f3a06d3d48.1553147219.5.1553933785.1553926060.'}
headers = {"User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# r = requests.get("https://www.douban.com/people/4621276/colletc", proxies=proxies, cookies=cookies, headers=headers)
# soup = BeautifulSoup(r.content)
# print(soup)

url = "https://movie.douban.com/chart"
all_comment_postfix = "comments?sort=new_score&status=P"
user_all_watched_postfix = "/collect?&sort=time"
user_all_watched_prefix = "https://movie.douban.com/people/"

r = requests.get(url ,proxies = proxies , cookies = cookies , headers = headers)
soup = BeautifulSoup(r.content)
movies = soup.find_all('a',class_='nbg')
#movies = movies[0:1]
movie_comments = []


col = ["user_id" , "user_name" , "movie_url" , "movie_img" , "rate" , "movie_name"]
count = 0
for i in movies:

    r = requests.get(i["href"] + all_comment_postfix , proxies = proxies , cookies = cookies , headers = headers)
    soup = BeautifulSoup(r.content)
    comments = soup.find_all('span',class_='comment-info')
    user_comments = []

    for c in comments :
        comment = {}
        print(c)
        if c.find("span" , class_="rating") != None:
            # comment["username"] = c.a.get_text()
            # comment["user_id"] = c.a["href"].split("/")[4]
            # comment["level"] = c.find("span" , class_="rating")["title"]
            print(c.a["href"].split("/")[4])
            print(c.a.get_text())
            print(i["href"])
            print(i.img["src"])
            print(c.find("span" , class_="rating")["title"])
            print(i["title"])
            comment = {"user_id":c.a["href"].split("/")[4] , "user_name" :c.a.get_text(), "movie_url" :i["href"], "movie_img" :i.img["src"], "rate":c.find("span" , class_="rating")["title"] , "movie_name":i["title"]}
            movie_comments.append(comment)
            count += 1
            print(count)
            for m in range(0,int(sys.argv[1])):
                r = requests.get(user_all_watched_prefix + comment["user_id"] + user_all_watched_postfix + "&start=" + str(m*15),
                                 proxies=proxies, cookies=cookies, headers=headers)
                soup = BeautifulSoup(r.content)
                u_w_movies = soup.find_all("div", class_="item")
                m = {}
                for u_w_movie in u_w_movies:
                    # print(u_w_movie.find_all("li")[2].span["class"][0])
                    # print(u_w_movie.find("a" , class_="nbg")["href"])
                    # print(u_w_movie.img)
                    user_watched_comment = {"user_id": comment["user_id"], "user_name": comment["user_name"],
                                            "movie_url": u_w_movie.find("a", class_="nbg")["href"],
                                            "movie_img": u_w_movie.img["src"],
                                            "rate": u_w_movie.find_all("li")[2].span["class"][0],
                                            "movie_name": u_w_movie.img["alt"]}
                    movie_comments.append(user_watched_comment)
                    count += 1
                    print(count)
        movie_comments.append(comment)

    #movie_comments.append({"movie_name" : i["title"] , "movie_url" : i["href"] , "movie_img" : i.img["src"] , "comments" : user_comments})

df = pd.DataFrame(movie_comments)
df.to_csv("data.csv" ,encoding='utf_8_sig')












