from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

class Author(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.UUIDField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date published')
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=4096)
    
    def __str__(self):
        return self.author + '_' + self.title
        
    def was_published_recently(self):
        return self.create_date >= timezone.now() - datetime.timedelta(days=1)
        

