import datetime

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.
def welcome(request):
    return render(request,"testapp/home_page.html")

def date(request):
    date=datetime.date.today()
    time= datetime.datetime.now()
    return render(request,"testapp/Date.html",{'date':date,'time':time})

