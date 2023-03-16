from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Training(models.Model):
    image = models.ImageField(default='user.png')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
<<<<<<< HEAD
    duration = models.PositiveIntegerField(default=60)
=======
    duration = models.PositiveIntegerField()
>>>>>>> adf4293ed7d76528e7f8e775232b737b04318074

    def __str__(self):
        return self.title


class FavoriteTraining(models.Model):
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user}_{self.training}'
