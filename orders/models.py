from django.db import models
from games.models import Game
# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Game, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __set__(self):
        return f"Order ID:{self.id}"

    def get_cost(self):
        return self.price * self.quantity