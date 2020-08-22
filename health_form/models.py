from django.db import models


class HealthQuestions(models.Model):

    how_often = models.CharField(max_length=100, blank=False, null=False)
    what_times = models.CharField(max_length=100, blank=False, null=False)
    favourite_way = models.CharField(max_length=100, blank=False, null=False)
    supplement = models.CharField(max_length=100, blank=False, null=False)
    where_you_hear = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.user
