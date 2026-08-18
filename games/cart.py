from decimal import Decimal
from django.conf import settings
from .models import Game  # 👈 直接引入同資料夾的模型

class Cart:
    def __init__(self, request):
        self.session = request.session
        # ⚠️ 請確保在 settings.py 檔案最後面加上這行：CART_SESSION_ID = 'cart'
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """遍歷購物車品項，從資料庫撈出對應的物件"""
        product_ids = self.cart.keys()
        products = Game.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, product, quantity=1, override_quantity=False):
        """新增商品或修改數量"""
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """從購物車刪除"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        """計算總價"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """清空購物車"""
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __len__(self):
        """計算購物車內所有商品的總數量"""
        return sum(item['quantity'] for item in self.cart.values())
