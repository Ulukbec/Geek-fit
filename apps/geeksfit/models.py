from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Training(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    def __str__(self):
        return self.title

STAR_CHOICES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(choices=STAR_CHOICES, default=0)

    def __str__(self):
        return self.text
