from django import forms
from django.db import models
from alumni_app.models import notice_model 

class notice_form(forms.ModelForm): 
         
	class Meta():
		model = notice_model
		fields = ['name','file']

		labels = {'name':'Name','file':'File'}
		widgets = {
					'name':forms.TextInput(attrs={'required':True,'class':'form-control','placeholder':'name of the notice to display','label':"sdfs"}),
					'file':forms.FileInput(attrs={'required':True,'class':'form-control'})
				  }