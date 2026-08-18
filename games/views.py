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
        context = {'item': single_game}
        return render(request,'games/product.html', context)

