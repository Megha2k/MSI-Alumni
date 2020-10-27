from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from alumni_app.forms import notice_form
from alumni_app.models import notice_model
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
def index(request):
	if request.method == "POST":

		if 'login_form' in request.POST:

			username = request.POST["username"]
			password = request.POST["password"]

			user = authenticate(username=username, password=password)

			if user and user.is_staff:
				login(request,user)
				return HttpResponseRedirect("/notice")

			else:
				return render(request,'index.html',{"status":"Invalid username or password!"})
	else:

		return render(request, 'alumni_app/index.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/homepage")
	
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