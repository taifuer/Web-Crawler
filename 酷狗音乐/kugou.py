# -*- coding:utf-8 -*-
"""
@name:   kugou.py
@time:   2019 / 05 / 07
@author: taifu
"""


import requests
from bs4 import BeautifulSoup
import json
import time

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


# 写入文件
def writeToFile(content):
    with open('kugou.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 获取页面源码
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

    # 排名
    ranks = soup.select('span.pc_temp_num')
    # 歌曲信息
    infos = soup.select('div.pc_temp_songlist > ul > li > a')
    # 歌曲时长
    lens = soup.select('span.pc_temp_tips_r > span')

    result = []
    for rank, info, len in zip(ranks, infos, lens):
        info = {
            'rank': rank.get_text().strip(),
            'singer': info.get_text().strip().split('-')[0],
            'song': info.get_text().strip().split('-')[1],
            'len': len.get_text().strip()
        }
        result.append(info)
    return result

# 获取多个链接
urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1, 23)]

# 入口
if __name__ == '__main__':
    for url in urls:
        html = getOnePage(url)
        items = parseOnePage(html)
        for item in items:
            writeToFile(item)
            print(item)
            time.sleep(0.05)