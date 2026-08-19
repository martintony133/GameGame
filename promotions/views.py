from django.shortcuts import render, get_object_or_404
from .models import FestivalSale
# Create your views here.
def promo_game(request):
    promotions_list = FestivalSale.objects.all().prefetch_related('products')
    context = {
        'promotions': promotions_list
    }
    return render(request, 'promotions/game.html', context)

def discount_page(request, pk):
    sale_activity = get_object_or_404(
        FestivalSale.objects.prefetch_related('products'), 
        pk=pk
    )
    context = {
        'activity': sale_activity,
    }
    return render(request, 'promotions/discount_page.html', context)