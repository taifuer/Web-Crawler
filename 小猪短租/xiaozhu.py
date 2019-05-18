# -*- coding:utf-8 -*-
"""
@name:   xiaozhu.py
@time:   2019 / 05 / 06
@author: taifu
"""


import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# 代理
proxies = {
    'http': 'http://119.101.113.153:9999'
}


# 替换文件名中可能的非法字符
def validateName(name):
    pattern = r"[\/\\\:\*\?\"\<\>\|]"
    newName = re.sub(pattern, '_', name)
    return newName

# 保存房间图片
def saveHouseImage(url, name):
    image = requests.get(url, headers=headers)
    path = 'xiaozhuImage/'
    if not os.path.exists(path):
        os.makedirs(path)
    name = validateName(name)
    with open(path + name + '.png', 'wb') as f:
        f.write(image.content)

# 写入文件
def writeToFile(content):
    with open('xiaozhu.txt', 'a+', encoding='utf-8') as f:
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
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find(class_='pho_info')
    # 标题
    title = div.h4.em.string
    # 地址
    address = div.p.span.string
    # 价格
    price = soup.find(class_='detail_avgprice').string
    # 图片
    imageUrl = soup.find(id='curBigImage')['src']
    # 房主昵称
    name = soup.find(class_='lorder_name').string

    info = {
        'title': title,
        'address': address.strip(),
        'price': price.strip(),
        'imageUrl': imageUrl,
        'name': name
    }

    saveHouseImage(imageUrl, title)

    return info

# 获取多个链接
urls = ['http://cs.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 10)]

if __name__ == '__main__':
    for url in urls:
        html = getOnePage(url)
        soup = BeautifulSoup(html, 'lxml')
        houseUrls = soup.find_all(class_='resule_img_a')
        for houseUrl in houseUrls:
            housePage = getOnePage(houseUrl['href'])
            houseInfo = parseOnePage(housePage)
            print(houseInfo)
            time.sleep(0.05)
            writeToFile(houseInfo)