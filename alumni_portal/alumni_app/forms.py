from django import forms
from django.db import models
from alumni_app.models import notice_model
from alumni_app.models import slideshow_model

class notice_form(forms.ModelForm):

	class Meta():
		model = notice_model
		fields = ['name','file']

		labels = {'name':'Name','file':'File'}
		widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'name of the notice to display'}),
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class slideshow_form(forms.ModelForm):

	class Meta():
		model = slideshow_model
		fields = ['title','description','photo']

		labels = {'title':'Title','description':'Description','photo':'Photograph'}
		widgets = {
					'title':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'title to display'}),
					'description':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'description of photograph'}),
					'photo':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }