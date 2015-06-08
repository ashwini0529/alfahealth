# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlfahealthItem(scrapy.Item):
    url= scrapy.Field()
    link= scrapy.Field()
    #desc= scrapy.Field()
    title = scrapy.Field()
    name = scrapy.Field()	
    desc = scrapy.Field()
    	
    pass
