from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title


class FavoriteTraining(models.Model):
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user}_{self.training}'
