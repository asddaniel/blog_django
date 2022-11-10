from pyclbr import Class
from django.db import models


class Article(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.fields.TextField()
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.user}'