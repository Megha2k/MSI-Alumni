from django.db import models
from datetime import datetime
from django.urls import reverse

class notice_model(models.Model):
	name = models.CharField(max_length=40, blank=True)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='notice', default="", blank=True)

class events_model(models.Model):
	name = models.CharField(max_length=40, blank=True)
	date = models.DateTimeField(default=datetime.now)
	file = models.FileField(upload_to='events', default="", blank=True)

class slideshow_model(models.Model):
	photo = models.ImageField(upload_to='slideshow', default="", blank=True)

class display_alumni_model(models.Model):
	name = models.CharField(max_length=25, blank=True)
	description = models.TextField(max_length=250, blank=True)
	photo = models.ImageField(upload_to='slideshow', default="", blank=True)

	def get_absolute_url(self):
		return reverse("alumniDetail",kwargs={'pk':self.pk})

	def __str__(self):
		return self.name


month_list = [('january','January'),('february','February'),('march','March'),('april','April'),('may','May'),('june','June'),('july','July'),('august','August'),('september','September'),('october','October'),('november','November'),('december','December')]
check_list = [('yes','yes'),('no','no'),('unknown','unknown')]

class placement_companies_model(models.Model):
    name = models.CharField(max_length=25, blank=True)
    description = models.TextField(max_length=250, blank=True)
    month = models.CharField(max_length=9, choices=month_list, default='august', blank=True)
    stipend = models.TextField(max_length=250, blank=True)
    bond = models.CharField(max_length=10, blank=True)
    rounds = models.TextField(max_length=250, blank=True)
    syllabus = models.TextField(max_length=250, blank=True)
    bca = models.CharField(max_length=7, choices=check_list, default='unknown', blank=True)
    bba = models.CharField(max_length=7, choices=check_list, default='unknown', blank=True)
    bed = models.CharField(max_length=7, choices=check_list, default='unknown', blank=True)
    bcom = models.CharField(max_length=7, choices=check_list, default='unknown', blank=True)

class achievements_model(models.Model):
    names = models.CharField(max_length=250, blank=True)
    achievement_name = models.CharField(max_length=40, blank=True)
    photo = models.ImageField(upload_to='slideshow', default="", blank=True)
    checked = models.CharField(max_length=7, choices=check_list, default='unknown', blank=True)

class bca_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	email = models.EmailField(max_length=35, default="", blank=True)
	academic_yr = models.CharField(max_length=9, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bba_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	email = models.EmailField(max_length=25, default="", blank=True)
	academic_yr = models.CharField(max_length=9, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bed_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	email = models.EmailField(max_length=40, default="", blank=True)
	academic_yr = models.CharField(max_length=9, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

class bcom_students_model(models.Model):
	fname = models.CharField(max_length=25, blank=True)
	lname = models.CharField(max_length=25, blank=True)
	rollno = models.PositiveIntegerField(unique=True, blank=True)
	email = models.EmailField(max_length=25, default="", blank=True)
	academic_yr = models.CharField(max_length=9, blank=True)
	file = models.FileField(upload_to='alumni', default="", blank=True)

