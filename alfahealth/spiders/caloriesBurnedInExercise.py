# A spider to crawl diet data apt for the user according to the algorithm 
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import caloriesBurnedInExercise
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "caloriesBurnedInExercise"
    allowed_domains = ["www.fitclick.com"]
    start_urls = [
        'http://www.fitclick.com/calories_burned?page=10#.VYKSpaGli1E',
    ]

    def parse(self, response):
    	item = caloriesBurnedInExercise()
    	item['exerciseName1']=response.xpath('//ul/li[@class = "row0"]/div[2]/div[1]/a/text()').extract()
        item['exerciseName2']=response.xpath('//ul/li[@class = "row1"]/div[2]/div[1]/a/text()').extract()
        item['caloriesBurned1']=response.xpath('//ul/li[@class = "row0"]/div[2]/div[2]/div[2]/div[2]/span/text()').extract()
        item['caloriesBurned2']=response.xpath('//ul/li[@class = "row1"]/div[2]/div[2]/div[2]/div[2]/span/text()').extract()
        
        return item
