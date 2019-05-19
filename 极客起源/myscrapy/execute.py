# -*- coding:utf-8 -*-
"""
@name:   execute.py
@time:   2019 / 05 / 17
@author: taifu
"""
from scrapy import cmdline
cmd = 'scrapy crawl BlogSpider -o blog.json -s FEED_EXPORT_ENCODING=utf-8'.split()
cmdline.execute(cmd)
