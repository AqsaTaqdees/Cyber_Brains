# Create your views of app here.
#render is used for calling templates
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    #To use a string we have to write httpresponse which is used to render a string on website.
    #But ideally we have to use Templates for our responses instead of httpresponse.
    #return HttpResponse('Hi I am home')
    '''Context is a set of variables we sent to our templates'''
    context = {'variable1': '\Bai mein sent hun\\',
               'variable2':'Aur mein var 2 hun'} #This is dictionary
    return render(request,'index.html',context) #render have 3 things 1. request 2. template(index.html) 3. context(dictionary of variables)
def services(request):
    #return HttpResponse("Hi I am service page<a href ='/'> <br> back to home</a>")
    return render(request,'services.html')
def about(request):
    #return HttpResponse("Hi I am about page")
    return render(request,'about.html')
def contact(request):
    #return HttpResponse("Hi I am contact page")
    if request.method == 'POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(firstName=firstName,lastName=lastName, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted!')
    return render(request,'contact.html')