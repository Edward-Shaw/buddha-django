from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=256)

class Article(models.Model):
    id = models.UUIDField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateTimeField('date published')
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=4096)

