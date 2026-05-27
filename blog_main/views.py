from django.shortcuts import render,redirect
from .forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import * 
from .forms import *
from django.contrib.auth import authenticate, login, logout

def home(request):
    category = Category.objects.all()
    blog = Blog.objects.all()
    context = {
        'category':category,
        'blog':blog
    }
    return render(request,'home-blogs.html',context)

def categoryFilter(request,id):
    blog = Blog.objects.filter(category_id=id)
    category = Category.objects.all()
    context = {
        'category':category,
        'blog':blog,
    }
    return render(request,'home-blogs.html',context)

def Continue_Reading(request,slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog':blog
        }
    return render(request,'continueation.html',context)

def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)
        
def Logout(request):
    logout(request)
    return redirect('login')
