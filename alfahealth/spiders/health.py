# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import AlfahealthItem
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "health"
    allowed_domains = ["www.bodybuilding.com"]
    start_urls = [
        'http://www.bodybuilding.com/exercises/detail/view/name/ab-roller',
    ]

    def parse(self, response):
       for sel in response.xpath('//ul/li'):
       	item = AlfahealthItem()
       	item['title']=sel.xpath('a/text()').extract()
       	item['link'] = sel.xpath('a/@href').extract()
       	item['desc'] = sel.xpath('text()').extract()
        yield item

