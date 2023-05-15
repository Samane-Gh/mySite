# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name


class Post(models.Model):
    image =models.ImageField(upload_to='blog/',default='blog/defult.jpg')
    auther =models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=350)
    content = models.TextField() 
    #tag
    Category =models.ManyToManyField(Category)
    counted_views = models.IntegerField()
    status = models.BooleanField(default=False)
    creted_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True) #2023-05-01 07:04:11.160718
    published_date = models.DateTimeField(null=True)

    def __str__(self):
         return self.title
     
    def snippets(self):
        return self.content[:100]+"..."
    