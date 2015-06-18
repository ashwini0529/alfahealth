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
    	item['dietCategory']=response.xpath('//div[@class="viewSaveDietData"][5]/span/text()').extract()
        item['dietPlanLength']=response.xpath('//div[@class="viewSaveDietData"][6]/span/text()').extract()
        item['mealsPerDay']=response.xpath('//div[@class="viewSaveDietData"][7]/span/text()').extract()
        item['targetGender']=response.xpath('//div[@class="viewSaveDietData"][8]/span/text()').extract()
        item['weightGoal']=response.xpath('//div[@class="viewSaveDietData"][9]/span/text()').extract()
        item['cookingDifficulty']=response.xpath('//div[@class="viewSaveDietData"][10]/span/text()').extract()
        item['tags']=response.xpath('//div[@class="viewSaveDietData"][11]/span/text()').extract()
       	item['description'] = response.xpath('//div[@id="custDietViewUC_upnlView"]/div[2]/div[5]/div/text()').extract()
        item["dietOptions"] = response.xpath('//div[@id="custDietViewUC_upnlView"]/div[2]/div[9]/div/text()')
        return item
