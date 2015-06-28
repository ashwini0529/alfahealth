
# A spider to crawl diet data apt for the user according to the algorithm 
# Will crawl several important data and will parse in json..
# Website : www.fitclick.com
import scrapy
from scrapy.selector import Selector
from scrapy.spider import Spider
from alfahealth.items import getExercise
#  trying to crawl data of the exercise named 'Ab- Roller' and send the required details in json

#a function to get all the exercise urls 
test = 'https://www.jefit.com/exercises/'
d = []
d= [test + str(i) for i in range (1350)]

class HealthSpider(scrapy.Spider):
    name = "getExercise"
    allowed_domains = ["www.jefit.com"]
    start_urls = d

    def parse(self, response):
    	item = getExercise()
    	item['exerciseName']=response.xpath('//table[@class = "JefitMainTable"]//tr/td[2]/table[2]/thead/tr/th/text()').extract()
        item['procedure']=response.xpath('//table[@class = "JefitMainTable"]//tr/td[2]/table[3]/tbody/tr/td[1]/text()').extract()
        item['muscle'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[1]/text()').extract()
        item['detailed_muscle'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[2]/text()').extract()
        item['other_muscle_group'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[3]/text()').extract()
        item['type'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[4]/text()').extract()
        item['mechanics'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[5]/text()').extract()
        item['equipments'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[6]/text()').extract()
        item['difficulty'] = response.xpath('//table[@id = "hor-minimalist_2"]/tbody/tr/td[3]/p[7]/text()').extract()
        return item
 