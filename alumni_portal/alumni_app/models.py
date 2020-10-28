from django.db import models
from datetime import datetime

class notice_model(models.Model):
	name = models.CharField(max_length=25, blank=True)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='notice', default="", blank=True)

class slideshow_model(models.Model):
    title = models.CharField(max_length=25, blank=True)
    description = models.TextField(max_length=250, default='', blank=True)
    photo = models.ImageField(upload_to='slideshow',default="", blank=True)