# Generated by Django 4.1.5 on 2023-02-22 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeksfit', '0004_training_favourite_training_slug_training_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='favourite',
        ),
        migrations.RemoveField(
            model_name='training',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='training',
            name='user',
        ),
    ]