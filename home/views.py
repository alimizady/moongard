from django.shortcuts import render
from django.http import HttpResponse
from .models import Tiket


def userpage(request):
    persion={"output":Tiket.objects.all()}
    return render(request,"userpage.html",context=persion)

def say_hello(requset):
    return HttpResponse("<h>wellcome to my site!!</h>")

def home(requset):
    return HttpResponse(" go to first page : <a href=/home/base</a>")

def sellpage(requset):
    return render(requset,"sellpage.html")

def basepage(requset):
    return render(requset,"base.html")