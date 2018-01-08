from django.db import models
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.DO_NOTHING,)
    aId  = models.IntegerField(default=0)
    press = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True)
    published_date = models.DateTimeField(default=timezone.now)
    crawled_date = models.DateTimeField(default=timezone.now)
    title = models.TextField()
    text = models.TextField()
    url = models.URLField(default="https://")    
    #sentiment = document.sentiment
    #추후 구현
    def __str__(self):
        return self.title

class Requirement(models.Model):
    user_id = models.CharField(max_length=200,default="")
    press = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200,default="")
    date = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.user_id
