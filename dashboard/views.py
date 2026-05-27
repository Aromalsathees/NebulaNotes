from django.shortcuts import render
from blog_main.models import *
# Create your views here.

def dashboard(request):
    blog = Blog.objects.all().count()
    category = Category.objects.all().count()
    context = {
        'blog':blog,
        'category':category
    }
    return render(request,'dashboard/dashboard.html',context)

