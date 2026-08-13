from django.shortcuts import render
from .models import Genre
from django.core.paginator import Paginator

# Create your views here.
def genre(request):
        genre_list = Genre.objects.order_by('id')
        paginator = Paginator(genre_list, 6)
        page_number = request.GET.get('page',1)
        genres_page = paginator.get_page(page_number)
        context = {'genres' : genres_page}
        return render(request,'genres/home.html', context)