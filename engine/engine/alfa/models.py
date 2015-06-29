from django.db import models

# Create your models here.

class Bmi(models.Model):
	user_id = models.IntegerField()
	bmi = models.IntegerField(default = 0)
	pub_date = models.DateTimeField('date published')
	desired_id = models.IntegerField(default = 0) # This would be the wannabe avatar id.. that he choses at the time of startup
	def __unicode__(self):              # __unicode__ on Python 2
        return  u % (self.user_id, self.bmi,self.pub_date,self.desired_id)
class exerciseList(models.Model):
	exercise_id = models.IntegerField()
	exercise_name = models.CharField(max_length = 256)
	exercise_for = models.CharField(max_length = 256) # Which bodypart




