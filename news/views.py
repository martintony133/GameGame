from django.shortcuts import render, get_object_or_404
from .models import News
from .choices import themes
from games.cart import Cart
# 1. 匯入廣告模型（根據你的專案架構，廣告位於 advertisements 應用程式中）
from advertisements.models import Advertisement 

def news(request):
    news_list = News.objects.all().order_by('-date')

    active_ads = Advertisement.objects.all()
    
    context = {
        'news': news_list,
        'advertisements': active_ads,
        'cart' : Cart(request), 
    }
    
    return render(request, "news/home.html", context)

def post(request, post_id):
    single_post = get_object_or_404(News, id=post_id)
    active_ads = Advertisement.objects.all()

    context = {
        'item': single_post,
        'advertisements': active_ads,
        'cart' : Cart(request), 
    }
    
    return render(request, "news/single.html", context)