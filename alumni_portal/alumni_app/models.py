from django.db import models
from datetime import datetime

class notice_model(models.Model):
	name = models.CharField(max_length=25, blank=True)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='notice', default="", blank=True)

class slideshow_model(models.Model):
	title = models.CharField(max_length=25, blank=True)
	description = models.CharField(max_length=250, blank=True)
	photo = models.ImageField(upload_to='slideshow', default="", blank=True)

class bca_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bba_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bed_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bcom_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)