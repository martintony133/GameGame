from django.shortcuts import render
from games.models import Game
from devices.models import Device
from django.core.paginator import Paginator 
from games.cart import Cart
from news.models import News
# Create your views here.
def index(request):
    news = News.objects.all().order_by('?')[:5]
    devices = Device.objects.all().order_by('?')[:5]
    games = Game.objects.all().order_by('?')[:6]
    selected_ids = [game.id for game in games]
    extra_games = Game.objects.all().exclude(id__in=selected_ids).order_by('?')[:2]
    
    context = {
        'cart': Cart(request),
        'games': games,              # 傳給前端第一區塊（6個）
        'extra_games': extra_games,
        'devices' : devices,
        'news' : news,
    }  
    return render(request, 'pages/index.html', context)

def about_us(request):
    return render(request,'pages/about_us.html')

def faq(request):
    return render(request,'pages/faq.html')

def privacy_policy(request):
    return render(request,'pages/privacy_policy.html')