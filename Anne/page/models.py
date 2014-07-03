from django.db import models

class artwork(models.Model):
    isSold = models.BooleanField(default=False)
    art = models.ImageField(upload_to='/images/')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

class photography(models.Model):
    isSold = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='/images/')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

class design(models.Model):
    isSold = models.BooleanField(default=False)
    design = models.ImageField(upload_to='/images/')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)

class message(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
