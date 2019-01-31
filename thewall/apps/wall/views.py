from django.shortcuts import render,redirect
from apps.wall.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(req):

    return render(req ,'wall/index.html')

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
        return redirect(f'/dashboard/')

def dashboard(req):
    context={
        'contents': Message.objects.all(),
    }
    return render(req,'wall/dashboard.html',context)

def login(req):
    errorslogin=User.objects.validate_login(req.POST)

    if errorslogin:
        for key,value in errorslogin.items():
            messages.error(req,value)
        return redirect(f'/')
    else:
        user=User.objects.get(email=req.POST['email'])
        req.session['name']=user.first_name
        req.session['userid']=user.id
        return redirect(f'/dashboard/')

def message(req):
    Message.objects.create(message=req.POST['message'],user_messages=User.objects.get(id=req.session['userid']))
    
    return redirect(f'/dashboard/')

def comment(req):
    Comment.objects.create(comment=req.POST['comment'],messages_comments=(Message.objects.get(id=req.POST['id'])),user_comments=User.objects.get(id=req.session['userid']))
    return redirect(f'/dashboard/')
def logout(req):
    req.session.clear()
    return redirect(f'/')