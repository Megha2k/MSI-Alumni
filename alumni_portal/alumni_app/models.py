from django.db import models
from datetime import datetime

class notice(models.Model):
	name = models.CharField(max_length=25)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='notice',default="")