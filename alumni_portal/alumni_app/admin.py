from django.contrib import admin
from alumni_app.models import notice_model,events_model,display_alumni_model,placement_companies_model,bca_students_model,bba_students_model,bed_students_model,bcom_students_model,slideshow_model

admin.site.register(notice_model)
admin.site.register(events_model)
admin.site.register(slideshow_model)
admin.site.register(display_alumni_model)
admin.site.register(placement_companies_model)
admin.site.register(bca_students_model)
admin.site.register(bba_students_model)
admin.site.register(bed_students_model)
admin.site.register(bcom_students_model)