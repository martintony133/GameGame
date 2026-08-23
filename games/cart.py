from decimal import Decimal
from django.conf import settings
from .models import Game
from devices.models import Device

class Cart:
    def __init__(self, request):
        self.session = request.session
        # ⚠️ 請確保在 settings.py 檔案最後面加上這行：CART_SESSION_ID = 'cart'
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart_items = self.cart.copy()
    
        for key, item in cart_items.items():
            # 從 item 入面攞返 type 同 id（或者由 key 拆解，例如 "game_1" -> type="game", id="1"）
            item_type = item.get('type')
            product_id = item.get('id')
    
            # 如果 type 或者 id 唔夠，可以嘗試由 key 拆解 (防禦性編程)
            if not item_type and '_' in key:
                item_type, product_id = key.split('_', 1)
    
            # 初始化欄位
            item['product'] = None
            item['device'] = None
    
            try:
                # 嚴格根據類型去對應嘅 Model 拎資料，避免 ID 撞橋
                if item_type == 'game':
                    item['product'] = Game.objects.get(id=product_id)
                elif item_type == 'device':
                    item['device'] = Device.objects.get(id=product_id)
            except (Game.DoesNotExist, Device.DoesNotExist):
                pass
            
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            # 把 cart_key 帶埋落去前端，方便 form 直接用
            item['cart_key'] = key 
            yield item

    def add(self, product, quantity=1, override_quantity=False):
        # 自動判斷係 Game 定 Device
        if isinstance(product, Device):
            item_type = 'device'
        else:
            item_type = 'game'

        product_id = str(product.id)

        # 關鍵：cart_key 必須嚴格包含 type，例如 "game_1" 或 "device_1"
        cart_key = f"{item_type}_{product_id}"

        if cart_key not in self.cart:
            self.cart[cart_key] = {
                'id': product_id,
                'type': item_type,  # 清楚記低係邊個類型
                'quantity': 0,
                'price': str(product.price) # 視乎你原本用 price 定 unit_price
            }

        if override_quantity:
            self.cart[cart_key]['quantity'] = quantity
        else:
            self.cart[cart_key]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """從購物車移除"""
        # 判斷係 Device 定 Game，用返同 add 一樣嘅 key 邏輯
        if isinstance(product, Device):
            cart_key = f"device_{product.id}"
        else:
            cart_key = f"game_{product.id}"
            
        # 根據正確嘅 cart_key 嚟刪除
        if cart_key in self.cart:
            del self.cart[cart_key]
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
