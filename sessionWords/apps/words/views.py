from django.shortcuts import render,redirect,HttpResponse
from time import gmtime, strftime
# Create your views here.

def index(req):
    return render(req,'words/index.html')


def add(req):
    if 'big' in req.POST:
        showbig=1
    else:
        showbig=0
    if req.session.has_key('words'):
        temp_list=req.session['words']
        temp_list.append({
        'word':req.POST['word'],
        'color': req.POST['color'],
        'big': showbig,
        'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())
        })
        req.session['words']=temp_list
    else:
        temp_list =[{
        'word':req.POST['word'],
        'color': req.POST['color'],
        'big': showbig,
        'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())
        },]
        req.session['words']=temp_list

    return redirect('/session_words')

