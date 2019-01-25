from django.shortcuts import render,redirect,HttpResponse
import random
from time import gmtime, strftime
# Create your views here.

def index(req):
    if not req.session.has_key('gold'):
        req.session['gold']=0
    
    return render(req,'gold/index.html')

def process(req):

    if req.POST['building']=="farm":
        number=random.randrange(10,21)
        req.session['gold']= req.session['gold']+number
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if not req.session.has_key('activity'):
            temp_list =[{'activity':"Earned "+str(number)+" from the Farm "+ time},]
            req.session['activity']=temp_list
        else:
            temp_list=req.session['activity']
            temp_list.append({'activity': "Earned "+str(number)+" from the Farm "+ time})
            req.session['activity']=temp_list
        return redirect('/')
    if req.POST['building']=="cave":
        number=random.randrange(5,11)
        req.session['gold']= req.session['gold']+number
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if not req.session.has_key('activity'):
            temp_list =[{'activity': "Earned "+str(number)+" from the Cave "+ time},]
            req.session['activity']=temp_list
        else:
            temp_list=req.session['activity']
            temp_list.append({'activity': "Earned "+str(number)+" from the Cave "+ time})
            req.session['activity']=temp_list
        return redirect('/')
    if req.POST['building']=="house":
        number=random.randrange(2,5)
        req.session['gold']= req.session['gold']+number
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if not req.session.has_key('activity'):
            temp_list =[{'activity':"Earned "+str(number)+" from the House "+ time},]
            req.session['activity']=temp_list
        else:
            temp_list=req.session['activity']
            temp_list.append({'activity': "Earned "+str(number)+" from the House "+ time})
            req.session['activity']=temp_list
        return redirect('/')
    if req.POST['building']=="casino":
        number=random.randrange(-50,50)
        req.session['gold']= req.session['gold']+number
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
        if not req.session.has_key('activity'):
            if number > 0:
                temp_list =[{'activity': "Earned "+str(number)+" from the casino "+ time},]
            if number<0:
                temp_list =[{'activity':"Lost "+str(number)+" from the Casino "+ time},]
            req.session['activity']=temp_list
        else:
            temp_list=req.session['activity']
            if number > 0:
                temp_list.append({'activity':"Earned "+str(number)+" from the Casino "+ time})
            if number<0:
                temp_list.append({'activity':"Lost "+str(number)+" from the Casino "+ time})
            req.session['activity']=temp_list
        return redirect('/')
