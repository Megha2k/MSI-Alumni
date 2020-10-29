from django.db import models
from datetime import datetime

class notice_model(models.Model):
	name = models.CharField(max_length=25, blank=True)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='notice', default="", blank=True)