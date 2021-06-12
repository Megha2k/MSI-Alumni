from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from alumni_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # GOOGLE SIGN IN
    path('chat/', include('chat.urls'),name='chat'), #For Chat
    url(r'^alumni_app/', include('alumni_app.urls')),
    url(r'^$', views.index, name='index'),
    path('bca_placement/', views.bca_placement, name='bca_placement'),
    path('bba_placement/', views.bba_placement, name='bba_placement'),
    path('bed_placement/', views.bed_placement, name='bed_placement'),
    path('bcom_placement/', views.bcom_placement, name='bcom_placement'),
    path('achievements/', views.achievements, name='achievements'),
    path('notice/', views.notice, name='notice'),
    path('events/', views.events, name='events'),
    path('login_success/', views.login_success, name='login_success'),
    path('msi_admin/', views.msi_admin, name='msi_admin'),
    path('alumni/', views.alumni, name='alumni'),
    url(r'^homepage',views.index,name='homepage'),
    path('send/', views.sendanemail, name="sendemail"),
    url(r'^gallery',views.gallery,name="gallery"),
    url(r'^allAlumni',views.AlumniListView.as_view(),name="allAlumni"),
    path('alumni/<int:pk>', views.AlumniDetailView.as_view(), name='alumniDetail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)