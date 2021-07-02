from django.db import models
from datetime import datetime
from django.db.models.deletion import DO_NOTHING


class Listing(models.Model):
    realtor=models.ForeignKey('realtors.Realtor', on_delete=DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=30)
    decription=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5, decimal_places=1)
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo1=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo2=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo3=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo4=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo5=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo6=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.title


        

