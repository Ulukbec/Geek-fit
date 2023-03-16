from rest_framework import serializers
from .models import *
from phonenumber_field.serializerfields import PhoneNumberField
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class PersonalInformSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInform
        fields = 'id image name phone gender'.split()


class MyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCard
        fields = 'full_name card_number month year cvc'.split()


class MyCardValidateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    card_number = serializers.DecimalField(max_digits=16, decimal_places=0)
    month = serializers.IntegerField(max_value=12, min_value=1)
    year = serializers.IntegerField(min_value=23)
    cvc = serializers.DecimalField(max_digits=3, decimal_places=0)


class PersonalInformValidateSerializer(serializers.Serializer):
<<<<<<< HEAD
    image = serializers.ImageField(default='user.png')
=======
    image = serializers.ImageField()
>>>>>>> adf4293ed7d76528e7f8e775232b737b04318074
    name = serializers.CharField()
    phone = PhoneNumberField()
    gender = serializers.CharField()
