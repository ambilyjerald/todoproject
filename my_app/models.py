from django.db import models

# Create your models here.
class project(models.Model):
    Name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=10)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
