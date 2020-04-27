import requests

url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E7%BD%97%E5%BF%97%E7%A5%A5&page_type=searchall'
html = requests.get(url)
print(html.text)