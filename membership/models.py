from django.db import models


class Article(models.Model):

    date_published = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    article = models.TextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.headline
