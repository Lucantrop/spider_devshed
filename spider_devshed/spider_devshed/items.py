# -*- coding: utf-8 -*-

import scrapy


class DevShedItem(scrapy.Item):
    # define the fields for item
    title = scrapy.Field()
    link = scrapy.Field()
    answers = scrapy.Field()
