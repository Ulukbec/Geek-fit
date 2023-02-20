from django.db import models
from django.contrib.auth.models import User

LEVEL_CHOICES = (('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard'))

class Training(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50)
    category = models.CharField(choices=LEVEL_CHOICES, max_length=50, null=True, blank=True)
    link = models.CharField(max_length=250)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.title

