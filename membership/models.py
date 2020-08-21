from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    date_published = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    article = models.TextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.headline


class HealthQuestions(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    how_often = models.CharField(max_length=100)
    what_times = models.CharField(max_length=100)
    favourite_way = models.CharField(max_length=100)
    supplement = models.CharField(max_length=100)
    Where_you_hear = models.CharField(max_length=100)

    def __str__(self):
        return self.user
