from django.db import models


# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False, default="Anonymous")
    last_name = models.CharField(max_length=100, null=False, blank=False, default="Anonymous")
    email = models.EmailField(null=False, blank=False)
    phone_number = models.IntegerField(blank=False)


class Publisher(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reporter = models.ForeignKey(to=Reporter, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(to=Publisher)
