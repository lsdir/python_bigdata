import requests
from urllib import parse
import json

# 搜索关键字
wd = '罗志祥'
# 爬取的页数
page_num = 10

# 对中文进行编码
wd_url_encode = parse.quote(wd)

# 爬取网站地址
url = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D60%26q%3D$1%26t%3D0&page_type=searchall&page=$2"

# 替换搜索关键字
url = url.replace('$1', wd_url_encode)

for i in range(page_num):
    # 替换页数关键字
    url = url.replace("$2", str(i))

    print(i)
    # 发起request请求
    text = requests.get(url)
    # 将字符串转化为json对象
    js = json.loads(text.text)

    # 取数据
    cards = js['data']['cards']
    for card in cards:
        mblog = card["mblog"]
        # 用户id
        id = mblog["id"]
        # 内容
        text = mblog["text"]
        # 用户信息
        user = mblog["user"]
        # 转发数量
        reposts_count = mblog["reposts_count"]
        # 评论数量
        comments_count = mblog["comments_count"]
        # 点赞数量
        attitudes_count = mblog["attitudes_count"]
        # 用户名
        screen_name = user["screen_name"]
        # 关注数
        follow_count = user["follow_count"]
        # 粉丝数
        followers_count = user["followers_count"]
        # 性别
        gender = user["gender"]

        # 字符创拼接
        line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
            id, reposts_count, comments_count, attitudes_count, screen_name, gender, follow_count, followers_count,
            text)

        print(line)
