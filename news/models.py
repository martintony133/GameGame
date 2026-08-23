from django.db import models
from .choices import themes 

class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=30, choices=themes.items(), default=())
    content = models.TextField(blank=True, null=True)
    photo_1 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 =models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2= models.TextField(blank=True)
    paragraph_3= models.TextField(blank=True)
    paragraph_4= models.TextField(blank=True)
    paragraph_5= models.TextField(blank=True)
    paragraph_6= models.TextField(blank=True)
    paragraph_7= models.TextField(blank=True)
    paragraph_8= models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title



