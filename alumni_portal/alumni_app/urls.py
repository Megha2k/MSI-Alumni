from django.conf.urls import url
from alumni_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]