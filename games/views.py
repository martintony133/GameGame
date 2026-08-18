from django.shortcuts import render
from .models import Game
from django.core.paginator import Paginator
from .cart import Cart

# Create your views here.
def game(request):
        game_list = Game.objects.order_by('id')
        paginator = Paginator(game_list, 6)
        page_number = request.GET.get('page',1)
        games_page = paginator.get_page(page_number)
        context = {'games' : games_page, 'cart' : Cart(request)}
        return render(request,'games/home.html', context)
