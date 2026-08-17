from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from multiselectfield import MultiSelectField
# Create your models here.

from django.db import models

class Device(models.Model):

    PLATFORM_CHOICES = [
        ('PC','PC'),
        ('PS5','PlayStation 5'),
        ('XBOX','XBOX'),
        ('SWITCH','Nintendo Switch'),
        ('MOBILE','Mobile')
    ]

    STATUS_TAG_CHOICES = [
        ('New','New'),
        ('Top','Top'),
        ('Out of Stock','Out of Stock'),
        ('None','None')
    ]

    device_name = models.CharField(max_length=225)
    device_type = MultiSelectField(max_length=250, choices=PLATFORM_CHOICES, default='', blank=True, null=True)
    color_code = models.CharField(max_length=7, default='#888888', verbose_name="Device Color")
    specifications=models.TextField(blank=True)
    features=models.TextField(max_length=250, blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    status_tag = models.CharField(max_length=50,choices=STATUS_TAG_CHOICES,default='', blank=True, null=True)
    reviews_count = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    def stars_percentage(self):
        if self.stars:
            return self.stars * 20
        return 0

    def __str__(self):
        return self.device_name
