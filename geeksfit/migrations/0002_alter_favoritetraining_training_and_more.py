# Generated by Django 4.1.5 on 2023-02-23 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geeksfit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritetraining',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='geeksfit.training'),
        ),
        migrations.AlterField(
            model_name='favoritetraining',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
