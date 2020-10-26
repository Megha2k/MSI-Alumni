from django import forms
from django.db import models
from alumni_app.models import notice 

class notice_form(forms.ModelForm):
	class Meta():
		model = notice
		fields = ['name','file']