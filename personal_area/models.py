from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.
from rest_framework.authtoken.admin import User


class PersonalInform(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    gmail = models.EmailField()
    phone = PhoneNumberField()
    gender = models.CharField(choices=(
        ("Мужчина", "Мужчина"),
        ("Женщина", "Женщина")
    ), max_length=50)




class MyCard(models.Model):
    full_name = models.CharField(max_length=200)
    card_number = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    cvc = models.IntegerField()
