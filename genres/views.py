from django.shortcuts import render
from .models import Genre
# Create your views here.
def genre(request):
        games = Genre.objects.all()
        context = {'games' : games}
        return render(request,'genres/home.html', context)