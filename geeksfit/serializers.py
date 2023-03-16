from rest_framework import serializers
from geeksfit.models import *


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = ('image', 'title', 'duration')


class TrainingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = 'title description'.split()


class FavoriteTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTraining()
        fields = 'training user'.split()


class TrainingValidateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
