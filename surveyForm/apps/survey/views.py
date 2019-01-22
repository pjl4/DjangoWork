from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(req):
    req.session['times']=0
    return render(req,'survey/index.html')

def process(req):
    req.session['name']=req.POST['name']
    req.session['location']=req.POST['location']
    req.session['language']=req.POST['language']
    req.session['comment']=req.POST['comment']
   
    req.session['times']=req.session['times']+1
    return redirect('/result')

def result(req):
    return render(req,'survey/result.html')