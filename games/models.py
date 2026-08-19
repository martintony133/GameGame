from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from multiselectfield import MultiSelectField
from recommendations.models import GAME_TYPE_CHOICES
# Create your models here.

class Game(models.Model):
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

    title = models.CharField(max_length=225)
    game_type = MultiSelectField(max_length=250, choices=GAME_TYPE_CHOICES, default='', blank=True, null=True)
    description=models.TextField(blank=True)
    short_description=models.TextField(max_length=250, blank=True)
    platform = MultiSelectField(max_length=250, choices=PLATFORM_CHOICES, default='', blank=True, null=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    status_tag = models.CharField(max_length=50,choices=STATUS_TAG_CHOICES,default='', blank=True, null=True)
    reviews_count = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField()
    is_free = models.BooleanField(default=False, blank=True, null=True)
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
        return self.title

    class Meta:
        db_table = 'games_game'