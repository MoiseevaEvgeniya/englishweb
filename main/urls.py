
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
path('admin/', views.admin,name="admin"),
path('', views.home,name="home"),
path('about', views.news,name="news"),
path('callback', views.callback,name="callback")

]



