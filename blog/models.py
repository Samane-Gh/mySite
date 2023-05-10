# Create your models here.
from django.db import models
class Post(models.Model):
    
    title = models.CharField(max_length=350)
    content = models.TextField() 
    counted_views = models.IntegerField()
    status = models.BooleanField(default=False)
    creted_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True) #2023-05-01 07:04:11.160718
    published_date = models.DateTimeField(null=True)

    def __str__(self):
         return self.title