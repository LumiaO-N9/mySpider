# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JingDongItem(scrapy.Item):
    id = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    score = scrapy.Field()
