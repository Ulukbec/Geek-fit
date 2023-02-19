from rest_framework import serializers
from .models import *
from phonenumber_field.serializerfields import PhoneNumberField


class PersonalInformSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInform
        fields = 'id image name gmail gender phone'.split()


class MyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCard
        fields = 'full_name card_number month year cvc'.split()


class FavoritesPersonalInformSerializer(serializers.HyperlinkedModelSerializer):
    personal_inform = PersonalInformSerializer(many=True)

    class Meta:
        model = FavoritesPersonalInform
        fields = 'favorites personal_inform'.split()


class FavoritesSerializer(serializers.HyperlinkedModelSerializer):
    favorites_personal_inform = PersonalInformSerializer(many=True)

    class Meta:
        model = Favorites
        fields = 'user favorites_personal_inform'.split()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    favorites = FavoritesSerializer(many=True)

    class Meta:
        model = User
        fields = 'id basket'.split()


class MyCardValidateSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=200)
    card_number = serializers.DecimalField(max_digits=16, decimal_places=0)
    month = serializers.IntegerField(max_value=12, min_value=1)
    year = serializers.IntegerField(min_value=23)
    cvc = serializers.DecimalField(max_digits=3, decimal_places=0)


class PersonalInformValidateSerializer(serializers.Serializer):
    image = serializers.ImageField(default='Без_названия.jpg')
    name = serializers.CharField()
    gmail = serializers.EmailField()
    phone = PhoneNumberField()
    gender = serializers.CharField()
