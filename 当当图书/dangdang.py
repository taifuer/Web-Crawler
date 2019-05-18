# -*- coding:utf-8 -*-
"""
@name:   dangdang.py
@time:   2019 / 05 / 08
@author: taifu
"""

import requests
from pyquery import PyQuery as pq
import json
import os
import re
import time

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# 替换文件名中可能的非法字符
def validateName(name):
    pattern = r"[\/\\\:\*\?\"\<\>\|]"
    newName = re.sub(pattern, '_', name)
    return newName

# 保存书籍图片
def saveImage(url, name):
    image = requests.get(url, headers=headers)
    path = 'dangdangImage/'
    if not os.path.exists(path):
        os.makedirs(path)
    name = validateName(name)
    with open(path + name + '.png', 'wb') as f:
        f.write(image.content)

# 写入文件
def writeToFile(content):
    with open('dangdang.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 得到页面源码
def getOnePage(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except Exception:
        return None

# 获取指定内容
def parseOnePage(html):
    doc = pq(html)
    ul = doc('.bigimg')
    liList = ul('li')
    for li in liList.items():
        a = li('a:first-child')
        # 图书主页URL
        href = a[0].get('href')
        # 图片
        image = a('img').attr('data-original')
        if image is None:
            image = a('img').attr('src')
        # 标题
        title = a[0].get('title')
        # 价格
        span = li('.search_now_price')
        price = span[0].text[1:]
        # 信息
        p = li('.search_book_author')
        # 作者
        author = p('a:first-child').attr('title')
        # 出版日期
        date = p('span:nth-child(2)').text()[1:]
        # 出版社
        publisher = p('span:nth-child(3) > a').text()
        # 评论数
        comment = li('.search_comment_num').text()[:-3]
        # 简介
        detail = li('.detail').text()

        saveImage(image, title)

        yield {
            'title': title,
            'href': href,
            'image': image,
            'price': price,
            'author': author,
            'date': date,
            'publisher': publisher,
            'comment': comment,
            'detail': detail
        }

# 获取多个链接
urls = ['http://search.dangdang.com/?key=python&act=input&page_index={}'.format(str(i)) for i in range(1, 4)]

# 入口
if __name__ == '__main__':
    for url in urls:
        html = getOnePage(url)
        for item in parseOnePage(html):
            print(item)
            time.sleep(0.05)
            writeToFile(item)