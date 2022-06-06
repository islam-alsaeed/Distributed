from distutils.command.upload import upload
from django.db import models
from django.forms import DecimalField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    book_status=[
        ('available','available'),
        ('rented','rented'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250,null= True,blank=True)
    book_photo = models.ImageField(upload_to='photos',null=True,blank=True)
    author_photo = models.ImageField(upload_to='photos',null= True,blank=True)
    pages = models.IntegerField(null= True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null= True,blank=True)
    retail_price_day= models.DecimalField(max_digits=5,decimal_places=2,null= True,blank=True)
    retail_period = models.IntegerField(null= True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=book_status,null= True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null= True,blank=True)
    
    def __str__(self):
        return self.title