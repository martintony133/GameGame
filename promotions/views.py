from django.shortcuts import render, get_object_or_404
from .models import FestivalSale
from games.cart import Cart
from advertisements.models import Advertisement
from django.core.paginator import Paginator


# Create your views here.
def promo_game(request):
    promotions_query = FestivalSale.objects.all().prefetch_related('products')
    active_ads = Advertisement.objects.all()
    paginator = Paginator(promotions_query,3)
    page_number = request.GET.get('page', 1)
    promotions_list = paginator.get_page(page_number)
    context = {
        'promotions': promotions_list,
        'cart' : Cart(request),
        'advertisements': active_ads, 
    }
    return render(request, 'promotions/game.html', context)

def discount_page(request, pk):
    sale_activity = get_object_or_404(
        FestivalSale.objects.prefetch_related('products'), 
        pk=pk
    )
    active_ads = Advertisement.objects.all()
    context = {
        'activity': sale_activity,
        'cart' : Cart(request),
        'advertisements': active_ads, 
    }
    return render(request, 'promotions/discount_page.html', context)