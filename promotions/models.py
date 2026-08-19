from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [('Game', 'Game'), ('Accessory', 'Accessory'), ('Device', 'Device')]

    STATUS_TAG_CHOICES = [
            ('New','New'),
            ('Top','Top'),
            ('Out of Stock','Out of Stock'),
            ('None','None')
        ]
    
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    product_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], blank=True, null=True)
    reviews_count = models.IntegerField(default=0, blank=True, null=True)
    status_tag = models.CharField(max_length=50,choices=STATUS_TAG_CHOICES,default='', blank=True, null=True)

    def stars_percentage(self):
            if self.stars:
                return self.stars * 20
            return 0

    def __str__(self):
        return f"[{self.get_product_type_display()}] {self.product_name}"


class FestivalSale(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    products = models.ManyToManyField(Product, through='FestivalSaleItem', related_name='sales', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()


    class Meta:
        verbose_name = "Festival Sale"
        verbose_name_plural = "Festival Sales"

    def _str_(self):
        return self.title

class FestivalSaleItem(models.Model):
    festival_sale = models.ForeignKey(FestivalSale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    individual_sale_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="The event has a separate special price"
    )


    class Meta:
        unique_together = ('festival_sale', 'product') 

    def _str_(self):
        return f"{self.festival_sale.title} - {self.product.product_name}: ${self.individual_sale_price}"

    @property
    def show_status(self):
        now = timezone.localtime(timezone.now())
        if self.festival_sale.start_date <= now <= self.festival_sale.end_date:
            return 'Live'
        elif now < self.festival_sale.start_date:
            return 'UpComing'
        else:
            return 'Expired'
