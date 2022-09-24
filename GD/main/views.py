from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from main.models import email

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fsubject=request.POST.get('subject')
        fdesc=request.POST.get('message')
        query=email(name=fname,email=femail,subject=fsubject,message=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")
        return redirect('/contact')
        
    return render(request, 'contact.html')
   

def projects(request):
    return render(request, 'projects.html')
