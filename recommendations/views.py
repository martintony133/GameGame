from django.shortcuts import render
from .models import RecommendedGame
from django.core.paginator import Paginator
from advertisements.models import Advertisement
import datetime 

def recommendation(request):
    # 1. 撈出原本啲 Game 嘅資料
    free_ranked_games = RecommendedGame.objects.filter(rank_type='free_rank').order_by('rank')
    paid_ranked_games = RecommendedGame.objects.filter(rank_type='paid_rank').order_by('rank')
    regular_games = RecommendedGame.objects.filter(rank_type='none')
    
    game_list = RecommendedGame.objects.order_by('id')
    paginator = Paginator(game_list, 3)
    page_number = request.GET.get('page', 1)
    recommendations_page = paginator.get_page(page_number)
    
    # 2. 喺同一個 View 入面撈埋廣告數據（先用 objects.all() 確保一定有 Data，成功咗先改返日期篩選）
    active_ads = Advertisement.objects.all()
    
    # 3. 將所有嘢打包放入同一個字典傳去前端
    content = {
        'free_game': free_ranked_games,
        'paid_game': paid_ranked_games,
        'regular_game': regular_games,
        'recommendations': recommendations_page,
        'advertisements': active_ads,  # 👈 核心：加埋呢行變數過去 HTML！
    }
    
    return render(request, 'recommendations/home.html', content)

# ⚠️ 注意：原本第 23 行嘅整個 def home_view(request): 可以直接刪除唔要喇！
