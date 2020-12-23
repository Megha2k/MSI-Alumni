from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from alumni_app.forms import notice_form,events_form,display_alumni_form,placement_companies_form,bca_students_form,bba_students_form,bed_students_form,bcom_students_form,slideshow_form
from alumni_app.models import notice_model,events_model,display_alumni_model,placement_companies_model,bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import pandas as pd


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/homepage")

def index(request):

    slideshow_obj = slideshow_model.objects.all()
    slideshow_list = {'slideshow_obj':slideshow_obj}

    display_alumni_obj = display_alumni_model.objects.all()
    display_alumni_list = {"display_alumni_objs":display_alumni_obj}

    if request.method == "POST":

    	if 'login_form' in request.POST:

    		username = request.POST["username"]
    		password = request.POST["password"]

    		user = authenticate(username=username, password=password)

    		if user and user.is_staff:
    			login(request,user)
    			return HttpResponseRedirect("/msi_admin")

    		else:
    			return render(request,'alumni_app/index.html',{"status":"Invalid username or password!"})
    else:
    	return render(request, 'alumni_app/index.html',{"list_slideshow":slideshow_list,"list_display_alumni":display_alumni_list})


def bca_placement(request):
    placement_companies_obj = placement_companies_model.objects.all()
    placement_companies_list = {'placement_companies_obj':placement_companies_obj}
    return render(request, 'alumni_app/bca_placement.html',placement_companies_list)

def achievements(request):
	return render(request, 'alumni_app/achievements.html')

def notice(request):
	notice_obj = notice_model.objects.all()
	notice_list = {'notice_obj':notice_obj}
	return render(request, 'alumni_app/notice.html',notice_list)

def events(request):
	events_obj = events_model.objects.all()
	events_list = {'events_obj':events_obj}
	return render(request, 'alumni_app/events.html',events_list)

def msi_admin(request):

	form_notice = notice_form(request.POST)
	form_events = events_form(request.POST)
	form_slideshow = slideshow_form(request.POST)
	form_display_alumni = display_alumni_form(request.POST)
	form_placement_companies = placement_companies_form(request.POST)
	form_bca_students = bca_students_form(request.POST)
	form_bba_students = bba_students_form(request.POST)
	form_bed_students = bed_students_form(request.POST)
	form_bcom_students = bcom_students_form(request.POST)

	if 'notice_form' in request.POST:
		form = notice_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'notice_form':form})

	if 'events_form' in request.POST:
		form = events_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'events_form':form})

	if 'slideshow_form' in request.POST:
		form = slideshow_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'slideshow_form':form})

	if 'display_alumni_form' in request.POST:
		form = display_alumni_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'display_alumni_form':form})

	if 'placement_companies_form' in request.POST:
		form = placement_companies_form(request.POST)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'placement_companies_form':form})

	if 'bca_students_form' in request.POST:
		form = bca_students_form(request.POST,request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			csv = pd.read_csv(file)
			for i in range(len(csv)):
				fname = csv['fname'][i]
				lname = csv['lname'][i]
				rollno = csv['rollno'][i]
				email = fname+str(rollno)+"@msi-ggsip.org"
				academic_yr = str(csv['start yr'][i]) + "-" + str(csv['end yr'][i])
				form = bca_students_model(fname=fname,lname=lname,rollno=rollno,email=email,academic_yr=academic_yr,file=file)
				form.save()
		return render(request, 'alumni_app/msi_admin.html',{'bca_students_form':form})

	if 'bba_students_form' in request.POST:
		form = bba_students_form(request.POST,request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			csv = pd.read_csv(file)
			for i in range(len(csv)):
				fname = csv['fname'][i]
				lname = csv['lname'][i]
				rollno = csv['rollno'][i]
				email = fname+str(rollno)+"@msi-ggsip.org"
				academic_yr = str(csv['start yr'][i]) + "-" + str(csv['end yr'][i])
				form = bba_students_model(fname=fname,lname=lname,rollno=rollno,email=email,academic_yr=academic_yr,file=file)
				form.save()
		return render(request, 'alumni_app/msi_admin.html',{'bba_students_form':form})

	if 'bed_students_form' in request.POST:
		form = bed_students_form(request.POST,request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			csv = pd.read_csv(file)
			for i in range(len(csv)):
				fname = csv['fname'][i]
				lname = csv['lname'][i]
				rollno = csv['rollno'][i]
				email = fname+str(rollno)+"@msi-ggsip.org"
				academic_yr = str(csv['start yr'][i]) + "-" + str(csv['end yr'][i])
				form = bed_students_model(fname=fname,lname=lname,rollno=rollno,email=email,academic_yr=academic_yr,file=file)
				form.save()
		return render(request, 'alumni_app/msi_admin.html',{'bed_students_form':form})

	if 'bcom_students_form' in request.POST:
		form = bcom_students_form(request.POST,request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			csv = pd.read_csv(file)
			for i in range(len(csv)):
				fname = csv['fname'][i]
				lname = csv['lname'][i]
				rollno = csv['rollno'][i]
				email = fname+str(rollno)+"@msi-ggsip.org"
				academic_yr = str(csv['start yr'][i]) + "-" + str(csv['end yr'][i])
				form = bcom_students_model(fname=fname,lname=lname,rollno=rollno,email=email,academic_yr=academic_yr,file=file)
				form.save()
		return render(request, 'alumni_app/msi_admin.html',{'bcom_students_form':form})

	return render(request, 'alumni_app/msi_admin.html',{'notice_form':form_notice,'events_form':form_events,'display_alumni_form':form_display_alumni,'placement_companies_form':form_placement_companies,'bca_students_form':form_bba_students,'bba_students_form':form_bca_students,'bed_students_form':form_bed_students,'bcom_students_form':form_bcom_students,'slideshow_form':form_slideshow})