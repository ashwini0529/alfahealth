# -*- coding: utf-8 -*-
import scrapy


class HealthSpider(scrapy.Spider):
    name = "health"
    allowed_domains = ["www.bodybuilding.com"]
    start_urls = [
        'http://www.bodybuilding.com/exercises/detail/view/name/ab-roller',
    ]

    def parse(self, response):
       for sel in response.xpath('//ul/li'):
       	item = alfaItem()
       	item['title']=sel.xpath('a/text()').extract()
       	item['link'] = sel.xpath('a/@href').extract()
       	item['desc'] = sel.xpath('text()').extract()
        yield item

