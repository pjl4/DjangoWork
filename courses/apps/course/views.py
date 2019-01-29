from django.shortcuts import render,redirect
from apps.course.models import *
from django.contrib import messages
# Create your views here.

def index(req):
    context={
        'courses': Course.objects.all()
    }
    return render(req,'course/index.html',context)
def delete(req,id):
    context={
        'course':Course.objects.get(id=id)
    }
    return render(req,'course/delete.html',context)
def destroy(req,id):
    b = Course.objects.get(id=id)
    b.delete()
    return redirect('/courses')
def create(req):
    errors = Course.objects.validator(req.POST)

    if errors:
        for key,value in errors.items():
            messages.error(req,value)
            return redirect('/courses')
    else:
        Course.objects.create(name=req.POST['name'],desc=req.POST['desc'])
        return redirect('/courses')