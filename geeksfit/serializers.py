from rest_framework import serializers
from geeksfit.models import *


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ('title', 'duration')


class TrainingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = 'title description video'.split()


class FavoriteTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTraining
        fields = '__all__'


class TrainingValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.CharField()
