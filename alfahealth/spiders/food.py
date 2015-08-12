# A spider to crawl diet data apt for the user according to the algorithm 
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import Food
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "Food"
    allowed_domains = ["www.myfitnesspal.com"]
    start_urls = [
        'http://www.myfitnesspal.com/food/search?page=2&search=india',
    ]

    def parse(self, response):
        item = Food()
        for i in range(1,10):
            item['foodName']=response.xpath('//ul/li['+str(i)+']/div/div[1]/a[1]/text()').extract()
            x=response.xpath('//ul/li['+str(i)+']/div/div[2]/label[1]/following-sibling::text()').extract()
            item['servingSize']=x[0]
            item['calories']=x[1]
            item['fat']=x[2]
            item['carbohydrates']=x[3]
            item['protiens']=x[4]
            print item