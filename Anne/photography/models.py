from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    picture_of_work = models.ImageField(upload_to='photography/static/')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    name = models.CharField(max_length=50)
    is_sold = models.BooleanField(default=False)