# Generated by Django 4.1.5 on 2023-02-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeksfit', '0002_alter_training_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]
