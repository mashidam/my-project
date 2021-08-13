from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=25)
    middle_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    date_of_birth=models.DateField()
    email=models.EmailField(default="example@gmail.com")
    



