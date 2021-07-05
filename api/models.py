from django.db import models

# Create your models here.
class Dress(models.Model):
    name=models.CharField(max_length=100)
    rental=models.IntegerField()
    security=models.IntegerField()
    size=models.CharField(max_length=5)
    productID=models.CharField(max_length=15)
    color=models.CharField(max_length=20)
    material=models.CharField(max_length=20)
    neck_design=models.CharField(max_length=20)
    sleeves=models.CharField(max_length=20)
    designer=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name