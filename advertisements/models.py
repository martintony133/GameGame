from django.db import models

class Advertisement(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Project Name")
    media = models.FileField(upload_to='media/%Y/%m/%d/')
    destination_url = models.URLField(max_length=500, verbose_name="Destination URL (Landing Page)")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    contact_person = models.CharField(max_length=100, verbose_name="Contact Person")
    phone_number = models.CharField(max_length=30, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    company_website = models.URLField(max_length=500, blank=True, null=True, verbose_name="Company Website")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    def __str__(self):
        return self.project_name