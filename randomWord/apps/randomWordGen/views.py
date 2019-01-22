from django.shortcuts import render,HttpResponse,redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(req):
    context={
    "string": get_random_string(length=14)
    }
    req.session['attempt']=req.session['attempt']+1
    print("increment attempt")
    return render(req,'randomWordGen/index.html',context)

def delete(req):
    del req.session['attempt']
    print("delete session attempt")
    return redirect('/')