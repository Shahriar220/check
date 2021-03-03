from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    
