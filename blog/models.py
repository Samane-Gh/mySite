# Create your models here.
from django.db import models
class post(models.Model):
    title = models.CharField(max_length=350)
    content = models.TextField() 

