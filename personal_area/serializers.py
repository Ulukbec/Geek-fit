from rest_framework import serializers
from .models import *


class PersonalInformSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInform
        fields = 'gmail phone_number gender'


class PersonalInformValidateSerializer(serializers.Serializer):
    gmail = serializers.CharField()
    phone_number = serializers.IntegerField()
    gender = serializers.BooleanField()
