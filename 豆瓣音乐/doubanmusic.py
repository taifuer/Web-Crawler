# -*- coding:utf-8 -*-
"""
@name:   doubanmusic.py
@time:   2019 / 05 / 10
@author: taifu
"""

# -*- coding:utf-8 -*-

"""
@name:   main.py
@time:   2019 / 05 / 02
@author: taifu
"""

import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import os
import sqlite3

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

# 保存到文件
def write2File(filename, info):
    with open(filename, 'a+', encoding='utf-8') as f:
        f.write(json.dumps(info, ensure_ascii=False) + '\n')
# 保存为CSV
def save2CSV(filename, info):
    with open(filename, 'a+', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'author', 'style', 'time', 'score', 'comment', 'image']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(info)
# 保存到数据库
def save2DB(dbname, info):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    music = (info['id'], info['name'], info['author'], info['style'],
             info['time'], info['score'], info['comment'], info['image'])
    cur.execute('''
        insert into musics(musicId, musicName, musicAuthor, musicStyle, musicTime, 
        musicScore, musicComment, musicImage) values (?, ?, ?, ?, ?, ?, ?, ?)''', music)
    conn.commit()


# 获取页面html代码
def getOnePage(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.content
            htmlText = str(html, encoding='utf-8')
            return htmlText
        return None
    except Exception:
        return None

id = 0

# 获取指定内容
def parseOnePage(html):
    soup = BeautifulSoup(html, 'lxml')
    # 专辑id
    global id
    id = id + 1
    # 专辑名称
    name = soup.find(id='wrapper').h1.span.get_text()
    # 专辑作者
    author = soup.find(id='info').find('a').get_text()
    # 流派
    style = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />', html, re.S)
    if len(style) == 0:
        style = ""
    else:
        style = style[0].strip()
    # 发行时间
    time = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />', html, re.S)
    if len(time) == 0:
        time = ""
    else:
        time = time[0].strip()
    # 评分
    score = soup.find(class_='ll rating_num').get_text()
    # 评价人数
    comment = soup.find(class_='rating_people').span.get_text()
    # 图片
    image = soup.find(class_='nbg').attrs['href']

    info = {
        'id': id,
        'name': name,
        'author': author,
        'style': style,
        'time': time,
        'score': score,
        'comment': comment,
        'image': image
    }

    return info

# 获取多个链接
urls = ['https://music.douban.com/top250?start={}'.format(i*25) for i in range(0, 10)]

# 入口
if __name__ == '__main__':
    filename1 = 'doubanmusic.csv'
    filename2 = 'doubanmusic.txt'
    dbname = 'doubanmusic.db'

    if os.path.exists(dbname):
        os.remove(dbname)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''
        create table musics
        (
            musicId int primary key not null,
            musicName text not null,
            musicAuthor text not null,
            musicStyle text,
            musicTime text,
            musicScore real not null,
            musicComment integer not null,
            musicImage text
        );
        '''
    )
    conn.commit()

    with open(filename1, 'w', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'author', 'style', 'time', 'score', 'comment', 'image']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

    for url in urls:
         indexHtml = getOnePage(url)
         soup = BeautifulSoup(indexHtml, 'lxml')
         aTags = soup.find_all('a', class_='nbg')
         for aTag in aTags:
             itemUrl = aTag.attrs['href']
             itemHtml = getOnePage(itemUrl)
             itemInfo = parseOnePage(itemHtml)
             print(itemInfo)
             save2CSV(filename1, itemInfo)
             write2File(filename2, itemInfo)
             save2DB(dbname, itemInfo)
