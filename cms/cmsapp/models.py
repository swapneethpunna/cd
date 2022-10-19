from django.db import models
from django.forms import CharField, DateField

# Create your models here.
class regform(models.Model):
    # Question=models.CharField(max_length=30)
    answer=models.CharField(max_length=30)
    

