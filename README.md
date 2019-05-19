# Web-Crawler
### 介绍

简单的网页爬虫实战，主要练习正则表达式和相关爬虫库网络库的使用。

### 项目

- [豆瓣电影 Top 250](https://movie.douban.com/top250)（正则表达式）

  ```json
  {"index": "1", "image": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg", "title": "肖申克的救赎", "actor": "导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...", "type": "1994 / 美国 / 犯罪 剧情", "score": "9.6", "comment": "1367659人评价", "quote": "希望让人自由。"}
  ```

- [猫眼电影 TOP100榜](https://maoyan.com/board/4?offset=0)（正则表达式）

  ```json
  {"index": "1", "image": "https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c", "title": "霸王别姬", "actor": "张国荣,张丰毅,巩俐", "time": "1993-01-01", "score": "9.5"}
  ```

- [糗事百科段子](https://www.qiushibaike.com/text/)（正则表达式）

  ```json
  {"id": "九头纪", "level": "82", "sex": "男", "content": "大学毕业前，和几个寝室哥们去一家还算比较好的餐厅吃饭。<br/>想到马上要分离了，到吃完时，气氛又点沉沉的。突然冒出只苍蝇在汤盆子上空飞啊飞，8只眼睛就盯着它，估计苍蝇吓坏了，直接掉汤里面溺汤身亡了。洗具来了，我们把服务员叫过来，让她去把领班的叫过来，然后让领班看苍蝇，告诉他“我们把汤喝完了，结果里面有只苍蝇，你们这叫苍蝇汤不叫海带排骨汤啊？你看怎么办吧？”他说给我们换盆。我们不答应，让他去把经理找来。最后汤免费，其他费用打八折。", "comment": "406", "like": "406"}
  ```

- [豆瓣图书 Top 250](https://book.douban.com/top250)（lxml和xpath）

  ```json
  {"bookRank": "1", "bookTitle": "追风筝的人", "bookImage": "https://img3.doubanio.com/view/subject/m/public/s1727290.jpg", "bookLink": "https://book.douban.com/subject/1770782/", "bookInfo": "[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元", "bookScore": "8.9", "bookComment": "437742人评价", "bookQuote": "为你，千千万万遍"}
  ```

- [起点中文网全部作品](https://www.qidian.com/all?page=1)（lxml + xpath）

  ```json
  {"title": "凡人修仙之仙界篇", "author": "忘语", "type": "仙侠 · 神话修真", "integrity": "连载中", "introduction": "凡人修仙，风云再起时空穿梭，轮回逆转金仙太乙，大罗道祖三千大道，法则至尊《凡人修仙传》仙界篇，一个韩立叱咤仙界的故事，一个凡人小子修仙的不灭传说。特说明下，没有看过前传的书友，并不影响本书的阅读体验，"}
  ```

- [小猪房屋信息](http://cs.xiaozhu.com/)（BeautifulSoup 方法选择器和节点选择器）

  ```json
  {"title": "《我行我宿 》小清新&五一地铁口/投影一室", "address": "湖南省长沙市芙蓉区定王台街道五一路东牌楼街25...", "price": "238", "imageUrl": "https://image.xiaozhustatic3.com/00,800,533/51,0,11,100399,2666,2000,fffd393b.jpg", "name": "AA我行我宿"}
  ```

- [酷狗Top500](https://www.kugou.com/yy/rank/home/1-8888.html)（BeautifulSoup CSS选择器）

  ```json
  {"rank": "1", "singer": "陈雪凝 ", "song": " 你的酒馆对我打了烊", "len": "4:11"}
  ```

- [当当图书排行榜](http://search.dangdang.com/?key=python&act=input&page_index=1)（pyquery）

  ```json
  {"title": " Python编程 从入门到实践", "href": "http://product.dangdang.com/24003310.html", "image": "http://img3m0.ddimg.cn/67/4/24003310-1_b_7.jpg", "price": "61.40", "author": "[美]埃里克・马瑟斯（Eric Matthes）", "date": "2016-07-01", "publisher": "人民邮电出版社", "comment": "74550", "detail": "上到有编程基础的程序员，下到10岁少年，想入门Python并达到可以开发实际项目的水平，本书是读者*！ 本书是一本全面的从入门到实践的Python编程教程，带领读者快速掌握编程基础知识、编写出能解决实际问题的代码并开发复杂项目。 书中内容分为基础篇和实战篇两部分。基础篇介绍基本的编程概念，如列表、字典、类和循环，并指导读者编写整洁且易于理解的代码。另外还介绍了如何让程序能够与用户交互，以及如何在代码运行前进行测试。实战篇介绍如何利用新学到的知识开发功能丰富的项目：2D游戏《外星人入侵》，数据可视化实战，Web应用程序。"}
  ```

- [京东手机销量排行榜](https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&psort=1&page=184&s=1&scrolling=y)（pyquery）

  ```json
  {"title": "Apple iPhone XR (A2108) 128GB 黑色 移动联通电信4G手机", "price": "5749.00", "seller": "Apple产品京东自营旗舰店", "url": "https://item.jd.com/100000177760.html", "image": "https://img10.360buyimg.com/n7/jfs/t1/3405/18/3537/69901/5b997c0aE5dc8ed9f/a2c208410ae84d1f.jpg"}
  ```

- [豆瓣音乐TOP250](https://music.douban.com/top250?start=0)（BeautifulSoup + 正则表达式 + sqlite）

  ```json
  {"name": "We Sing. We Dance. We Steal Things.", "author": "Jason Mraz", "style": "民谣", "time": "2008-05-13", "score": "9.1", "comment": "105760", "image": "https://img3.doubanio.com/view/subject/m/public/s2967252.jpg"}
  ```
  
  ![](https://ae01.alicdn.com/kf/HTB1LcuFViLaK1RjSZFx761mPFXam.png)

- [极客起源博客](https://geekori.com/blogsCenter.php?uid=geekori)（Scrapy + Beautiful Soup）

  ```json
  {"title": ["Python从菜鸟到高手（1）：初识Python"], "quote": ["Python是一种面向对象的解释型计算机程序设计语言，由荷兰人吉多·范罗苏姆（Guido van Rossum）于1989年发明，第一个公开发行版发行于1991年。目前Python的最新发行版是Python3.6。"], "time": ["2018-09-03"]},
  ```

### 参考

- [Python3网络爬虫开发实战](https://germey.gitbooks.io/python3webspider/content/)
- [Python从入门到实战·爬虫](https://ke.qq.com/course/395289)