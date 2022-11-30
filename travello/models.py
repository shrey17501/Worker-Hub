from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.TextField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default='False')

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name








# class Registerasworker(models.Model):
#     first_name = models.CharField(max_length=122)
#     last_name = models.CharField(max_length=122)
#     username = models.CharField(max_length=10)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=12)
#     password1 = models.CharField(max_length=10)
#     password2 = models.CharField(max_length=10)
#     profession = models.TextField()
    
     