from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from apps.users.models import *
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

def index(req):
    context={
        'users': User.objects.all()
    }
    return render(req,'users/index.html',context)

def new(req):
    return render(req,'users/new.html')

def show(req,id):
    user=User.objects.get(id=id)
    context={
        'user':user
    }
    return render(req,'users/show.html',context)
def delete(req,id):
    b= User.objects.get(id=id)
    b.delete()
    return redirect(f'/users/')

def edit(req,id):
    user=User.objects.get(id=id)
    context={
        'user':user
    }
    return render(req,'users/edit.html',context)
def update(req,id):
    errors= User.objects.validator(req.POST)
    if errors:
        for key,value in errors.items():
            messages.error(req,value)
        return redirect(f'/users/{id}/edit')
    else:
        user=User.objects.get(id=id)
        user.name= req.POST['name']
        user.email=req.POST['email']
        return redirect(f'/users/{id}/show')

def create(req):
    errors= User.objects.validator(req.POST)
    if errors:
        for key,value in errors.items():
            messages.error(req,value)
        return redirect(f'/users/new')

    User.objects.create(name=req.POST['name'],email=req.POST['email'])
    id=User.objects.last().id
    return redirect(f'/users/{id}/show')