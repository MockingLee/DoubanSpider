# DoubanSpider
豆瓣电影爬虫 爬取top电影的评论 + 每个用户的看过的电影的评论  用于推荐系统的 协同过滤

## 用法 
python3 runSpider.py [用户观看page深度] [是否代理 0 or 1]

## API 
top250 https://api.douban.com/v2/movie/top250 作为root入口


## todo
- [x] data clearning
- [x] db?
- [x] data unique
- [x] root 
- [ ] 循环深度
