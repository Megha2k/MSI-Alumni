from django.shortcuts import render
# from django.http import HttpResponse
from alumni_app.forms import notice_form
from alumni_app.models import notice_model

def index(request):
	return render(request, 'alumni_app/index.html')

def bca_placement(request):
	return render(request, 'alumni_app/bca_placement.html')

def achievements(request):
	return render(request, 'alumni_app/achievements.html')

def notice(request):
	notice_obj = notice_model.objects.all()
	notice_list = {'notice_obj':notice_obj}
	return render(request, 'alumni_app/notice.html',notice_list)

def msi_admin(request):

	form_notice = notice_form(request.POST)
	
	if 'notice_form' in request.POST:
		form = notice_form(request.POST,request.FILES)
		if form.is_valid():
			form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'notice_form':form})

	return render(request, 'alumni_app/msi_admin.html',{'notice_form':form_notice})