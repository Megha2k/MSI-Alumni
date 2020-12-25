from django import forms
from django.db import models
from alumni_app.models import notice_model,events_model,display_alumni_model,placement_companies_model,achievements_model,bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model

class notice_form(forms.ModelForm):

	class Meta():
		model = notice_model
		fields = ['name','file']

		labels = {'name':'Name','file':'File'}
		widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'name of the notice to display'}),
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class events_form(forms.ModelForm):

	class Meta():
		model = events_model
		fields = ['name','file']

		labels = {'name':'Name','file':'File'}
		widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'name of the event to display'}),
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class display_alumni_form(forms.ModelForm):

	class Meta():
		model = display_alumni_model
		fields = ['name','description','photo']

		labels = {'name':'Name','description':'Description','photo':'Photo'}
		widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'Name of Alumni'}),
					'description':forms.Textarea(attrs={'required':True,'class':'form-control','placeholder':'description of his/her achievement(s)'}),
				 	'photo':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class slideshow_form(forms.ModelForm):

	class Meta():
		model = slideshow_model
		fields = ['photo']

		labels = {'photo':'Photo'}
		widgets = {
					'photo':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class placement_companies_form(forms.ModelForm):

    class Meta():
        model = placement_companies_model
        fields = ['name','description','month','stipend','bond','rounds','syllabus']

        labels = {'name':'Name','description':'Description','month':'Month','stipend':'Stipend','bond':'Bond','rounds':'Rounds','syllabus':'Syllabus'}

        widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'name of company'}),
					'description':forms.Textarea(attrs={'required':True,'class':'form-control','placeholder':'description of company offerings'}),
				 	'stipend':forms.Textarea(attrs={'required':True,'class':'form-control','placeholder':'stipend details'}),
				 	'bond':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'bond (if any)'}),
				 	'rounds':forms.Textarea(attrs={'required':True,'class':'form-control','placeholder':'names & no. of rounds'}),
				 	'syllabus':forms.Textarea(attrs={'required':True,'class':'form-control','placeholder':'syllabus for preparation'}),
				 	'month': forms.Select(attrs={'required':True})
				  }

class submit_achievements_form(forms.ModelForm):

	class Meta():
		model = achievements_model
		fields = ['names','achievement_name','photo']

		labels = {'names':'Names','achievement_name':'Achievement Name','photo':'Photograph / Collage'}
		widgets = {
					'names':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'Names of Achievers'}),
					'achievement_name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'Name of Achievement'}),
					'photo':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }

class grant_achievements_form(forms.ModelForm):

	class Meta():
		model = achievements_model
		fields = ['achievement_name','checked']

		widgets = {
					'checked': forms.Select(attrs={'required':True,'class':'form-control','id':'checked_id'}),
					'achievement_name':forms.TextInput(attrs={'required':True,'class':'form-control','id':'achievement_name_id'})
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