from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Training(models.Model):
    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    title = models.TextField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='categories', null=True
    )
    favourites = models.ManyToManyField(
        User, related_name='favourite',
        default=None, blank=True
    )
    is_active = models.BooleanField(default=False)

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


STAR_CHOICES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    training = models.ForeignKey(
        Training, on_delete=models.CASCADE,
        related_name='reviews', null=True
    )
    stars = models.IntegerField(choices=STAR_CHOICES, default=0)

    def __str__(self):
        return self.text
