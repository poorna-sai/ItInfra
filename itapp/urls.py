"""itinfra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path("" , views.Register , name = "register"),
    path("login/" , views.Login , name = "login"),
    path("logout/" , views.logout , name = "logout"),
    path("dashboard/" , views.admin_dashboard , name = "dashboard"),
    path('forget-password/', views.ForgetPassword , name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name = "change-password"), 

    path("add_data/" , views.add_data , name ='add_data'),
    path("show_solved/" , views.show_solved , name ='show_solved'),
    path("solved/<str:id>/" , views.solved , name ='solved'),
    path("mycomplaints/" , views.mycomplaints , name ='mycomplaints'),
    path("show_complaints/" , views.show_complaints , name ='show_complaints'),
    path("Edit_data/<str:id>/" , views.Edit_data , name ='Edit_data'),
    path("add_complaint" , views.add_complaint , name ='add_complaint'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
