# A spider to crawl calories burnt from each exercise
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import AlfahealthCaloriesBurned
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "caloriesBurned"
    allowed_domains = ["www.fitclick.com"]
    start_urls = [
        'http://www.fitclick.com/exercises_Crunches?eqID=21#.VXm_STeY48o',
    ]

    def parse(self, response):
    	item = AlfahealthCaloriesBurned()
        item['exerciseName']=response.xpath('//div[@class="pageTitle"]/h1/text()').extract()
    	item['caloriesBurned']=response.xpath('(//*[@id="main_content"]/text()').extract()
    	'''
    	item['also_known_as']=response.xpath('//*[@id="exerciseDetails"]/p/label/text()').extract()
    	#item['video_link']=response.xpath('//*[@id="maleVideo"]/video/source/text()').extract()
    	item['exercise_type']=response.xpath('//*[@id="exerciseDetails"]/span[1]/a/text()').extract()
    	item['main_muscle_worked']=response.xpath('//*[@id="exerciseDetails"]/span[2]/a/text()').extract()
    	item['other_muscles']=response.xpath('//*[@id="exerciseDetails"]/span[3]/a/text()').extract()
    	item['equipment']=response.xpath('//*[@id="exerciseDetails"]/span[4]/a/text()').extract()
    	item['mechanics_type']=response.xpath('//*[@id="exerciseDetails"]/span[5]/a/text()').extract()
    	item['level']=response.xpath('//*[@id="exerciseDetails"]/span[6]/a/text()').extract()
    	item['level']=response.xpath('//*[@id="exerciseDetails"]/span[7]/a/text()').extract()
    	item['procedure']=response.xpath('//div[@class="guideContent"]/ol/li/text()').extract()
    	item['caution']=response.xpath('//div[@class="guideContent"]/p[3]/text()').extract()
    	item['bodyImage']=response.xpath('//div[@class="muscles-worked"]//img[@src]/text()').extract()
        #Is variation field needed?
    	#item['variations']=response.xpath('//div[@class="guideContent"]/p[4]/text()').extract()
    	'''
       	return item
