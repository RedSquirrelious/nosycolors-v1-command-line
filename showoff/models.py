from django.db import models

from django.utils import timezone

import datetime
# Create your models here.



class Target(models.Model):
	target_name = models.CharField(max_length = 30)
	target_handle = models.CharField(max_length = 15, default='some_handle')

	def __str__(self):
		return self.target_name

	def what_handle(self):
		return self.target_handle





class Tweet(models.Model):
	tweet_text = models.CharField(max_length = 140)
	tweet_date = models.DateTimeField('date tweeted')
	target_user = models.ForeignKey(Target)

	def __str__(self):
		return self.tweet_text

	def was_tweeted_in_last_7_days(self):
		return self.tweet_date >= timezone.now() - datetime.timedelta(days = 7)

