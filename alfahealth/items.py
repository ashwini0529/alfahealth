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

class AlfahealthDiet(scrapy.Item):
  # url = scrapy.Field()
   dietName = scrapy.Field()
   dietCategory = scrapy.Field()
   dietPlanLength = scrapy.Field()
   mealsPerDay= scrapy.Field()
   targetGender = scrapy.Field()
   weightGoal = scrapy.Field()
   cookingDifficulty = scrapy.Field()
   tags = scrapy.Field()
   description = scrapy.Field()
   dietOptions = scrapy.Field()
   pass

class AlfahealthCaloriesBurned(scrapy.Item):
  # url = scrapy.Field()
   exerciseName = scrapy.Field()
   caloriesBurned = scrapy.Field()
   pass
  # dietPlanLength = scrapy.Field()
class caloriesBurnedInExercise(scrapy.Item):
  exerciseName1 = scrapy.Field()
  exerciseName2 = scrapy.Field()
  caloriesBurned1 = scrapy.Field()
  caloriesBurned2 = scrapy.Field()
  pass


class getFoods(scrapy.Item):
  foodName = scrapy.Field()
  servingSize = scrapy.Field()
  pass

class getExercise(scrapy.Item):
  exerciseName = scrapy.Field()
  procedure = scrapy.Field()
  muscle = scrapy.Field()
  detailed_muscle = scrapy.Field()
  other_muscle_group= scrapy.Field()
  type = scrapy.Field()
  mechanics = scrapy.Field()
  equipments = scrapy.Field()
  difficulty = scrapy.Field()

#get food data

class Food(scrapy.Item):
  foodName=scrapy.Field()
  servingSize=scrapy.Field()
  calories=scrapy.Field()
  carbohydrates=scrapy.Field()
  protiens=scrapy.Field()
  fat=scrapy.Field()
  pass