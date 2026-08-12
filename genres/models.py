from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Genre(models.Model):
    PLATFORM_CHOICES = [
        ('PC','PC'),
        ('PS5','PlayStation 5'),
        ('XBOX','XBOX'),
        ('SWITCH','Nintendo Switch'),
        ('MOBILE','Mobile')
    ]

    title = models.CharField(max_length=225)
    platform = models.CharField(max_length=50,choices=PLATFORM_CHOICES)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.title
