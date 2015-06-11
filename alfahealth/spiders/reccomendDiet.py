# A spider to crawl diet data apt for the user according to the algorithm 
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import AlfahealthDiet
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json
class HealthSpider(scrapy.Spider):
    name = "diet"
    allowed_domains = ["www.fitclick.com"]
    start_urls = [
        'https://www.fitclick.com/free_diet_plan?n=FitClick_Diabetes_Diet_by_FitClick&cd=23982#.VXmk6zeY48p',
    ]

    def parse(self, response):
    	item = AlfahealthDiet()
    	item['dietName']=response.xpath('///div[@class="pageTitle"]/h1/text()').extract()
    	item['dietCategory']=response.xpath(('//div[@class="viewSaveDietData"]//[text()="Diet Category"]/span[@class = "Answer"]/text()').extract())
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
