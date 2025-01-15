
from django.shortcuts import render
from .models import *
from django.contrib import admin
# Create your views here.
menu=[{"title":"Главная","url":"home"},
      {"title":"О себе","url":"news"},
      {"title":"Обратная связь","url":"callback"},
      {"title":"admin","url":"admin"}]


def home(reqest):
    posts=Head_page.objects.all()
    return render(reqest,"main/home.html",{'posts':posts,'menu':menu,'title':'Главная'})

def news(reqest):
    about=About_page.objects.all()
    return render(reqest,"main/about.html",{'about':about,'menu':menu,'title':'Новости'})

def callback(reqest):
    call=Contact_page.objects.all()
    return render(reqest,"main/callback.html",{'call':call,'menu':menu,'title':'Обратная связь'})
def admin(reqest):
    return render(reqest,admin.site.urls)



