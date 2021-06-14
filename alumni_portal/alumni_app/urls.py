from django.conf.urls import url
from alumni_app import views
from django.urls import path

app_name= 'alumni_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('about',views.about,name='about'),
]