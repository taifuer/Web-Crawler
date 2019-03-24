# -*- coding:utf-8 -*-
"""
@name:   main.py
@time:   2019 / 03 / 24
@author: taifu
"""

import json
import requests
from requests.exceptions import RequestException
import re

# 获取网页源文件
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 单页解析
def parse_one_page(html):
    pattern = re.compile('<div.*?item">.*?<em.*?>(\d+)</em>.*?<img.*?src="(.*?)".*?>.*?info">.*?<span.*?title">(.*?)</span>.*?<p class="">(.*?)<br>(.*?)</p>.*?'\
          + 'average">(.*?)</span>.*?<span>(.*?)</span>.*?quote">.*?inq">(.*?)</span>', re.S)
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip().replace('&nbsp;', ' '),
            'type': item[4].strip().replace('&nbsp;', ' '),
            'score': item[5],
            'comment': item[6],
            'quote': item[7]
        }

# 保存到文件
def write_to_file(content):
    with open('douban.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

# 爬取
def crawl(offset):
    url = 'https://movie.douban.com/top250?start=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

# 入口
if __name__ == '__main__':
    for i in range(10):  # 总页数
        crawl(i*25)  # 每页数量