# -*- coding:utf-8 -*-
"""
@name:   doubanmusicMultiThread.py
@time:   2019 / 05 / 18
@author: taifu
"""

import requests
from bs4 import BeautifulSoup
import re
import threading
import datetime

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

# 获取页面html代码
def getOnePage(url, threadName):
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
def parseOnePage(html, threadName):
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

# 获取音乐页面URL
def getMusicUrl(url, threadName):
    indexHtml = getOnePage(url, threadName)
    soup = BeautifulSoup(indexHtml, 'lxml')
    aTags = soup.find_all('a', class_='nbg')
    for aTag in aTags:
        itemUrl = aTag.attrs['href']
        itemHtml = getOnePage(itemUrl, threadName)
        itemInfo = parseOnePage(itemHtml, threadName)
        print(threadName, itemInfo)

# 获取URL
lock = threading.Lock()
def getUrl():
    global urls
    lock.acquire()
    if len(urls) == 0:
        lock.release()
        return ''
    else:
        url = urls[0]
        del urls[0]
    lock.release()
    return url

# 多线程爬虫
class SpiderThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        while True:
            url = getUrl()
            if url != '':
                getMusicUrl(url, self.name)
            else:
                break


# 入口
if __name__ == '__main__':
    startTime = datetime.datetime.now()

    # 获取多个链接
    urls = ['https://music.douban.com/top250?start={}'.format(i * 25) for i in range(0, 10)]

    thread1 = SpiderThread('thread1')
    thread2 = SpiderThread('thread2')
    thread3 = SpiderThread('thread3')
    thread4 = SpiderThread('thread4')

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    endTime = datetime.datetime.now()
    print('耗费时间', (endTime - startTime).seconds, '秒')

