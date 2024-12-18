from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=50)
    password=models.CharField(max_length=50)