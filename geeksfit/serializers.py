from rest_framework import serializers
from geeksfit.models import *


class TrainingLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingLevel
        fields = 'level'.split()


class TrainingDetailSerializer(serializers.ModelSerializer):
    level_training = TrainingLevelSerializer(many=False).fields.get('level')

    class Meta:
        model = Training
        fields = 'level_training title description'.split()


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = ('image', 'title', 'duration')


class FavoriteTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTraining()
        fields = 'training user'.split()


class TrainingValidateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
