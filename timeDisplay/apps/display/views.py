from django.shortcuts import render,HttpResponse,redirect
from time import gmtime, strftime
# Create your views here.


def index(req):
    context={
        "time": strftime("%d/%m/%Y %H:%m %p",gmtime())
    }
    return render(req,'display/index.html',context)