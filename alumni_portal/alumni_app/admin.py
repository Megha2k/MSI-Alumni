from django.contrib import admin
from alumni_app.models import (notice_model,events_model,display_alumni_model,placement_companies_model,achievements_model,
	bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model, ContactUs)



admin.site.site_header = "MSI Alumni Association"

class notice_modelAdmin(admin.ModelAdmin):
	list_display = ["name","date"]
	search_fields = ["name","date"]
	list_filter = ['date']

class events_modelAdmin(admin.ModelAdmin):
	list_display = ["name","date"]
	search_fields = ["name","date"]
	list_filter = ['date']

class display_alumni_modelAdmin(admin.ModelAdmin):
	list_display = ["name","description"]
	search_fields = ["name"]


class placement_companies_modelAdmin(admin.ModelAdmin):
	list_display = ["name","description","month"]
	search_fields = ["name","month"]
	list_filter = ['name','month']


class achievements_modelAdmin(admin.ModelAdmin):
	list_display = ["names","achievement_name"]
	search_fields = ["names"]

class bca_students_modelAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","rollno","email","academic_yr"]
	search_fields = ["fname","rollno","academic_yr","email"]
	list_filter = ['academic_yr']

class bba_students_modelAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","rollno","email","academic_yr"]
	search_fields = ["fname","rollno","academic_yr","email"]
	list_filter = ['academic_yr']

class bed_students_modelAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","rollno","email","academic_yr"]
	search_fields = ["fname","rollno","academic_yr","email"]
	list_filter = ['academic_yr']

class bcom_students_modelAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","rollno","email","academic_yr"]
	search_fields = ["fname","rollno","academic_yr","email"]
	list_filter = ['academic_yr']

class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['fname','lname','email']
	search_fields = ['fname','lname','email']



admin.site.register(notice_model, notice_modelAdminot)
admin.site.register(events_model,events_modelAdmin)
admin.site.register(slideshow_model)
admin.site.register(display_alumni_model,display_alumni_modelAdmin)
admin.site.register(placement_companies_model,placement_companies_modelAdmin)
admin.site.register(achievements_model,achievements_modelAdmin)
admin.site.register(bca_students_model,bca_students_modelAdmin)
admin.site.register(bba_students_model,bba_students_modelAdmin)
admin.site.register(bed_students_model,bed_students_modelAdmin)
admin.site.register(bcom_students_model,bcom_students_modelAdmin)
admin.site.register(ContactUs, ContactUsAdmin)