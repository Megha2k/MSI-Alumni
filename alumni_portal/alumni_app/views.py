from django.shortcuts import render
# from django.http import HttpResponse
from alumni_app.forms import notice_form

def index(request):
	return render(request, 'alumni_app/index.html')

def bca_placement(request):
	return render(request, 'alumni_app/bca_placement.html')

def achievements(request):
	return render(request, 'alumni_app/achievements.html')

def notice(request):
	return render(request, 'alumni_app/notice.html')

def msi_admin(request):
	form_notice = notice_form(request.POST)
	if 'notice_form' in request.POST:
		form = notice_form(request.POST,request.FILES)
		if "file" in request.FILES:
			file = request.FILES["file"]
		else:
			print("no file")

		if form.is_valid():
			form.save(commit=True)
			print('form submitted successfully!')
		else:
			print('invalid input')
		return render(request, 'alumni_app/msi_admin.html',{'notice_form':form})
	return render(request, 'alumni_app/msi_admin.html',{'notice_form':form_notice})
