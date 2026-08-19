from django.db import models
from django.contrib.auth.models import User

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='support_tickets')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    photo_main = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_1 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='support_tickets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket #{self.id} - {self.subject} by {self.email}"
