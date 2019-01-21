from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(req):
    response="Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(req):
    response="placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def show(req,number):
    response="placeholder to show blog "+ number
    return HttpResponse(response)

def edit(req,number):
    response="placeholder to edit blog "+ number
    return HttpResponse(response)

def destroy(req,number):
    return redirect('/')