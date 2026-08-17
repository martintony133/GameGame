from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

PLATFORM_CHOICES = [
    ('PC', 'PC'),
    ('PS5', 'PlayStation 5'),
    ('XBOX', 'Xbox Series X/S'),
    ('SWITCH', 'Nintendo Switch'),
]

class Accessory(models.Model):
    ACCESSORY_CHOICES = [
        ('KEYBOARDS', 'Keyboards'),
        ('MICE & MOUSEPADS', 'Mice & Mousepads'),
        ('WIRED HEADSETS', 'Wired Headsets'),
        ('WIRELESS HEADSETS', 'Wireless Headsets'),
    ]

    STATUS_TAG_CHOICES = [
        ('New', 'New'),
        ('Top', 'Top'),
        ('Out of Stock', 'Out of Stock'),
        ('None', 'None')
    ]

    accessory_name = models.CharField(max_length=225)
    accessory_type = MultiSelectField(max_length=250, choices=ACCESSORY_CHOICES, default='', blank=True, null=True)
    description = models.TextField(blank=True)
    short_description = models.TextField(max_length=250, blank=True)
    platform = MultiSelectField(max_length=250, choices=PLATFORM_CHOICES, default='', blank=True, null=True) # 💡 已補上 PLATFORM_CHOICES 參照
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    status_tag = models.CharField(max_length=50, choices=STATUS_TAG_CHOICES, default='', blank=True, null=True)
    reviews_count = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField()
    is_free = models.BooleanField(default=False, blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def stars_percentage(self):
        if self.stars:
            return self.stars * 20
        return 0

    def __str__(self):
        return self.accessory_name


class AccessoryColor(models.Model):
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, related_name='colors')
    color_name = models.CharField(max_length=100, help_text="e.g. Royal Grey, Blue Chill")
    color_code = models.CharField(max_length=7, default="#ffffff", verbose_name="Hex color code")

    def __str__(self):
        return f"{self.color_name} ({self.color_code})"
