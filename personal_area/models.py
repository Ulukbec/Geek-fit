from django.db import models


# Create your models here.

class PersonalInform(models.Model):
    gmail = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField()
    gender = models.BooleanField(default=False)
