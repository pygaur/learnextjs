from django.db import models

# Create your models here.
class Player(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=128)
    email=models.EmailField()