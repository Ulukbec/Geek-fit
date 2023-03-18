from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class TrainingLevel(models.Model):
    level = models.CharField(choices=(
        ('Начинающий', 'Начинающий'),
        ('Продолжающий', 'Продолжающий'),
        ('Продвинутый', 'Продвинутый')
    ), max_length=50)

    def __str__(self):
        return self.level


class Training(models.Model):
    level_training = models.ForeignKey(TrainingLevel, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(default=60)

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
