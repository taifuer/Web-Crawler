# Web-Crawler
### 介绍

简单的网页爬虫实战，主要练习正则表达式和部分网络库的使用。

### 项目

- [豆瓣电影 Top 250](https://movie.douban.com/top250)

  ```json
  {"index": "1", "image": "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg", "title": "肖申克的救赎", "actor": "导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...", "type": "1994 / 美国 / 犯罪 剧情", "score": "9.6", "comment": "1367659人评价", "quote": "希望让人自由。"}
  ```

- [猫眼电影 TOP100榜](https://maoyan.com/board/4?offset=0)

  ```json
  {"index": "1", "image": "https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c", "title": "霸王别姬", "actor": "张国荣,张丰毅,巩俐", "time": "1993-01-01", "score": "9.5"}
  ```

- [糗事百科段子](https://www.qiushibaike.com/text/)

  ```json
  {"id": "九头纪", "level": "82", "sex": "男", "content": "大学毕业前，和几个寝室哥们去一家还算比较好的餐厅吃饭。<br/>想到马上要分离了，到吃完时，气氛又点沉沉的。突然冒出只苍蝇在汤盆子上空飞啊飞，8只眼睛就盯着它，估计苍蝇吓坏了，直接掉汤里面溺汤身亡了。洗具来了，我们把服务员叫过来，让她去把领班的叫过来，然后让领班看苍蝇，告诉他“我们把汤喝完了，结果里面有只苍蝇，你们这叫苍蝇汤不叫海带排骨汤啊？你看怎么办吧？”他说给我们换盆。我们不答应，让他去把经理找来。最后汤免费，其他费用打八折。", "comment": "406", "like": "406"}
  ```

- [豆瓣图书 Top 250](https://book.douban.com/top250)

  ```json
  {"bookRank": "1", "bookTitle": "追风筝的人", "bookImage": "https://img3.doubanio.com/view/subject/m/public/s1727290.jpg", "bookLink": "https://book.douban.com/subject/1770782/", "bookInfo": "[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元", "bookScore": "8.9", "bookComment": "437742人评价", "bookQuote": "为你，千千万万遍"}
  ```

- [起点中文网全部作品](https://www.qidian.com/all?page=1)

  ```json
  {"title": "凡人修仙之仙界篇", "author": "忘语", "type": "仙侠 · 神话修真", "integrity": "连载中", "introduction": "凡人修仙，风云再起时空穿梭，轮回逆转金仙太乙，大罗道祖三千大道，法则至尊《凡人修仙传》仙界篇，一个韩立叱咤仙界的故事，一个凡人小子修仙的不灭传说。特说明下，没有看过前传的书友，并不影响本书的阅读体验，"}
  ```

- [小猪房屋信息](http://cs.xiaozhu.com/)

  ```json
  {"title": "《我行我宿 》小清新&五一地铁口/投影一室", "address": "湖南省长沙市芙蓉区定王台街道五一路东牌楼街25...", "price": "238", "imageUrl": "https://image.xiaozhustatic3.com/00,800,533/51,0,11,100399,2666,2000,fffd393b.jpg", "name": "AA我行我宿"}
  ```

### 参考

- [Python3网络爬虫开发实战](https://germey.gitbooks.io/python3webspider/content/)
- [Python从入门到实战·爬虫](https://ke.qq.com/course/395289)