from django.db import models

def Artwork(models.Model):
    isSold = models.BooleanField(default=False)
    art = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

def Photography(models.Model):
    isSold = models.BooleanField(default=False)
    photo = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

def Design(models.Model):
    isSold = models.BooleanField(default=False)
    design = models.ImageField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

def Message(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
