from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class RecommendGame(models.Model):
    
    GAME_TYPE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Multiplayer', 'Multiplayer'),
        ('Casual','Casual'),
        ('Dating Sims','Dating Sims'),
        ('Tower Defense','Tower Defense'),
        ('Indie','Indie'),
        ('Sports','Sports'),
        ('Strategy','Strategy'),
        ('Racing','Racing'),
        ('Space','Space'),
        ('Horror','Horror'),
        ('Sci-Fi & Cyberpunk','Sci-Fi & Cyberpunk'),
    ]

    RANK_TYPE_CHOICES = [
        ('Free Rank','Free Rank'),
        ('Paid Rank','Paid Rank'),
        ('None','None'),
    ]
    
    title = models.CharField(max_length=200)
    game_type = MultiSelectField(max_length=250, choices=GAME_TYPE_CHOICES, default='', blank=True, null=True)
    description = models.TextField()
    platform = models.CharField(max_length=100)
    developer = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    is_free = models.BooleanField(default=False)
    price = models.IntegerField()
    rank_type = models.CharField(max_length=20,choices=RANK_TYPE_CHOICES,default='none')
    rank = models.IntegerField(default=0,blank=True,null=True)
    download_count = models.BigIntegerField(default=0)
    download_text = models.CharField(max_length=50,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title