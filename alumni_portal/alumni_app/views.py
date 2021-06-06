from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from alumni_app.forms import (notice_form,events_form,display_alumni_form,placement_companies_form,submit_achievements_form,
                             grant_achievements_form,bca_students_form,bba_students_form,bed_students_form,bcom_students_form,slideshow_form)

from alumni_app.models import (notice_model,events_model,display_alumni_model,placement_companies_model,achievements_model,
                               bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model, Contact)

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import pandas as pd
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import (TemplateView, ListView, DetailView )

def index(request):

    slideshow_obj = slideshow_model.objects.all()
    slideshow_list = {'slideshow_obj':slideshow_obj}

    display_alumni_obj = display_alumni_model.objects.all()
    display_alumni_list = {"display_alumni_objs":display_alumni_obj}

    if request.method == "POST":
        if 'contact_form' in request.POST:
            fname = request.POST["fname"]
            lname = request.POST['lname']
            email = request.POST['email']
            subject = request.POST['subject']
            data = Contact(fname=fname,lname=lname,email=email,subject=subject)
            data.save()
            return render(request,'alumni_app/contact_form_redirect.html')

    return render(request, 'alumni_app/index.html',{"list_slideshow":slideshow_list,"list_display_alumni":display_alumni_list})

def bca_placement(request):
    placement_companies_obj = placement_companies_model.objects.all().filter(bca="yes").order_by('name')
    placement_companies_list = {'placement_companies_obj':placement_companies_obj}
    return render(request, 'alumni_app/bca_placement.html',placement_companies_list)

def bba_placement(request):
    placement_companies_obj = placement_companies_model.objects.all().filter(bba="yes").order_by('name')
    placement_companies_list = {'placement_companies_obj':placement_companies_obj}
    return render(request, 'alumni_app/bca_placement.html',placement_companies_list)

def bed_placement(request):
    placement_companies_obj = placement_companies_model.objects.all().filter(bed="yes").order_by('name')
    placement_companies_list = {'placement_companies_obj':placement_companies_obj}
    return render(request, 'alumni_app/bca_placement.html',placement_companies_list)

def bcom_placement(request):
    placement_companies_obj = placement_companies_model.objects.all().filter(bcom="yes").order_by('name')
    placement_companies_list = {'placement_companies_obj':placement_companies_obj}
    return render(request, 'alumni_app/bca_placement.html',placement_companies_list)

def achievements(request):
    achievements_obj = achievements_model.objects.all().filter(checked="yes")
    achievements_list = {"achievements_obj":achievements_obj}
    return render(request, 'alumni_app/achievements.html',achievements_list)

def notice(request):
	notice_obj = reversed(notice_model.objects.all())
	notice_list = {'notice_obj':notice_obj}
	return render(request, 'alumni_app/notice.html',notice_list)

def events(request):
	events_obj = reversed(events_model.objects.all())
	events_list = {'events_obj':events_obj}
	return render(request, 'alumni_app/events.html',events_list)

@login_required
def login_success(request):
    bca_student = bca_students_model.objects.all().filter(email=request.user.email)
    bba_student = bba_students_model.objects.all().filter(email=request.user.email)
    bed_student = bed_students_model.objects.all().filter(email=request.user.email)
    bcom_student = bcom_students_model.objects.all().filter(email=request.user.email)
    User = get_user_model()
    usr = User.objects.all().filter(email=request.user.email,is_active=True,is_staff=True)
    if bca_student:
        return render(request, 'alumni_app/alumni.html')
    elif bba_student:
        return render(request, 'alumni_app/alumni.html')
    elif bed_student:
        return render(request, 'alumni_app/alumni.html')
    elif bcom_student:
        return render(request, 'alumni_app/alumni.html')
    elif usr:
        return msi_admin(request)
    else:
        pass
    return index(request)

