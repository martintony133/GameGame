from django.shortcuts import render
from games.models import Game
# Create your views here.
def index(request):
    games =Game.objects.all()
    return render(request,'pages/index.html',{'games':games})

def about_us(request):
    return render(request,'pages/about_us.html')

def faq(request):
    return render(request,'pages/faq.html')

def privacy_policy(request):
    return render(request,'pages/privacy_policy.html')