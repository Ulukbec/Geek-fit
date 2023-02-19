# Generated by Django 4.1.5 on 2023-02-15 12:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('card_number', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cvc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.BooleanField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gender', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=50)),
            ],
        ),
    ]
