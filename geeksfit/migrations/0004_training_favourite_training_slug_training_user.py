# Generated by Django 4.1.5 on 2023-02-21 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geeksfit', '0003_alter_training_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='post_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='training',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='training',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
