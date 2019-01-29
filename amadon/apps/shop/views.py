from django.shortcuts import render,redirect
from django.contrib import messages
from apps.shop.models import *

# Create your views here.
def index(req):
    context={
        'items':Item.objects.all()
    }
    return render(req,'shop/index.html',context)

def buy(req):
    id=req.POST['id']
    purchase=Item.objects.get(id=id)
    total= float(purchase.price) * float(req.POST['number'])

    if req.session.has_key('purchases'):
        req.session['purchases']=int(req.session['purchases']) + int(req.POST['number'])
    else:
        req.session['purchases']= int(req.POST['number'])
    if req.session.has_key('total'):
        req.session['total']=float(req.session['total'])+total
    else:
        req.session['total']=total
    req.session['price']=total
    return redirect(f'/amadon/checkout/')

def checkout(req):
    return render(req,'shop/checkout.html')