from django.shortcuts import render
from django.http import HttpResponse
from alumni_app.forms import notice_form,bca_students_form,bba_students_form,bed_students_form,bcom_students_form,slideshow_form
from alumni_app.models import notice_model,bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model

def index(request):
    slideshow_obj = slideshow_model.objects.all()
    slideshow_list = {'slideshow_obj':slideshow_obj}
    return render(request, 'alumni_app/index.html',slideshow_list)

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
	form_slideshow = slideshow_form(request.POST)
	form_bca_students = bca_students_form(request.POST)
	form_bba_students = bba_students_form(request.POST)
	form_bed_students = bed_students_form(request.POST)
	form_bcom_students = bcom_students_form(request.POST)

	if 'notice_form' in request.POST:
		form = notice_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'notice_form':form})

	if 'slideshow_form' in request.POST:
		form = slideshow_form(request.POST,request.FILES)
		if form.is_valid():
		    form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'slideshow_form':form})

	if 'bca_students_form' in request.POST:
		form = bca_students_form(request.POST,request.FILES)
		if form.is_valid():
			form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'bca_students_form':form})

	if 'bba_students_form' in request.POST:
		form = bba_students_form(request.POST,request.FILES)
		if form.is_valid():
			form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'bba_students_form':form})

	if 'bed_students_form' in request.POST:
		form = bed_students_form(request.POST,request.FILES)
		if form.is_valid():
			form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'bed_students_form':form})

	if 'bcom_students_form' in request.POST:
		form = bcom_students_form(request.POST,request.FILES)
		if form.is_valid():
			form.save(commit=True)
		return render(request, 'alumni_app/msi_admin.html',{'bcom_students_form':form})

	return render(request, 'alumni_app/msi_admin.html',{'notice_form':form_notice,'bca_students_form':form_bba_students,'bba_students_form':form_bca_students,'bed_students_form':form_bed_students,'bcom_students_form':form_bcom_students,'slideshow_form':form_slideshow})