@login_required
def alumni(request):

    form_submit_achievements = submit_achievements_form(request.POST)

    if 'submit_achievements_form' in request.POST:
        form = submit_achievements_form(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
        return render(request, 'alumni_app/alumni.html',{'submit_achievements_form':form})

    return render(request, 'alumni_app/alumni.html',{'submit_achievements_form':form_submit_achievements})

@login_required
def msi_admin(request):

    form_notice = notice_form(request.POST)
    form_events = events_form(request.POST)
    form_slideshow = slideshow_form(request.POST)
    form_display_alumni = display_alumni_form(request.POST)
    form_placement_companies = placement_companies_form(request.POST)
    form_grant_achievements = grant_achievements_form(request.POST)
    form_bca_students = bca_students_form(request.POST)
    form_bba_students = bba_students_form(request.POST)
    form_bed_students = bed_students_form(request.POST)
    form_bcom_students = bcom_students_form(request.POST)

    achievements_obj = achievements_model.objects.all().filter(checked="unknown")
    achievements_list = {'achievements_obj':achievements_obj}

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

    if 'grant_achievements_form' in request.POST:
        form = grant_achievements_form(request.POST)
        if form.is_valid():
            achievements_model.objects.all().filter(achievement_name=request.POST["achievement_name"]).update(checked=request.POST["checked"])

    if 'bca_students_form' in request.POST:
        form = bca_students_form(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            csv = pd.read_csv(file)
            for i in range(len(csv)):
                fname = csv['fname'][i]
                lname = csv['lname'][i]
                rollno = csv['rollno'][i]
                email = fname+"0"+str(rollno)+"@msi-ggsip.org"
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

    return render(request, 'alumni_app/msi_admin.html',{"list_achievements":achievements_list,'notice_form':form_notice,'events_form':form_events,'display_alumni_form':form_display_alumni,'placement_companies_form':form_placement_companies,'grant_achievements_form':form_grant_achievements,'bca_students_form':form_bba_students,'bba_students_form':form_bca_students,'bed_students_form':form_bed_students,'bcom_students_form':form_bcom_students,'slideshow_form':form_slideshow})


#send an email function
def sendanemail(request):
    if request.method == "POST":
        emailone = request.POST.getlist('emailarray[]')
        textone = request.POST.get('content')
        emailtwo = ["shubhamrathore514@gmail.com"]
        for i in emailone:
            if i == "bca":
                emailbca = bca_students_model.objects.values_list('email', flat=True)
                emailtwo.extend(emailbca)
            elif i == "bba":
                emailbba = bba_students_model.objects.values_list('email', flat=True)
                emailtwo.extend(emailbba)
            elif i == "bed":
                emailbed = bed_students_model.objects.values_list('email', flat=True)
                emailtwo.extend(emailbed)
            elif i == "bcom":
                emailbcom = bcom_students_model.objects.values_list('email', flat=True)
                emailtwo.extend(emailbcom)
        send_mail(
        "Hello MSI Alumni",
        textone,
        settings.EMAIL_HOST_USER,
        emailtwo
        )
        return render(request, 'alumni_app/msi_admin.html',{'title' : 'send an email'})
    else:
        return render(request, 'alumni_app/msi_admin.html',{'title' : 'send an email'})


def gallery(request):
    slideshow_obj = slideshow_model.objects.all()
    slideshow_list = {'slideshow_obj':slideshow_obj}
    return render(request, 'alumni_app/gallery.html',{"list_slideshow":slideshow_list})



class AlumniListView(ListView):
    
    model = display_alumni_model
    template_name = "alumni_app/display_alumni_list.html"
    def get_context_data(self,**kwargs):
        display_alumni_obj = display_alumni_model.objects.all()
        display_alumni_list = {"list_display_alumni":display_alumni_obj}
        return display_alumni_list
    
    

class AlumniDetailView(DetailView):
    model = display_alumni_model
    template_name = "alumni_app/display_alumni_detail.html"


