from django.db import models

# Create your models here.


class Tags(models.Model):
    name = models.CharField(primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, name="title")
    content = models.TextField()
    category = models.CharField()
    tags = models.ManyToManyField(to=Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
