from django.shortcuts import render
from django.utils import timezone
from .models import Advertisement
from games.cart import Cart


def home_view(request):
    active_ads = Advertisement.objects.all()
    
    # 👈 加呢兩行
    print("=== 偵錯開始 ===")
    print("資料庫入面到底有幾多條廣告：", active_ads.count())
    
    context = {
        'advertisements': active_ads,
        'cart' : Cart(request), 
    }
    return render(request, 'recommendations/home.html', context)