# -*- coding:utf-8 -*-
"""
@name:   doubanbook.py
@time:   2019 / 05 / 04
@author: taifu
"""

# 使用lxml和xpath完成豆瓣读书top250的爬虫

from lxml import etree
import requests
import json

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# 获取页面html代码
def getOnePage(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except Exception:
        return None

# 排名
rank = 0

# 抓取指定内容
def parseOnePage(html):
    selector = etree.HTML(html)
    # 选取指定节点tr
    items = selector.xpath('//tr[@class="item"]')
    for item in items:
        bookTitle = item.xpath('td/div/a/@title')
        bookImage = item.xpath('td/a/img/@src')
        bookLink = item.xpath('td/div/a/@href')
        bookInfo = item.xpath('td/p[@class="pl"]/text()')
        bookScore = item.xpath('td/div/span[@class="rating_nums"]/text()')
        bookComment = item.xpath('td/div/span[@class="pl"]/text()')
        bookQuote = item.xpath('td/p[@class="quote"]/span/text()')
        print('《' + bookTitle[0] + '》 已完成')
        global rank
        rank = rank + 1
        yield {
            'bookRank': str(rank),
            'bookTitle': bookTitle[0],
            'bookImage': bookImage[0],
            'bookLink': bookLink[0],
            'bookInfo': bookInfo[0],
            'bookScore': bookScore[0],
            'bookComment': bookComment[0].strip('(').strip(')').strip(),
            'bookQuote': (bookQuote[0] if (len(bookQuote) > 0) else '')
        }

# 保存到文件
def writeToFile(content):
    with open('doubanbook.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

# 得到多个url
urls = ['https://book.douban.com/top250?start={}'.format(str(i*25)) for i in range(0, 10)]

# 入口
if __name__ == '__main__':
    for url in urls:
        html = getOnePage(url)
        for item in parseOnePage(html):
            writeToFile(item)