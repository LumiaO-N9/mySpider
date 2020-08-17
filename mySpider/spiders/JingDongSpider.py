# coding=utf-8
import json

import scrapy
import re
from mySpider.items import JingDongItem


# 启动爬虫
# 第一种方式：cmd 中 执行 scrapy crawl 爬虫名
class JingDongSpider(scrapy.Spider):
    # 爬虫名
    name = "JingDongSpider"
    # 自定义请求头
    heads = {
        ":authority": "sclub.jd.com",
        ":method": "GET",
        ":path": "/comment/productPageComments.action?callback=fetchJSON_comment98vv1&productId=100002672294&score=0&sortType=5&page=0&pageSize=10&isShadowSku=100001490211&fold=1",
        ":scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "referer": "https://item.jd.com/100002672294.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }

    # 指定爬虫程序开始的URL，会根据url发送一个Request
    # 自动发起请求
    # start_urls = ["https://www.baidu.com"]
    # 手动发起请求
    def start_requests(self):
        for i in range(20):
            url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100012885246&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&rid=0&fold=1" % (
                i)
            yield scrapy.Request(url=url, headers=self.heads, callback=self.parse)

    # 回调函数，处理服务器返回的Response
    def parse(self, response):
        print("回调函数")
        # 使用正则表达式 将 json字符串切分出来
        # flags 贪婪匹配
        r = re.compile(r'[(](.*)[)]', re.S)  # 贪婪匹配
        list = r.findall(response.text)
        print(list[0])
        jsonComment = json.loads(list[0])
        comments = jsonComment['comments']
        for comment in comments:
            id = comment["id"]
            content = comment["content"]
            nickname = comment["nickname"]
            score = comment["score"]
            jingDongItem = JingDongItem()
            jingDongItem['id'] = id
            jingDongItem['content'] = content
            jingDongItem['nickname'] = nickname
            jingDongItem['score'] = score

            # 可以将Item发送给pipeline处理
            yield jingDongItem
