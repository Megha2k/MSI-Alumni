from django import forms
from django.db import models
from alumni_app.models import notice_model,bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model

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

		labels = {'title':'Title','description':'Description','photo':'Photo'}
		widgets = {
					'title':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'title to display'}),
					'description':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'description of photograph'}),
				# 	'photo':forms.ImageField(attrs={'required':True,'class':'form-control'})
				  }

class bca_students_form(forms.ModelForm):

	class Meta():
		model = bca_students_model
		fields = ['file']

		labels = {'file':'File'}
		widgets = {
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class bba_students_form(forms.ModelForm):

	class Meta():
		model = bba_students_model
		fields = ['file']

		labels = {'file':'File'}
		widgets = {
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class bed_students_form(forms.ModelForm):

	class Meta():
		model = bed_students_model
		fields = ['file']

		labels = {'file':'File'}
		widgets = {
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class bcom_students_form(forms.ModelForm):

	class Meta():
		model = bcom_students_model
		fields = ['file']

		labels = {'file':'File'}
		widgets = {
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }