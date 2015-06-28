from scrapy.spider import Spider
from scrapy.selector import Selector
from my.items import getExercise

class MySpider(Spider):
   name = "getExercise"
   allowed_domains = ["www.jefit.com"]
   start_urls = ["https://www.jefit.com/exercises/1/" ]

def parse(self, response):
   
   item = getExercise()
   item['exerciseName']=response.xpath('//table[@class = "JefitMainTable"]/tbody/tr/td[2]/table[2]/thead/tr/th/text()').extract()
   return item