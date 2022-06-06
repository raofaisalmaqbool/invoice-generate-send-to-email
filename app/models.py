from django.db import models
import datetime

# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=50,default="Faisal")
    address = models.CharField(max_length=150,default="Lahore")
    phone = models.IntegerField(default='+0000000000')
    date = models.DateTimeField(auto_now_add=True)

class buyer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.EmailField(default='None')
    purchase_date = models.DateField(default=datetime.datetime.now)

class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
