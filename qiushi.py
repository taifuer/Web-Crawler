# -*- coding:utf-8 -*-
"""
@name:   qiushi.py
@time:   2019 / 05 / 03
@author: taifu
"""

import requests
import re
import json

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# 转化为汉字
def verifySex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

# 得到一页的所有笑话
def getJoke(url):
    res = requests.get(url, headers=headers)
    html = res.text

    # id
    ids = re.findall('<h2>(.*?)</h2>', html, re.S)

    # level
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', html, re.S)

    # sex
    sexs = re.findall('<div class="articleGender (.*?)Icon">', html, re.S)

    # content
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', html, re.S)

    # comment
    comments = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', html, re.S)

    # like
    likes = re.findall('<i class="number">(\d+)</i>', html, re.S)

    result = []
    for id, level, sex, content, comment, like in zip(ids, levels, sexs, contents, comments, likes):
        info = {
            'id': id.strip(),
            'level': level.strip(),
            'sex': verifySex(sex),
            'content': content.strip(),
            'comment': comment.strip(),
            'like': like.strip()
        }
        # print(id, level)
        result.append(info)
    return result

# 得到多个url
urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 31)]

# 入口
if __name__ == '__main__':
    for url in urls:
        jokeList = getJoke(url)
        print(url, len(jokeList))
        for joke in jokeList:
            # 保存到文件
            f = open('./jokes.txt', 'a+', encoding='utf-8')
            try:
                f.write(json.dumps(joke, ensure_ascii=False) + '\n')
                # f.write(joke['id'] + ' ')
                # f.write(joke['level'] + ' ')
                # f.write(joke['sex'] + '\n')
                # f.write(joke['content'] + '\n')
                # f.write(joke['comment'] + ' ')
                # f.write(joke['like'] + '\n\n')
                f.close()
            except UnicodeDecodeError:
                pass