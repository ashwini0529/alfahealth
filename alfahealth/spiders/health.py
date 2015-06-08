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
    	item = AlfahealthItem()
    	item['name']=response.xpath('//*[@id="exerciseDetails"]/h1/text()').extract()
    	item['also_known_as']=response.xpath('//*[@id="exerciseDetails"]/p/label/text()').extract()
    	#item['video_link']=response.xpath('//*[@id="maleVideo"]/video/source/text()').extract()
    	item['exercise_type']=response.xpath('//*[@id="exerciseDetails"]/span[1]/a/text()').extract()
    	item['main_muscle_worked']=response.xpath('//*[@id="exerciseDetails"]/span[2]/a/text()').extract()
    	item['other_muscles']=response.xpath('//*[@id="exerciseDetails"]/span[3]/a/text()').extract()
    	item['equipment']=response.xpath('//*[@id="exerciseDetails"]/span[4]/a/text()').extract()
    	item['mechanics_type']=response.xpath('//*[@id="exerciseDetails"]/span[5]/a/text()').extract()
    	item['level']=response.xpath('//*[@id="exerciseDetails"]/span[6]/a/text()').extract()
    	item['level']=response.xpath('//*[@id="exerciseDetails"]/span[7]/a/text()').extract()
    	item['force']=response.xpath('//*[@id="exerciseDetails"]/span[8]/a/text()').extract()
    	item['procedure']=response.xpath('//div[@class="guideContent"]/ol/li/text()').extract()
    	return item
