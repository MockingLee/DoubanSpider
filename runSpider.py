from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import sys
import json
proxies = { "http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"}
cookies = {"cookie" : 'll="108169"; bid=oZmoV6qdLgs; __utmz=223695111.1545290180.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D059569B475A561078AFA35211FB7F553|dd6700d0a1bc188cc6edac51e819b21f; gr_user_id=9db93a63-8b75-444c-83ab-9eb2bd3899b2; __utmz=30149280.1554166742.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); viewed="30270959_27087503"; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554769995%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.470385602.1545290172.1554360208.1554769996.6; __utma=223695111.201513709.1545290180.1554360208.1554769996.4; __utmb=223695111.0.10.1554769996; ap_v=0,6.0; ps=y; __utmt=1; __utmb=30149280.2.9.1554770755601; dbcl2="194172670:/Uz7zGB7w24"; ck=hS0z; _pk_id.100001.4cf6=b472344ab7bd70d6.1545290180.4.1554770775.1554360218.; push_noty_num=0; push_doumail_num=0'}
#cookies = {"cookie" : 'll="108169"; bid=oZmoV6qdLgs; __utmz=223695111.1545290180.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D059569B475A561078AFA35211FB7F553|dd6700d0a1bc188cc6edac51e819b21f; gr_user_id=9db93a63-8b75-444c-83ab-9eb2bd3899b2; __utmz=30149280.1554166742.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); viewed="30270959_27087503"; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554769995%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.470385602.1545290172.1554360208.1554769996.6; __utmb=30149280.0.10.1554769996; __utma=223695111.201513709.1545290180.1554360208.1554769996.4; __utmb=223695111.0.10.1554769996; ap_v=0,6.0; _pk_id.100001.4cf6=b472344ab7bd70d6.1545290180.4.1554770415.1554360218.'}
headers = {"User-Agent" :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# r = requests.get("https://www.douban.com/people/4621276/colletc", proxies=proxies, cookies=cookies, headers=headers)
# soup = BeautifulSoup(r.content)
# print(soup)

url = "https://movie.douban.com/chart"
all_comment_postfix = "comments?sort=new_score&status=P"
user_all_watched_postfix = "/collect?&sort=time"
user_all_watched_prefix = "https://movie.douban.com/people/"
# movie_type = ["剧情" , "喜剧" , "动作" , "爱情" , "科幻" , "动画" , "悬疑" , "惊悚" , "恐怖" , "犯罪" , "同性" , "音乐" , "歌舞" , "传记" , "历史" , "战争" , "西部" , "奇幻" , "冒险" , "灾难" , "武侠" , "情色" ]
#
# #movie_type = ["剧情" , "喜剧", "动作", "爱情" ,"科幻", "动画", "悬疑", "惊悚", "恐怖", "纪录片" ,"短片", "情色", "同性", "音乐", "歌舞", "家庭" , "传记", "历史" ,"战争" ,"犯罪", "西部", "奇幻" ,"冒险", "灾难", "武侠", "古装" ,"运动", "黑色电影"]
# movie_type_rank_prefix = "https://movie.douban.com/tag/#/?sort=U&range=0,10&tags="
# for type in movie_type:
#     r = requests.get(movie_type_rank_prefix + type, proxies=proxies, cookies=cookies, headers=headers)
#     soup = BeautifulSoup(r.content)
#     print(soup)
#     print(soup.find_all('div',class_='info'))

api_url = 'http://api.douban.com/v2/movie/top250?&start=0&count=250&apikey=0df993c66c0c636e29ecbb5344252a4a'
str = requests.get(api_url).content
j = json.loads(str)
movies = []
for i in j["subjects"]:
    movies.append(i['alt'])
# r = requests.get(url ,proxies = proxies , cookies = cookies , headers = headers)
# soup = BeautifulSoup(r.content)
# movies = soup.find_all('a',class_='nbg')
# #movies = movies[0:1]
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












