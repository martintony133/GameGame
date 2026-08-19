from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from games.models import Game
from games.cart import Cart
# Create your views here.
def order_create(request):
    print("--- order_create 函式被觸發了！ ---") 
    cart = Cart(request)
    if request.method == "POST":
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            country=request.POST.get('country'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            message=request.POST.get('message'),
            user_id=request.user.id if request.user.is_authenticated else None
        )
        for item in cart:
            OrderItem.objects.create(
                order=order,                 
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        messages.success(request, '訂單建立成功！')
        return redirect("accounts:dashboard")
    
    return render(request,"orders/cart.html",{'cart':cart})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Game, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override', 'False') == 'True'
    cart.add(product=product, quantity=quantity, override_quantity=override)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'total_price' : cart.get_total_price(),
            'cart_count' : len(cart),
            })
    return redirect('orders:order_create')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Game, id=product_id)
    cart.remove(product)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'total_price' : cart.get_total_price(),
            'cart_count' : len(cart),
            })
    return redirect('orders:order_create')

def checkout(request):
    cart = Cart(request)
    context = {'cart':cart,}
    return render(request,"orders/checkout.html", context)