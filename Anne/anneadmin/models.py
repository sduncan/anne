from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    can_upload = models.BooleanField()
    can_sell = models.BooleanField()