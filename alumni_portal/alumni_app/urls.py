from django.urls import include, re_path
from alumni_app import views
from django.urls import path

app_name= 'alumni_app'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('about',views.about,name='about'),
]
