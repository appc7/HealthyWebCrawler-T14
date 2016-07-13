# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaomiAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    appurl = scrapy.Field()
    title = scrapy.Field()
    appid = scrapy.Field()
    category = scrapy.Field()
    # groupid = scrapy.Field()
    cateid = scrapy.Field()
    developer = scrapy.Field()
    rating = scrapy.Field()
    # count = scrapy.Field()
    ratingct = scrapy.Field()
    version = scrapy.Field()
    updatetm = scrapy.Field()
    developerrec = scrapy.Field()
    relatedrec = scrapy.Field()
    image = scrapy.Field()
    # update_time = scrapy.Field()
    # recommended = scrapy.Field()
    # developer_recommended = scrapy.Field()
    # related_recommended = scrapy.Field()
