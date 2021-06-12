from django.urls import path

from . import views

app_name= 'chat'
urlpatterns = [
    path('SelectChatRoom', views.SelectChatRoom, name='SelectChatRoom'),
    path('<str:room_name>/', views.room, name='room'),
]