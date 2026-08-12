from django.shortcuts import render
from .models import News
from .choices import themes 

def news(request):
    news_list = News.objects.all()    
    return render(request,"news/home.html", {'news' : news_list})

def post(request):
    news_list = News.objects.all()    
    return render(request,"news/single.html", {'news' : news_list})
