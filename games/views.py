from django.shortcuts import render, get_object_or_404
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

def product(request, product_id):
        single_game = get_object_or_404(Game, pk=product_id)
        previous_game = Game.objects.filter(id__lt=single_game.id).order_by('-id').first()
        next_game = Game.objects.filter(id__gt=single_game.id).order_by('id').first()
        game_list = Game.objects.exclude(id=product_id).order_by('?')[:4]
        context = {
                'item': single_game,
                'previous_game' : previous_game,
                'next_game' : next_game, 
                'cart' : Cart(request), 
                'games' : game_list
                }
        return render(request,'games/product.html', context)

