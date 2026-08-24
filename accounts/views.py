from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from orders.models import Order
from games.cart import Cart
# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return render(request,'accounts/register.html')
            else:
                if User.objects.filter(email=email.lower()).exists():
                    messages.error(request,'That email is being used')
                    return render(request,'accounts/register.html')
                else:
                    user = User.objects.create_user(username=username,
                    email=email.lower(),password=password,first_name=first_name,
                    last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('accounts:login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect(request,'accounts/register.html')
    else:
        return render(request,'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('accounts:login')
    return render(request,'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('pages:index')

def dashboard(request):
    orders = Order.objects.filter(user_id=request.user.id)
    for order in orders:
        order.total_sum = sum(item.price * item.quantity for item in order.items.all())
    context = {'orders':orders, 'cart' : Cart(request), }
    return render(request,'accounts/dashboard.html', context)


