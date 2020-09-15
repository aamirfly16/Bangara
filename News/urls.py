from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path, include
from Bjnewsapp.views import Index, bbc, Google, Travel, Contactus, Times, Indian, Test, video, Base, About
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('magazine/',Times, name = 'magazine'),
    path('business/',bbc, name = 'business'),
    path('sports/',Indian, name = 'sports'),
    path('test/', Test, name='test'),
    path('politics/', Google, name='politics'),
    path('travel/', Travel, name='travel'),
    path('contactus/', Contactus, name='contactus'),
    path('times/', Times, name='time'),
    path('aboutus/', About, name='about'),
    path('base/', Base, name='base'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
