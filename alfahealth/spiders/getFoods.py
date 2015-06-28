# A spider to crawl diet data apt for the user according to the algorithm 
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import getFoods
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "getFoods"
    allowed_domains = ["www.myfitnesspal.com"]
    start_urls = [
        'http://www.myfitnesspal.com/nutrition-facts-calories/indian-food?brand=indian-food&page=2',
    ]

    def parse(self, response):
    	item = getFoods()
    	item['foodName']=response.xpath('//ul/li[1]/div/div[1]/a/text()').extract()
        item['servingSize'] = response.xpath('//ul/li[1]/div/div[2]/text()').extract()
        return item