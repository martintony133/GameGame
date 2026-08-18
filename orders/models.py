from django.db import models
from games.models import Game
# Create your models here.
class Order(models.Model):
    product = models.CharField(max_length=100)
    product_id = models.IntegerField()
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

class OrderItem(models.Model):
    Order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Game, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __set__(self):
        return f"Order ID:{self.id}"

    def get_cost(self):
        return self.price * self.quantity