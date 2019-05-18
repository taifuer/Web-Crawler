# -*- coding:utf-8 -*-
"""
@name:   qidian.py
@time:   2019 / 05 / 05
@author: taifu
"""

import time
import xlwt
import requests
import json
from lxml import etree

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# 获取html代码
def getOnePage(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except Exception:
        return None

# 获取指定的内容
def parseOnePage(html):
    selector = etree.HTML(html)
    items = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for item in items:
        title = item.xpath('div[2]/h4/a/text()')[0]
        author = item.xpath('div[2]/p[1]/a[1]/text()')[0]
        type = item.xpath('div[2]/p[1]/a[2]/text()')[0] + ' · ' + item.xpath('div[2]/p[1]/a[3]/text()')[0]
        integrity = item.xpath('div[2]/p[1]/span/text()')[0]
        introduction = item.xpath('div[2]/p[2]/text()')[0].strip()
        print('《' + title + '》 已完成')

        yield {
            'title': title,
            'author': author,
            'type': type,
            'integrity': integrity,
            'introduction': introduction
        }

# 写入文件
def writeToFile(content):
    with open('qidian.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 保存到excel
header = ['标题', '作者', '类型', '完成度', '介绍']
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet("小说")
for h in range(len(header)):
    sheet.write(0, h, header[h])

i = 1
def saveToExcel(content):
    global i
    sheet.write(i, 0, content['title'])
    sheet.write(i, 1, content['author'])
    sheet.write(i, 2, content['type'])
    sheet.write(i, 3, content['integrity'])
    sheet.write(i, 4, content['introduction'])
    i = i + 1

# 获取多个连接
urls = ["https://www.qidian.com/all?page={}".format(str(i)) for i in range(1, 31)]

# 入口
if __name__ == '__main__':
    for url in urls:
        html = getOnePage(url)
        time.sleep(0.1)
        for item in parseOnePage(html):
            writeToFile(item)
            saveToExcel(item)
    book.save('qidian.xls')