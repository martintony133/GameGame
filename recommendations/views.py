from django.shortcuts import render
from .models import RecommendGame

# Create your views here.
def recommendation(request):
    free_ranked_games = RecommendGame.objects.filter(rank_type='free_rank').order_by('rank')
    paid_ranked_games = RecommendGame.objects.filter(rank_type='paid_rank').order_by('rank')
    regular_games = RecommendGame.objects.filter(rank_type='none')
    game_list = RecommendGame.objects.order_by('?')[:5]
    content = {
        'free_game' : free_ranked_games,
        'paid_game' : paid_ranked_games,
        'regular_game' : regular_games,
        'recommendations' : game_list,
    }
    return render(request,'recommendations/home.html', content)
