from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Watches(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price= models.FloatField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class WatchUpload(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price= models.FloatField()
    image=models.ImageField(upload_to='watchImage/')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Wishlists(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product =models.ManyToManyField(WatchUpload)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Carts(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    products =models.ManyToManyField(WatchUpload)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
