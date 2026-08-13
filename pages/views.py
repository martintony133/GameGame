from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about_us(request):
    return render(request,'pages/about_us.html')

def faq(request):
    return render(request,'pages/faq.html')

def privacy_policy(request):
    return render(request,'pages/privacy_policy.html')