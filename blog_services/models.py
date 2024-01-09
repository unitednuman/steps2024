from django.db import models


# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, default="Anonymous")
    last_name = models.CharField(max_length=100, null=False, blank=False, default="Anonymous")
    email = models.EmailField(null=False, blank=False)
    phone_number = models.IntegerField(blank=False)
