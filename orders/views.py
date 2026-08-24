from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from games.models import Game
from devices.models import Device
from games.cart import Cart
from accounts.models import Account
# Create your views here.
def order_create(request):
    print("--- order_create 函數被觸發了！ ---")
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
        
        # 1. 跑迴圈建立所有 Cart 裡面的項目
        for item in cart:
            print("=== 正在處理的 Cart Item ===", item)
            product_obj = None
            device_obj = None
            item_type = item.get('type')
            item_id = item.get('id')
            
            try:
                if item_type == 'game':
                    product_obj = Game.objects.get(id=item_id) if item_id else item.get('product')
                elif item_type == 'device':
                    device_obj = Device.objects.get(id=item_id) if item_id else item.get('device')
                
                print(f"成功解析 -> product_obj: {product_obj}, device_obj: {device_obj}")
                
                OrderItem.objects.create(
                    order=order,
                    product=product_obj,
                    device=device_obj,
                    price=item['price'],
                    quantity=item['quantity']
                )
            except Exception as e:
                print("❌ 建立 OrderItem 失敗，錯誤原因是：", e)
        
        # 2. 【必須移到迴圈外面】所有項目建立完之後，先好清空購物車！
        cart.clear()
        
        messages.success(request, '訂單建立成功！')
        return redirect("accounts:dashboard")

    return render(request, "orders/cart.html", {'cart': cart})

@require_POST
def cart_add(request, product_id):
    item_type = request.POST.get('item_type')
    print("=== CART_ADD 被觸發 ===")
    print("收到的 product_id:", product_id)
    print("收到的 POST item_type:", item_type)
    print("當前請求路徑 (request.path):", request.path)
    
    cart = Cart(request)
    product = None
    
    if item_type == 'device':
        product = get_object_or_404(Device, id=product_id)
    elif item_type == 'game':
        product = get_object_or_404(Game, id=product_id)
    else:
        # 萬一冇傳，行 URL 判斷
        if 'devices' in request.path:
            product = get_object_or_404(Device, id=product_id)
        else:
            product = get_object_or_404(Game, id=product_id)
            
    print("成功抓取的 product 物件:", product)
    print("它的類別 (Type):", type(product))
    
    quantity = int(request.POST.get('quantity', 1))
    override = request.POST.get('override', 'False') == 'True'
    
    cart.add(product=product, quantity=quantity, override_quantity=override)
    print("目前 Cart 內的全部 Key:", list(cart.cart.keys()))
    
    request.session.save()

    return JsonResponse({
        'status': 'success',
        'total_price': str(cart.get_total_price()),  # 轉成字串確保 JSON 傳輸安全
        'cart_count': len(cart),
    })

def cart_remove(request, product_id):
    cart = Cart(request)
    product = None
    
    # 接收前端傳過黎嘅 item_type 黎精準判斷
    item_type = request.POST.get('item_type')
    
    if item_type == 'device':
        product = get_object_or_404(Device, id=product_id)
    elif item_type == 'game':
        product = get_object_or_404(Game, id=product_id)
    else:
        # 兼容你原本嘅 try-except 寫法（萬一前端冇傳 item_type）
        try:
            product = Game.objects.get(id=product_id)
        except Game.DoesNotExist:
            product = get_object_or_404(Device, id=product_id)

    cart.remove(product)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'message': '商品已成功移除！',
            'total_price': cart.get_total_price(),
            'cart_count': len(cart),
        })
    else:
        messages.success(request,"商品已成功移除！")
        return redirect('orders:order_create')

def checkout(request):
    cart = Cart(request)
    context = {'cart':cart,}
    return render(request,"orders/checkout.html", context)

def order_delete(request, order_id):
    # 搵出嗰張單，如果搵唔到就 404
    order = get_object_or_404(Order, id=order_id)
    # 執行刪除
    order.delete()
    messages.success(request, '訂單已成功刪除！')
    # 刪除完跳返去 dashboard 頁面
    return redirect('accounts:dashboard')