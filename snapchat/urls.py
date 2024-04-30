"""snapchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('about.html/',about,name='about'),
    path('contact.html/',contact,name='contact'),
    path('detail.html/',detail),
    path('feature.html/',feature),
    path('team.html/',team),
    path('testimonial.html/',testimonial),
    path('blog.html/',blog),
    path('service.html/',service),
    path('product.html/',product),
    path('login/',user_login,name='user_login'),
    path('logout/',logout,name='logout'),
    path('Farms/',register_Farm, name='register_Farm'),
    path('Farms_list/', Farm_list, name='Farm_list'),
    path('register/',register,name='register'),
    path('register_Farm/',register_Farm,name='register_Farm'),
]