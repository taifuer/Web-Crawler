# -*- coding:utf-8 -*-
"""
@name:   BlogSpider.py
@time:   2019 / 05 / 19
@author: taifu
"""

import scrapy
from bs4 import *
from scrapy.loader import *
from myscrapy.items import MyscrapyItem

class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'

    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori&page={}'.format(i) for i in range(1, 3)
    ]

    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'lxml')
        sectionList = soup.find_all(class_='stream-list__item')
        for section in sectionList:
            title = section.find(class_='title').a.get_text()
            quote = section.find(class_='excerpt wordbreak hidden-xs').get_text().strip()
            time = section.find(class_='col-xs-10').get_text().strip()[-12:-2]
            itemLoader = ItemLoader(item=MyscrapyItem(), response=response)
            itemLoader.add_value('title', title)
            itemLoader.add_value('quote', quote)
            itemLoader.add_value('time', time)
            items.append(itemLoader.load_item())
        return items