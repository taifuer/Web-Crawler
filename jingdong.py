# -*- coding:utf-8 -*-
"""
@name:   jingdong.py
@time:   2019 / 05 / 08
@author: taifu
"""

import requests
import xlwt
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
    path = 'jingdongImage/'
    if not os.path.exists(path):
        os.makedirs(path)
    name = validateName(name)
    with open(path + name + '.png', 'wb') as f:
        f.write(image.content)

# 写入文件
def writeToFile(content):
    with open('jingdong.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 写入Excel 四个sheet，分别代表总排行、苹果手机、华为手机、小米手机
iAll = 1
iApple = 1
iHuawei = 1
iXiaomi = 1
def writeToExcel(content):
    global iAll, iApple, iHuawei, iXiaomi
    sheetAll.write(iAll, 0, str(iAll))
    sheetAll.write(iAll, 1, content['title'])
    sheetAll.write(iAll, 2, content['price'])
    sheetAll.write(iAll, 3, content['seller'])
    sheetAll.write(iAll, 4, content['url'])
    sheetAll.write(iAll, 5, content['image'])
    iAll = iAll + 1

    if content['title'].lower().find("apple") != -1:
        sheetApple.write(iApple, 0, str(iApple))
        sheetApple.write(iApple, 1, content['title'])
        sheetApple.write(iApple, 2, content['price'])
        sheetApple.write(iApple, 3, content['seller'])
        sheetApple.write(iApple, 4, content['url'])
        sheetApple.write(iApple, 5, content['image'])
        iApple = iApple + 1
    elif content['title'].find("华为") != -1:
        sheetHuawei.write(iHuawei, 0, str(iHuawei))
        sheetHuawei.write(iHuawei, 1, content['title'])
        sheetHuawei.write(iHuawei, 2, content['price'])
        sheetHuawei.write(iHuawei, 3, content['seller'])
        sheetHuawei.write(iHuawei, 4, content['url'])
        sheetHuawei.write(iHuawei, 5, content['image'])
        iHuawei = iHuawei + 1
    elif content['title'].find("小米") != -1:
        sheetXiaomi.write(iXiaomi, 0, str(iXiaomi))
        sheetXiaomi.write(iXiaomi, 1, content['title'])
        sheetXiaomi.write(iXiaomi, 2, content['price'])
        sheetXiaomi.write(iXiaomi, 3, content['seller'])
        sheetXiaomi.write(iXiaomi, 4, content['url'])
        sheetXiaomi.write(iXiaomi, 5, content['image'])
        iXiaomi = iXiaomi + 1


# 得到页面源码
def getOnePage(url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.content
            html_doc = str(html, encoding='utf-8')
            return html_doc
        return None
    except Exception:
        return None

# 获取指定内容
def parseOnePage(html):
    doc = pq(html)
    ul = doc('.gl-warp.clearfix')
    liList = ul('.gl-item')
    for li in liList.items():
        # 名称，有多个描述
        product = li('div > div.p-name.p-name-type-2 > a > em').text().split('\n')
        title = product[0] + "手机"
        # 价格
        price = li('div > div.p-price > strong > i').text()
        # 卖家
        seller = li('div > div.p-shop > span > a').text()
        # 链接
        url = "https:" + li('div > div.p-name.p-name-type-2 > a').attr('href')
        # 图片
        image = "https:" + li('div > div.p-img > a > img').attr("source-data-lazy-img")

        saveImage(image, title)

        yield {
            'title': title,
            'price': price,
            'seller': seller,
            'url': url,
            'image': image
        }

# 入口
if __name__ == '__main__':

    # 创建Excel
    header = ['排名', '名称', '价格', '卖家', '链接', '图片']
    book = xlwt.Workbook(encoding='utf-8')
    sheetAll = book.add_sheet("所有手机销量排行榜")
    sheetApple = book.add_sheet("苹果手机销量排行榜")
    sheetHuawei = book.add_sheet("华为手机销量排行榜")
    sheetXiaomi = book.add_sheet("小米手机销量排行榜")
    l = len(header)
    for i in range(l):
        sheetAll.write(0, i, header[i])
        sheetApple.write(0, i, header[i])
        sheetHuawei.write(0, i, header[i])
        sheetXiaomi.write(0, i, header[i])

    # 链接已处理，每次读取30页
    for i in range(1, 10):
        url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&psort=3&page=' + str(i) + '&s=' + str((i - 1) * 30 + 1) + '&scrolling=y'
        html = getOnePage(url)
        for item in parseOnePage(html):
            print(item)
            time.sleep(0.05)
            writeToFile(item)
            writeToExcel(item)

    book.save('mobileRank.xls')