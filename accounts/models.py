from django.db import models

# Create your models here.
class Account(models.Model):
    listing = models.CharField(max_length=100)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    chef_email = models.EmailField(null=True)
    message = models.TextField()
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name