# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    link = scrapy.Field()
    company = scrapy.Field()
    payment = scrapy.Field()
    place = scrapy.Field()
    date = scrapy.Field()
    prop = scrapy.Field()
    exp = scrapy.Field()
    academic = scrapy.Field()
    num = scrapy.Field()
    job_type = scrapy.Field()
    description = scrapy.Field()
