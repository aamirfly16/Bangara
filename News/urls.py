"""News URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Bjnewsapp.views import Index, bbc, Sports, Art, Politics, Travel, Contactus, Times

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
    path('magazine/',Times, name = 'magazine'),
    path('business/',bbc, name = 'business'),
    path('sports/',Sports, name = 'sports'),
    path('art/', Art, name='art'),
    path('politics/', Politics, name='politics'),
    path('travel/', Travel, name='travel'),
    path('contactus/', Contactus, name='contactus'),
    # path('times/', Times, name='time'),
]
