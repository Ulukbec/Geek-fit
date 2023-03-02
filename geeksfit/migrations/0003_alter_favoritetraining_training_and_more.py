# Generated by Django 4.1.5 on 2023-02-24 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geeksfit', '0002_alter_favoritetraining_training_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritetraining',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeksfit.training'),
        ),
        migrations.AlterField(
            model_name='favoritetraining',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
