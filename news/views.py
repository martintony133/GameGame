from django.shortcuts import render, get_object_or_404
from .models import News
from .choices import themes 

def news(request):
    news_list = News.objects.all().order_by('-date')
    return render(request,"news/home.html", {'news' : news_list})

def post(request, post_id):
    single_post = get_object_or_404(News, id=post_id)   
    return render(request, "news/single.html", {'item': single_post})
