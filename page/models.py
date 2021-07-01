from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    number=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile',null=True)