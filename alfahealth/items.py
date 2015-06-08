# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlfahealthItem(scrapy.Item):
   url = scrapy.Field()
   size = scrapy.Field()
   name = scrapy.Field()
   also_known_as=scrapy.Field()
   #video_link=scrapy.Field()
   exercise_type= scrapy.Field()
   main_muscle_worked=scrapy.Field()
   other_muscles=scrapy.Field()
   equipment = scrapy.Field()
   mechanics_type=scrapy.Field()
   level=scrapy.Field()
   sport=scrapy.Field()
   force=scrapy.Field()
   procedure=scrapy.Field()
   caution=scrapy.Field()
   bodyImage=scrapy.Field()
   #is Variation needed? 
   #variations=scrapy.Field()
   pass
