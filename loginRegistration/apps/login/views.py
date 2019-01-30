from django.shortcuts import render,redirect
from apps.login.models import *
from django.contrib import messages
import bcrypt
# Create your views here.


def index(req):
    return render(req,'login/index.html')

def register(req):
    errors=User.objects.validateData(req.POST)

    if errors:
        for key,value in errors.items():
            messages.error(req,value)
        return redirect(f'/')
    else:
        pw_hash=bcrypt.hashpw(req.POST['password'].encode(),bcrypt.gensalt())
        user=User.objects.create(first_name=req.POST['first_name'],last_name=req.POST['last_name'],email=req.POST['email'],pw_hash=pw_hash)
        req.session['name']=user.first_name
        return redirect(f'/success/')

def success(req):
    return render(req,'login/success.html')

def login(req):
    errorslogin=User.objects.validate_login(req.POST)

    if errorslogin:
        for key,value in errorslogin.items():
            messages.error(req,value)
        return redirect(f'/')
    else:
        user=User.objects.get(email=req.POST['email'])
        req.session['name']=user.first_name
        return redirect(f'/success/')