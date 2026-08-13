from django.shortcuts import render
from .models import RecommendedGame
from django.core.paginator import Paginator

# Create your views here.
def recommendation(request):
    free_ranked_games = RecommendedGame.objects.filter(rank_type='free_rank').order_by('rank')
    paid_ranked_games = RecommendedGame.objects.filter(rank_type='paid_rank').order_by('rank')
    regular_games = RecommendedGame.objects.filter(rank_type='none')
    game_list = RecommendedGame.objects.order_by('id')
    paginator = Paginator(game_list, 3)
    page_number = request.GET.get('page',1)
    recommendations_page = paginator.get_page(page_number)
    content = {
        'free_game' : free_ranked_games,
        'paid_game' : paid_ranked_games,
        'regular_game' : regular_games,
        'recommendations' : recommendations_page,
    }
    return render(request,'recommendations/home.html', content)
